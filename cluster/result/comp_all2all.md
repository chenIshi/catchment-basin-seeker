## Testing parameter
1000 query tasks, 32 pods, a percentage of queries are spanned by all-to-all query
And an all-to-all query is involved with 5 sources. And we only want 5 final multicast group.
We varies the percentage rate from 80% to 20% in this experiment.

## Results
%,cost
80,28
75,61
70,38
65,58
60,69
55,67
50,85
45,84
40,129
35,159
30,195
25,201
20,270
