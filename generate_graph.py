# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:52:17 2021

@author: Dion
"""

# Generate graph data

from streamlit_agraph import Config, Edge, Node, agraph

def generate_graph(nodes, paths, layout, rankdir, ranksep, nodesep):
        
    all_nodes = []
    all_edges = []
    for node in nodes:
        all_nodes.append(Node(id=node, 
                          label=node, 
                          symbolType='square'))
    for path in paths:
            all_edges.append(
                Edge(source=path[0],
                     target=path[1], 
                    type="STRAIGHT")
            )

    config = Config(width=500, 
                    height=500,
                    graphviz_layout=layout,
                    graphviz_config={"rankdir": rankdir, "ranksep": ranksep, "nodesep": nodesep},
                    directed=True,
                    nodeHighlightBehavior=True, 
                    highlightColor="#F7A7A6",
                    collapsible=True,
                    node={'labelProperty':'label'},
                    link={'labelProperty': 'label', 'renderLabel': True},
                    maxZoom=2,
                    minZoom=0.1,
                    staticGraphWithDragAndDrop=False,
                    staticGraph=False,
                    initialZoom=1
                    ) 

    
    return agraph(nodes=all_nodes, 
                  edges=all_edges, 
                  config=config)