#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G, out_file=None, node_size=1500, font_size=10,
				node_and_labels=None, edge_and_labels=None):
	"""
	plot a graph
	"""

	pos = nx.get_node_attributes(G, 'pos')
	if not pos:
		pos = nx.spring_layout(G)

	nx.draw_networkx(G, pos, node_size=node_size, 
						node_color='w', 
						edge_color='k', 
						labels = node_and_labels,
						font_size=font_size,
						font_color='r',
						arrows=True,
						with_labels=True)

	plt.axis('off')	

	if edge_and_labels:
		nx.draw_networkx_edge_labels(G, pos, 
										edge_labels=edge_and_labels, 
										font_color='r',
										label_pos=0.4, 
										alpha=0.0)

	if out_file:
		plt.savefig(out_file, bbox_inches='tight')

	plt.show()

def main():
	pass

if __name__ == '__main__':
	main()