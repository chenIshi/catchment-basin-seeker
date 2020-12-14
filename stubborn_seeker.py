'''
Stubborn seeker borrow the main structure from clever Seeker
However, it insist putting aggregators on controller's ToR,
and also make controller's ToR available for placing monitor
'''


from argparse import ArgumentParser
import json, logging

import seeker.podSeeker as Seeker
import judge.simpleJudge as Judge
import updater.simpleUpdater as Updater

class Query():
    def __init__(self, query_id, src_id, dst_id):
        self.query_id = query_id
        self.src_id = src_id
        self.dst_id = dst_id

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def create_env():
    weights = [0] * 20
    queries = [0] * 20
    for i in range(20):
        queries[i] = []
    return weights, queries

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-r", "--read", help="Query input file location", dest="query_location", default="./data/queries.json")
    parser.add_argument("-n", "--number", help="Total query number", dest="query_number", type=int, default=250)
    parser.add_argument("-a", "--aggregator", help="Also deploy aggregator", type=str2bool, nargs='?',
const=True, default=True, dest="deploy_aggr")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    weights, switch_queries = create_env()

    with open(args.query_location, 'r') as read_queries:
        unparsed_queries = read_queries.read()

    input_queries = json.loads(unparsed_queries)


    if args.query_number <= 0:
        logging.error("Query number should be a positive integer !")
        exit()

    # mapping relationship between query and its monitors
    monitors_under_queries = [0] * args.query_number
    for i in range(args.query_number):
        monitors_under_queries[i] = []

    # place all aggregator on controller's ToR first
    weights[0] += args.query_number

    # we first place all query only to edge sw
    # also consider load balance among edge sw
    # but never place monitor on controller's edge sw
    # and always place aggregator on controller's edge sw
    for input_query in input_queries:
        # install monitor for each query
        query = Query(query_id=input_query['query_id'],
            src_id=input_query['src_host_id'],
            dst_id=input_query['dst_host_id'])
        edge_sw1, edge_sw2 = Seeker.find_edge_switch_on_path(
            switch_id1=query.src_id,
            switch_id2=query.dst_id,
            pod_scale=4)
        if weights[edge_sw1] > weights[edge_sw2]:
            weights[edge_sw2] += 1
        else:
            weights[edge_sw1] += 1

    # currently we got the lowest overall tasks
    # since there will only be one monitor for each query entry
    # every query entry on monitor/aggregator is counted as task
    # we take a conservative method, keep most queries far from controller
    if args.deploy_aggr:
        overall_task_count = len(input_queries) + args.query_number
    else:
        overall_task_count = len(input_queries)

    # sandhills are edge monitors awaits to push their task to center sws
    sandhills = sorted(range(len(weights)), key=lambda k: weights[k], reverse=True)

    for sandhill in sandhills:
        if sandhill > 7:
            break
        water_level = weights[sandhill]
        if sandhill == 0:
            water_level -= args.query_number

        for i in range(water_level):
            # the water_level is only for monitor tasks, not included aggregator task
            if sandhill == 0 and weights[0] <= args.query_number:
                break

            # find victim
            aggr_sws = Seeker.find_single_aggr(edge_id=sandhill, pod_scale=4)
            aggr_cost = (weights[aggr_sws[0]] + weights[aggr_sws[1]]) / 2
            hybrid_cost_with_0, hybrid_cost_with_1, core_cost = weights[aggr_sws[0]], weights[aggr_sws[1]], 0
            core_replace_1 = Seeker.find_single_core(aggr_id=aggr_sws[1], pod_scale=4)
            core_replace_0 = Seeker.find_single_core(aggr_id=aggr_sws[0], pod_scale=4)
            for core_sw in core_replace_1:
                hybrid_cost_with_0 += weights[core_sw]
                core_cost += weights[core_sw]
            for core_sw in core_replace_0:
                hybrid_cost_with_1 += weights[core_sw]
                core_cost += weights[core_sw]

            chosen_pos = Judge.find_lowest_cost_node(
                [weights[sandhill], aggr_cost, (hybrid_cost_with_0 / 3), (hybrid_cost_with_1 / 3), (core_cost / 4)],
                [[sandhill], aggr_sws, [aggr_sws[0]] + core_replace_1, [aggr_sws[1]] + core_replace_0, core_replace_0 + core_replace_1])

            if sandhill in chosen_pos:
                    break
            else:
                weights[sandhill] -= 1
                for sw in chosen_pos:
                    weights[sw] += 1



    # dump simple debug result
    for idx, weight in enumerate(weights):
        print("Switch %d weight = %d" % (idx, weight))
    mean = sum(weights) / len(weights)
    std_err = (sum((i - mean) ** 2 for i in weights) / len(weights)) ** 0.5
    print("Overall task number = %d, avg task = %.2f, std error = %.2f" % (sum(weights), mean, std_err))
