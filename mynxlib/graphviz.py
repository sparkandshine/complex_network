#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Graph visulization
"""

import matplotlib.pyplot as plt
import networkx as nx
import os

class PlotGraph:
    """plot graph"""
    @classmethod
    def plot_graph(cls, G, filename=None, node_attribute_name='id', edge_attribute_name=None, 
                    colored_nodes=None, colored_edges=None, colored_path=None, **kwargs):
    #def plot_graph(self, G, out_file, **kwd):
        """plot graph"""
        plt.clf()

        # get the layout of G
        pos = nx.get_node_attributes(G, 'pos')
        if not pos:
            pos = nx.spring_layout(G)

        # get node attributes
        with_labels = False
        node_labels = None
        if node_attribute_name == 'id':
            with_labels = True
        elif node_attribute_name:
            node_labels = nx.get_node_attributes(G, node_attribute_name)

        # get edge attributes
        if not edge_attribute_name:
            edge_labels = nx.get_edge_attributes(G, edge_attribute_name)

        # colored nodes
        node_default_color = '0.75' # Gray shades 

        node_color = node_default_color
        if colored_nodes:
            node_color = ['r' if node in colored_nodes else node_default_color
                            for node in G.nodes()]

        # colored path
        if colored_path:
            nrof_nodes = len(colored_path)
            idx = 0
            colored_edges = list()
            while idx < nrof_nodes-1:
                colored_edges.append((colored_path[idx], colored_path[idx+1]))
                idx += 1

        # colored edges
        edge_default_color = 'k' # black
        edge_color = edge_default_color
        if colored_edges:
            set_colored_edges = {frozenset(t) for t in colored_edges}  # G.edges returns a list of 2-tuples

            edge_color = ['r' if frozenset([u, v]) in set_colored_edges else edge_default_color
                            for u, v in G.edges()]


        # draw 
        nx.draw(G, pos, with_labels=with_labels, node_color=node_color, edge_color=edge_color, **kwargs)
        if node_labels:
            nx.draw_networkx_labels(G, pos, labels=node_labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        if filename:
            plt.savefig(filename, bbox_inches='tight', pad_inches=0)
        else:
            plt.show()


class FormatConverter:
    """converter different graph format
    """

    @classmethod
    def read_graphml_with_position(cls, filename):
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
