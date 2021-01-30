# Adjacency List Representation - Undirected Graph
# using dictionary and list (linked list)

import math


class Graph:
    def __init__(self, nodes_list):
        self.vertices = nodes_list  # total vertices
        self.adj_list = {}  # initially empty Dictionary - contains entire graph

        # loop through all the vertices, and add empty list to each vertex
        for i in self.vertices:
            self.adj_list[i] = []  # adj_list["A"] = []

    def add_edge(self, u, v):
        # undirected - add twice
        self.adj_list[u].append(v)  # vertex u - add v
        self.adj_list[v].append(u)  # vertex v - add u

    def find_degree(self, node):
        # find how many adjacent nodes are there in adj list of given node
        if node not in self.vertices:
            return None
        degree = len(self.adj_list[node])
        return degree

    def max_and_min_degree(self):
        # average_degree = (2*E) / V
        average_degree = (2 * self.total_edge()) / len(self.vertices)
        max_dg = math.ceil(average_degree)
        min_dg = math.floor(average_degree)
        print(f"Max degree = {max_dg}")
        print(f"Min degree = {min_dg}")

    def total_degree(self):
        degree = 0
        for i in self.adj_list:
            degree += len(self.adj_list[i])
        return degree

    def total_edge(self):
        # Total degree = 2 x Total edge
        edge = self.total_degree() // 2
        return edge

    def print_graph(self):
        # loop over all the vertices, and print adjacent nodes
        for vertex in self.vertices:
            print(vertex, "->", self.adj_list[vertex])


def main():
    nodes = ["A", "B", "C", "D", "E"]  # create a list of nodes
    my_graph = Graph(nodes)
    # my_graph.add_edge("A", "B")

    # add the edges (together - shortcut) - tuple within list
    all_edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")
    ]

    # access tuple using u,v inside all_edges list
    for u, v in all_edges:
        my_graph.add_edge(u, v)

    my_graph.print_graph()
    print()

    vertex = "C"
    print(f"Degree of {vertex} = {my_graph.find_degree(vertex)}")
    print(f"Total Degree of Graph = {my_graph.total_degree()}")
    print(f"Total Edge of Graph = {my_graph.total_edge()}")
    my_graph.max_and_min_degree()


if __name__ == '__main__':
    main()

# implement - Detect cycle in an undirected graph
