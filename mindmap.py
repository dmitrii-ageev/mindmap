#!/usr/bin/env python3
import sys
import pydot
import yaml


def message(message: str, output=sys.stdout):
    # Write the message to the output stream
    output.write(message + "\n")


def info(message: str):
    # Write the message to the standard output stream
    message("INFO: " + message, sys.stdout)


def error(message: str):
    # Write the message to the standard error stream
    message("ERROR: " + message, sys.stderr)


def fail(message: str):
    # Write the message to the standard error stream and exit
    message("FAIL: " + message, sys.stderr)
    sys.exit(1)


def parse_command_line():
    # Check if the user has provided the correct number of arguments
    if len(sys.argv) != 3:
        message("Usage: python mindmap.py title <mindmap.yaml>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def load_mindmap(filename: str):
    # Load the mindmap from the specified file
    with open(filename, 'r') as f:
        try:
            mindmap = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            fail("Error in configuration file: " + str(exc))
        return mindmap


def add_node(graph, node, mindmap):
    # Add a node to the graph and recursively add child nodes
    if type(mindmap) is list:
        for child in mindmap:
            graph.add_edge(pydot.Edge(node, child))
            graph = add_node(graph, child, child) if type(child) is list or type(child) is dict else graph
    if type(mindmap) is dict:
        childs = mindmap.keys() if type(mindmap) is dict else mindmap
        for child in childs:
            graph.add_edge(pydot.Edge(node, child))
            graph = add_node(graph, child, mindmap[child]) if type(mindmap[child]) is dict else graph
            graph = add_node(graph, child, mindmap[child]) if type(mindmap[child]) is list else graph
    elif type(mindmap) is str or type(mindmap) is int or type(mindmap) is float:
        graph.add_edge(pydot.Edge(node))
    return graph


def create_mindmap(title: str, mindmap: dict, filename: str):
    # Create a mindmap from the specified data
    graph = add_node(pydot.Dot(graph_type='digraph', rankdir='LR'), title, mindmap)
    # Write the graph to a file
    graph.write_png(filename)


def main():
    # Parse the command line
    title, filename = parse_command_line()

    # Load the mindmap from the specified file
    mindmap = load_mindmap(filename)

    # Create the mindmap from the specified data
    create_mindmap(title, mindmap, filename + ".png")


main()