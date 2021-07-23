## Testing parameter
1000 query tasks, 32 pods, a percentage of queries are spanned by all-to-all query
And an all-to-all query is involved with 10 sources. And we only want 10 final multicast group.
We varies the percentage rate from 80% to 5% in this experiment.

## Results
%,cost
80,20
75,19
70,16
65,72
60,76
55,62
50,75
45,66
40,60
35,109
30,111
25,106
20,112
15,111
10,189
5,313
