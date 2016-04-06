#!/usr/bin/env python
# -*- coding: utf-8 -*-#

import networkx as nx

# custom modules
from dominatingsets import DominatingSets

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

	# calculate a connected dominating set
	cds = DominatingSets.min_connected_dominating_sets_non_distributed(G)

	# draw the graph
	out_file = 'florentine_families_graph_cds_non_distributed.png'
	PlotGraph.plot_graph(G, filename=out_file, colored_nodes=cds)

if __name__ == '__main__':
	main()