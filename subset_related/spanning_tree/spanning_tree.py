#!/usr/bin/env python
# -*- coding: utf-8 -*-#

import networkx as nx

# import the custom module for drawing a graph 

import sys
import os 
# add the parent directory ../../ to PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) 

from mynxlib.graphviz import PlotGraph

def main():
	# build up a graph
	filename = '../../florentine_families_graph.gpickle'
	G = nx.read_gpickle(filename)

	# Spanning tree
	mst = nx.minimum_spanning_tree(G) 
	out_file = 'florentine_families_graph_minimum_spanning_tree.png'
	PlotGraph.plot_graph(G, filename=out_file, colored_edges=mst.edges())

	edges = nx.minimum_spanning_edges(G, weight='weight', data=True)
	list_edges = list(edges)
	print(list_edges)


if __name__ == '__main__':
	main()