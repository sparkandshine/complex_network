#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


"""
Draw trees with pygraphviz
"""

def main():
    # Create a directed graph
    G = nx.DiGraph()

    # An example
    l=[ ('a','b'),
        ('b','c'),
        ('c','d'),
        ('d','e'),
        ('e','f'),
        ('w','x'),
        ('w','t'),
        ('t','q'),
        ('q','r'),
        ('q','u')]

    # Build up a graph
    for t in l:
        G.add_edge(t[0], t[1])

    # Plot trees
    pos = graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, arrows=False)

    plt.savefig('draw_trees_with_pygraphviz.png', bbox_inches='tight')   
    plt.show()

if __name__ == '__main__':
    main()

