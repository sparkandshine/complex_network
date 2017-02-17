#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx

# Custom packages
import plotnxgraph

def pagerank_ab():
	"""
	Calculate PageRank for A <--> B
	"""
	pr = {'A':1.0, 'B':1.0}
	max_iter = 50

	for idx in range(1, max_iter+1):
		pr['A'] = 0.15/2 + 0.85*pr['B']
		pr['B'] = 0.15/2 + 0.85*pr['A']

		s = '{:3d}: A={:<10f}\tB={:<10f}'.format(idx, pr['A'], pr['B'])
		print(s)

def plot_graph_pagerank(G, out_file=None):
	"""
	plot networkx graph whose node label is PageRank
	"""
	node_and_pr = nx.pagerank(G)

	node_size = [pr*20000 for node, pr in node_and_pr.items()]
	node_and_labels = {node : node+'\n'+str(round(pr, 3))
						for node, pr in node_and_pr.items()}

	plotnxgraph.plot_graph(G, out_file=out_file, node_size=node_size, 
							node_and_labels=node_and_labels, font_size=15)

def main():

	# Example 1: A <---> B
	# build up a graph
	G = nx.DiGraph()
	G.add_node('A', pos=(1,0))
	G.add_node('B', pos=(2,0))
	G.add_path(['A', 'B'])
	G.add_path(['B', 'A'])

	# pagerank_ab()

	plotnxgraph.plot_graph(G, 'simple_example_pagerank_a_b.pdf', node_size=10000, font_size=15)
	#node_and_pr = nx.pagerank(G, max_iter=20)

	# plot a graph
	out_file = 'simple_examples_A_B.pdf'
	plot_graph_pagerank(G, out_file)

	# Example 2: looping, A --> B --> C --> D --> A
	G = nx.DiGraph()
	G.add_node('A', pos=(1,1))
	G.add_node('B', pos=(2,1))
	G.add_node('C', pos=(2,0))
	G.add_node('D', pos=(1,0))
	G.add_path(['A', 'B', 'C', 'D', 'A'])

	out_file = 'simple_examples_loop.pdf'
	plot_graph_pagerank(G, out_file)

	# Example 3: A --> B --> C <--> A
	G = nx.DiGraph()
	G.add_node('A', pos=(1,1))
	G.add_node('B', pos=(3,1))
	G.add_node('C', pos=(2,0))
	G.add_path(['A', 'B', 'C', 'A'])
	G.add_path(['A', 'C']) 

	out_file = 'simple_examples_triangle.pdf'
	plot_graph_pagerank(G, out_file)

	# Example 4: (B, C, D) --> A
	G = nx.DiGraph()
	G.add_node('B', pos=(1,3))
	G.add_node('C', pos=(1,2))
	G.add_node('D', pos=(1,1))
	G.add_node('A', pos=(2,2))
	G.add_path(['B', 'A'])
	G.add_path(['C', 'A'])
	G.add_path(['D', 'A'])

	out_file = 'simple_examples_dangling_node.pdf'
	plot_graph_pagerank(G, out_file)	

if __name__ == '__main__':
	main()