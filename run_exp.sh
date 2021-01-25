#!/bin/bash

dot_per_box=10
hop_size=250
total_hop_steps=12
exec_time_output_dstfile="/home/lthpc/git/catchment-basin-seeker/plot/exec_time.txt"

# clear output dst first
> $exec_time_output_dstfile

for (( hops=1; hops<=total_hop_steps; hops++ ))
do
	let query_counts=hops*hop_size
	echo "$query_counts" >> $exec_time_output_dstfile
	# printf "\n"
	for (( counter=dot_per_box; counter>0; counter-- ))
	do
		python3 data/gen_query.py -n $query_counts -e 4
		python gurobi/bipartite.py | grep "iterations) in" | awk '{print $8}' >> $exec_time_output_dstfile
		# echo -n "$counter "
	done
	printf "\n" >> $exec_time_output_dstfile
done
printf "\n"
