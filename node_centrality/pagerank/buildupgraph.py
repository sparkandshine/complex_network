#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx

def build_graph_wikipedia_pagerank_example():
	"""
	Build a graph for https://en.wikipedia.org/wiki/File:PageRanks-Example.svg
	"""

	G = nx.DiGraph()

	# A

	# B --> 
	G.add_path(['B', 'C'])

	# C -->
	G.add_path(['C', 'B'])

	# D --> 
	G.add_path(['D', 'A'])
	G.add_path(['D', 'B'])

	# E --> 
	G.add_path(['E', 'B'])
	G.add_path(['E', 'D'])
	G.add_path(['E', 'F'])

	# F --> 
	G.add_path(['F', 'B'])
	G.add_path(['F', 'E'])

	# G --> 
	G.add_path(['G', 'B'])
	G.add_path(['G', 'E'])

	# H --> 
	G.add_path(['H', 'B'])
	G.add_path(['H', 'E'])

	# I --> 
	G.add_path(['I', 'B'])
	G.add_path(['I', 'E'])

	# J --> 
	G.add_path(['J', 'E'])

	# J --> 
	G.add_path(['K', 'E'])

	return G

def read_graphml_with_position(filename):
	"""Read a graph in GraphML format with position
	"""
	G = nx.read_graphml(filename)
 
	# rearrage node attributes x, y as position for networkx
	pos = dict() # A dictionary with nodes as keys and positions as values. Positions should be sequences of length 2.
	node_and_x = nx.get_node_attributes(G, 'x')
	node_and_y = nx.get_node_attributes(G, 'y')
 
	for node in node_and_x:
		x = node_and_x[node]
		y = node_and_y[node]
		pos[node] = (x, y)
 
	# add node attribute `pos` to G
	nx.set_node_attributes(G, 'pos', pos)
 
	return G



def main():
	# Step 1: Build up a graph 
	G = build_graph_wikipedia_pagerank_example()
	out_file = 'wikipedia_pagerank_example.graphml'
	nx.write_graphml(G, out_file)

	'''
	in_file = 'wikipedia_pagerank_example_layout.graphml'
	G = read_graphml_with_position(in_file)
	'''

if __name__ == '__main__':
	main()