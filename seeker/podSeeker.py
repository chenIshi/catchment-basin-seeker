import math, logging

'''
Find edge switches (ToR switches) along assigned routing from switch_id1
to switch_id2
- pod_scale: overall pod number in the topology, should be 2's multiples
'''
def find_edge_switch_on_path(switch_id1: int, switch_id2: int, pod_scale: int):
    if pod_scale % 2 != 0:
        logging.error("Wrong input in find_edge_switch_on_path: pod_scale should be even")
        return
    else:
        server_within_the_same_edge_sw = float(pod_scale / 2)
        # Edge switch id = ⌈server_id /  server_within_the_same_edge_sw⌉
        return [math.floor(switch_id1 / server_within_the_same_edge_sw),
            math.floor(switch_id2 / server_within_the_same_edge_sw)]

'''
Find aggr switches along assigned routing from edge_id1 to edge_id2
- pod_scale: overall pod number in the topology, should be 2's multiples
'''
def find_aggr_switch_on_path(edge_id1: int, edge_id2: int, pod_scale: int):
    if pod_scale % 2 != 0:
        logging.error("Wrong input in find_aggr_switch_on_path: pod_scale should be even")
        return
    total_edge_sw_number = pod_scale * (int(pod_scale / 2))
    aggr_sw_within_the_same_pod = int(pod_scale / 2)
    edge_sw_within_the_same_pod = int(pod_scale / 2)
    pod1 = math.floor(edge_id1 / edge_sw_within_the_same_pod)
    pod2 = math.floor(edge_id2 / edge_sw_within_the_same_pod)
    starting_aggr_id1 = total_edge_sw_number + pod1 * aggr_sw_within_the_same_pod
    starting_aggr_id2 = total_edge_sw_number + pod2 * aggr_sw_within_the_same_pod
    aggr_id1 = []
    aggr_id2 = []
    for i in range(int(edge_sw_within_the_same_pod)):
        aggr_id1.append(starting_aggr_id1 + i)
        aggr_id2.append(starting_aggr_id2 + i)
    return [aggr_id1, aggr_id2]

'''
Find core switches along assigned routing from switch_id1 to switch_id2
- pod_scale: overall pod number in the topology, should be 2's multiples
'''
def find_core_switch_on_path(pod_scale: int):
    if pod_scale % 2 != 0:
        logging.error("Wrong input in find_core_switch_on_path: pod_scale should be even")
        return
    total_pod_switch_number = pod_scale ** 2
    # total_server_number = (pod_scale ** 2) / 2
    total_core_switch_number = (pod_scale / 2) ** 2
    core_id = []
    for i in range(int(total_core_switch_number)):
        core_id.append(total_pod_switch_number + i)
    return core_id

if __name__ == "__main__":
    edge_sw1, edge_sw2 = find_edge_switch_on_path(switch_id1=1, switch_id2=5, pod_scale=4)
    aggr_sw1, aggr_sw2 = find_aggr_switch_on_path(edge_id1=edge_sw1, edge_id2=edge_sw2, pod_scale=4)
    core_sw = find_core_switch_on_path(pod_scale=4)
    print(edge_sw1)
    print(edge_sw2)
    print(aggr_sw1)
    print(aggr_sw2)
    print(core_sw)
