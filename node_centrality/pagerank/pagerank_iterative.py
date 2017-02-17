#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from networkx.exception import NetworkXError
import numpy as np
import operator

# Custom package
import buildupgraph
import plotnxgraph

def pagerank(G, alpha=0.85, personalization=None,
			 max_iter=100, tol=1.0e-6, nstart=None, weight='weight',
			 dangling=None):
	"""
	Return the PageRank of the nodes in the graph.
	Source code from http://networkx.readthedocs.io/en/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html#pagerank
	"""
	if len(G) == 0:
		return {}

	if not G.is_directed():
		D = G.to_directed()
	else:
		D = G

	# Step 1: Create a copy in (right) stochastic form
	W = nx.stochastic_graph(D, weight=weight)
	N = W.number_of_nodes()						# N = 11

	# Plot the stochastic graph
	out_file = 'wikipedia_pagerank_example_stochastic_graph.pdf'
	edge_and_labels = {k : round(v, 2) for k, v in nx.get_edge_attributes(W, 'weight').items()}
	plot_graph(W, out_file=out_file, edge_and_labels=edge_and_labels)


	# Step 2: Choose fixed starting vector if not given
	if nstart is None:
		x = dict.fromkeys(W, 1.0 / N)
	else:
		# Normalized nstart vector
		s = float(sum(nstart.values()))
		x = dict((k, v / s) for k, v in nstart.items())

	# plot a graph with nstart: starting value of PageRank iteration for each node.
	out_file = 'wikipedia_pagerank_example_nstart.pdf'
	node_and_labels = {k : k+'\n'+str(round(v, 2)) 
							for k, v in x.items()}
	plot_graph(W, out_file=out_file, node_and_labels=node_and_labels)

	# Step 3: Assign uniform personalization vector if not given
	if personalization is None:
		p = dict.fromkeys(W, 1.0 / N)	# node and nonzero personalization value for each node
	else:
		missing = set(G) - set(personalization)
		if missing:
			raise NetworkXError('Personalization dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing)
		s = float(sum(personalization.values()))
		p = dict((k, v / s) for k, v in personalization.items())

	# Step 4: Use personalization vector if dangling vector not specified
	if dangling is None:
		dangling_weights = p
	else:
		missing = set(G) - set(dangling)
		if missing:
			raise NetworkXError('Dangling node dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing)
		s = float(sum(dangling.values()))
		dangling_weights = dict((k, v/s) for k, v in dangling.items())

	dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]


	# Step 5: power iteration: make up to max_iter iterations
	for _ in range(max_iter):
		xlast = x 							# pagerank for each node
		x = dict.fromkeys(xlast.keys(), 0)
		danglesum = alpha * sum(xlast[n] for n in dangling_nodes)

		for n in x:
			# this matrix multiply looks odd because it is
			# doing a left multiply x^T=xlast^T*W
			for nbr in W[n]:
				x[nbr] += alpha * xlast[n] * W[n][nbr][weight]	# PR(p_i) = d * PR(p_j)}/L(p_j)

			x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]	# danglesum/N  + (1-d)/N


		# Plot graph with one iteration
		'''
		out_file = 'wikipedia_pagerank_example_iteration_1.pdf'
		node_and_pr = x
		node_size = [pr*30000 for node, pr in node_and_pr.items()]
		node_and_labels = {node : node+'\n'+str(round(pr, 3))
							for node, pr in node_and_pr.items()}

		plot_graph(G, out_file=out_file, node_size=node_size, node_and_labels=node_and_labels)
		'''

		# check convergence, l1 norm
		err = sum([abs(x[n] - xlast[n]) for n in x])
		if err < N*tol:
			return x

	raise NetworkXError('pagerank: power iteration failed to converge in %d iterations.' % max_iter)


def pagerank_iterative(G, d=0.85, max_iter=100, tol=1.0e-6, weight='weight'):
	"""
	PageRank calculation iteratively
	"""

	# Step 1: Initiate PageRank
	N = G.number_of_nodes()						# N = 11
	node_and_pr = dict.fromkeys(G, 1.0 / N)

	# Step 2: Create a copy in (right) stochastic form
	stochastic_graph = nx.stochastic_graph(G, weight=weight)	# M = 1/L(pj)

	# Step 3: Power iteration: make up to max_iter iterations
	dangling_value = (1-d)/N

	for _ in range(max_iter):		# for each iteration
		node_and_prev_pr = node_and_pr
		node_and_pr = dict.fromkeys(node_and_prev_pr.keys(), 0)

		for node in node_and_pr:	# for each node
			for out_node in stochastic_graph[node]:		# node --> out_node
				node_and_pr[out_node] += d * node_and_prev_pr[node] * stochastic_graph[node][out_node][weight] 	# PR(p_i) = d * PR(p_j)}/L(p_j)
		
			node_and_pr[node] += dangling_value

		# Plot graph with one iteration
		'''
		out_file = 'wikipedia_pagerank_example_iteration_1.pdf'
		node_size = [pr*30000 for node, pr in node_and_pr.items()]
		node_and_labels = {node : node+'\n'+str(round(pr, 3))
							for node, pr in node_and_pr.items()}

		plotnxgraph.plot_graph(G, out_file=out_file, node_size=node_size, node_and_labels=node_and_labels)
		return
		'''

		# check convergence, l1 norm
		err = sum([abs(node_and_pr[node] - node_and_prev_pr[node]) for node in node_and_pr])
		if err < N*tol:
			return node_and_pr

	raise NetworkXError('pagerank: power iteration failed to converge in {} iterations.'.format(max_iter))


def main():
	# Step 1: Build up a graph 
	'''
	G = buildupgraph.build_graph_wikipedia_pagerank_example()
	out_file = 'wikipedia_pagerank_example.graphml'
	nx.write_graphml(G, out_file)
	'''

	in_file = 'wikipedia_pagerank_example_layout.graphml'	# Visualize the graph with the help of Graphviz
	G = buildupgraph.read_graphml_with_position(in_file)

	# Step 2: PageRank calculation
	node_and_pr = pagerank_iterative(G)

	# Normalized PageRank
	total_pr = sum(node_and_pr.values())		# 0.843339703286
	node_and_pr = {node : pr/total_pr for node, pr in node_and_pr.items()}

	# Plot the graph
	node_size = [pr*30000 for node, pr in node_and_pr.items()]
	node_and_labels = {node : node+'\n'+str(round(pr, 3))
							for node, pr in node_and_pr.items()}

	plotnxgraph.plot_graph(G, node_size=node_size, node_and_labels=node_and_labels)


if __name__ == '__main__':
	main()