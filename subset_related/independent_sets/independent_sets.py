#!/usr/bin/env python
# -*- coding: utf-8 -*-#

import networkx as nx
import networkx.algorithms.approximation as nxaa

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

	# Indepedent set
	maximal_iset = nx.maximal_independent_set(G)
	out_file = 'florentine_families_graph_maximal_iset.png'
	PlotGraph.plot_graph(G, filename=out_file, colored_nodes=maximal_iset)

	maximum_iset = nxaa.maximum_independent_set(G)
	out_file = 'florentine_families_graph_maximum_iset.png'
	PlotGraph.plot_graph(G, filename=out_file, colored_nodes=maximum_iset)

if __name__ == '__main__':
	main()