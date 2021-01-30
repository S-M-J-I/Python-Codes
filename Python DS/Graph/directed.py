# Adjacency List Representation - Directed Graph
# using dictionary and list (linked list)


class Graph:
    def __init__(self, Nodes, is_directed=False):
        # is_directed = to check if graph is directed or not
        self.vertices = Nodes  # Nodes - list of nodes
        self.adj_list = {}  # initially empty Dictionary - contains entire graph
        self.is_directed = is_directed

        # loop through all the vertices, and add empty list to each vertex
        for i in self.vertices:
            self.adj_list[i] = []  # adj_list["A"] = []

    def add_edge(self, u, v):
        # Directed - add once
        self.adj_list[u].append(v)  # vertex u - add v
        if not self.is_directed:
            self.adj_list[v].append(u)  # vertex v - add u

    def find_outDegree(self, node):
        # find out degree of a given vertex
        if node not in self.vertices:
            return None
        out_degree = len(self.adj_list[node])
        return out_degree

    def total_outDegree(self):
        out_degree = 0
        for i in self.adj_list:
            out_degree += len(self.adj_list[i])
        return out_degree

    def find_inDegree(self, node):
        if node not in self.vertices:
            return None
        in_degree = 0
        for i in self.adj_list:
            if node in self.adj_list[i]:
                in_degree += 1
        return in_degree

    def print_graph(self):
        # loop over all the vertices, and print adjacent nodes
        for vertex in self.vertices:
            print(vertex, "->", self.adj_list[vertex])


def main():
    nodes = ["A", "B", "C", "D"]  # create a list of nodes
    my_graph = Graph(nodes, is_directed=True)
    # my_graph.add_edge("A", "B")

    # add the edges (together - shortcut) - tuple within list
    all_edges = [
        ("A", "B"), ("A", "D"), ("B", "C"), ("C", "A"), ("D", "C")
    ]

    # access tuple using u,v inside all_edges list
    for u, v in all_edges:
        my_graph.add_edge(u, v)

    my_graph.print_graph()
    print()

    vertex = "C"
    print(f"Out-Degree of {vertex} = {my_graph.find_outDegree(vertex)}")
    print(f"Total Out-Degree of Graph = {my_graph.total_outDegree()}")

    vertex = "C"
    print(f"In-Degree of {vertex} = {my_graph.find_inDegree(vertex)}")


if __name__ == '__main__':
    main()
