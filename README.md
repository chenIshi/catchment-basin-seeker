# catchment-basin-seeker
Find monitor and aggregator placement in a pod topology

A control plane simple algorithm(?) to discover lowest cost monitor &
aggregator placement in datacenter pod topology network.

![Pod Topo](/image/pod-topo.png)

In a pod topo, each host (server) is connected to a destinated edge switch (ToR), while
it can latter choose from (k/2) aggregation switch, and then a destinated core switch
for routing to destinated host once aggregation switch is chosen. See []() for more
details.

We thus, label the switch with int ids. Starting from 0 in the first edge switch ("first"
here correspond to host order), then iterates through all k<sup>2</sup>/2 edge
switches, then we move on to iteration of k<sup>2</sup>/2 aggregation switches,
finally k<sup>2</sup>/4 iteration of core switches

As a result, we unfold the tree operation to an array operation, so there won't be any
tree data structure, just 2D array look up.

## Environment Requirement
1. python verion >= 3.6.9 (Tested under 3.6.9)
