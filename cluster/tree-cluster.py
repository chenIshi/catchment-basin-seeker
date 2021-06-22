#!/usr/bin/python3

from argparse import ArgumentParser
from sklearn.cluster import KMeans
from scipy.spatial import distance
import json, logging

def one_hot_encoder(inputs: list, size:int):
    ret_list = [0] * size
    for set_bit in inputs:
        ret_list[int(set_bit)] = 1
    return ret_list
	

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pod", help="Number of pod in network topology", dest="pod", type=int, default=30)
    parser.add_argument("-q", "--query", help="Number of overall queries", dest="query", type=int, default=1000)
    parser.add_argument("-c", "--cluster", help="Number of query cluster", dest="cluster", type=int, default=20)

    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
        
    with open("/home/lthpc/git/catchment-basin-seeker/data/queries-v2.json") as input:
        unparsed_queries = input.read()

    # TODO: ADD support for multiple imbalanced sources in gen_query module
    queries = json.loads(unparsed_queries)

    flat_queries = []
    for query in queries:
        flat_queries.append(one_hot_encoder(inputs=query["src"], size=args.pod))

    logging.info("Done preprocess.")

    kmeans = KMeans(n_clusters=args.cluster)
    kmeans.fit(flat_queries)
    print(kmeans.labels_)
    # y_kmeans = kmeans.predict(X)

	logging.info("Done clustering.")

	# Evaluate objective performance
	products = [0] * args.cluster
	sources = [0] * args.cluster
	for i in range(args.cluster):
		products[i] = []
		sources[i] = []
	for index, label in enumerate(kmeans.labels_):
		if not products[label]:
			products[label] = flat_queries[index]
		else:
			result = list(a|b for a,b in zip(products[label], flat_queries[index]))
			products[label] = result
		sources[label].append(index)

	cost = 0
	for i in range(args.cluster):
		for product in products[i]:
			for source in sources[i]:
				for idx in source: 
					cost += distance.hamming(product, flat_queries[idx])
			
	




	
		


	
