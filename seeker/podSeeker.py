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

'''
Assume controller being host 1
Also, how source routing did is one concern
'''
def find_route_to_controller(src_addr_id: int):
    if src_addr_id == 1:
        print("Monitor can't be set on controller's ToR !")
        return []
    elif src_addr_id == 2:
        return [10, 1]
    elif src_addr_id == 3:
        return [11, 17, 9, 1]
    elif src_addr_id == 4:
        return [12, 19, 10, 1]
    elif src_addr_id == 5:
        return [13, 18, 9, 1]
    elif src_addr_id == 6:
        return [14, 20, 10, 1]
    elif src_addr_id == 7:
        return [15, 17, 9, 1]
    elif src_addr_id == 8:
        return [16, 19, 10, 1]
    elif src_addr_id == 9:
        return [13, 18, 9, 1]
    elif src_addr_id == 10:
        return [1]
    elif src_addr_id == 11:
        return [18, 9, 1]
    elif src_addr_id == 12:
        return [20, 10, 1]
    elif src_addr_id == 13:
        return [17, 9, 1]
    elif src_addr_id == 14:
        return [19, 10, 1]
    elif src_addr_id == 15:
        return [18, 9, 1]
    elif src_addr_id == 16:
        return [20, 10, 1]
    elif src_addr_id == 17:
        return [9, 1]
    elif src_addr_id == 18:
        return [9, 1]
    elif src_addr_id == 19:
        return [10, 1]
    elif src_addr_id == 20:
        return [10, 1]
    else:
        print("Error: unmatched src addr id in finding route back to controller")
        return []

if __name__ == "__main__":
    edge_sw1, edge_sw2 = find_edge_switch_on_path(switch_id1=1, switch_id2=5, pod_scale=4)
    aggr_sw1, aggr_sw2 = find_aggr_switch_on_path(edge_id1=edge_sw1, edge_id2=edge_sw2, pod_scale=4)
    core_sw = find_core_switch_on_path(pod_scale=4)
    print(edge_sw1)
    print(edge_sw2)
    print(aggr_sw1)
    print(aggr_sw2)
    print(core_sw)
