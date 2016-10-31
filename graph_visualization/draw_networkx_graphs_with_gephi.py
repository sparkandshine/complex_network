#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import copy
import itertools
from collections import OrderedDict
import operator
from datetime import timedelta

import sys
import os 
sys.path.insert(0, '/Users/sparkandshine/git/complex_network')

from mynxlib.graphviz import PlotGraph
from mynxlib import graphviz


def main():

	filename = 'paris_gtfs_graph_layout.graphml'
	G = graphviz.FormatConverter.read_graphml_with_position(filename)

	out_file = 'paris_gtfs_graph.png'
	PlotGraph.plot_graph(G, filename=out_file, node_attribute_name=None, node_size=50)

if __name__ == '__main__':
 	main() 