#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from networkx.exception import NetworkXError
import numpy as np
import operator
import fractions

# Custom package
import buildupgraph

def pagerank_numpy(G, alpha=0.85, personalization=None, weight='weight', dangling=None):
    """Return the PageRank of the nodes in the graph.
    """
    
    if len(G) == 0:
        return {}

    M = nx.google_matrix(G, alpha, personalization=personalization,
                      weight=weight, dangling=dangling)

    # use numpy LAPACK solver
    eigenvalues, eigenvectors = np.linalg.eig(M.T)
    ind = eigenvalues.argsort()

    # eigenvector of largest eigenvalue at ind[-1], normalized
    largest = np.array(eigenvectors[:, ind[-1]]).flatten().real
    norm = float(largest.sum())

    return dict(zip(G, map(float, largest / norm)))

def main():
	# Step 1: Build up a graph 
	'''
	G = build_graph_wikipedia_pagerank_example()
	out_file = 'wikipedia_pagerank_example.graphml'
	nx.write_graphml(G, out_file)
	'''

	in_file = 'wikipedia_pagerank_example_layout.graphml'
	G = buildupgraph.read_graphml_with_position(in_file)

	# Step 2: Compute PageRank algebraically
	#np.set_printoptions(formatter={'float_kind':lambda x: str(fractions.Fraction(x).limit_denominator())})

	np.set_printoptions(precision=2)

	# Part 1: \mathbf {1}  is the column vector of length N containing only ones.
	N = len(G.nodes())		# N = 11
	column_vector = np.ones((N, 1), dtype=np.int)
	#print(column_vector)

	# Part 2: Matrix M
	# Adjacency matrix A
	nodelist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']	# sorted(G.nodes())
	A = nx.to_numpy_matrix(G, nodelist)

	# K is the diagonal matrix with the outdegrees in the diagonal.
	nodelist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']	# sorted(G.nodes())
	list_outdegree = map(operator.itemgetter(1), sorted(G.out_degree().items()))
	K = np.diag(list_outdegree)

	K_inv = np.linalg.pinv(K)

	# Matrix M
	M = (K_inv * A).transpose()

	# Part 3: PageRank calculation
	np.set_printoptions(precision=3)

	d = 0.85
	I = np.identity(N)
	R = np.linalg.pinv(I - d*M) * ((1-d)/N * column_vector)

	R = R/sum(R)	# normalized R, so that page ranks sum to 1.

	print(R)
	return

	# Part 4: Using nx.pagerank_numpy
	#pr = nx.pagerank_numpy(G)
	pr = pagerank_numpy(G)
	print(pr)



if __name__ == '__main__':
	main()