# Graph Traversal Technique
# Depth First Search - DFS
# Applied on Undirected Graph

class Graph:
    def __init__(self, nodes_list):
        self.vertices = nodes_list  # total vertices
        self.adj_list = {}  # initially empty Dictionary - contains entire graph
        self.visited = False
        self.is_directed = False

        # loop through all the vertices, and add empty list to each vertex
        for i in self.vertices:
            self.adj_list[i] = []  # adj_list["A"] = []

    def add_edge(self, u, v):
        # undirected - add twice
        self.adj_list[u].append(v)  # vertex u - add v
        self.adj_list[v].append(u)  # vertex v - add u

    def print_graph(self):
        # loop over all the vertices, and print adjacent nodes
        for vertex in self.vertices:
            print(vertex, "->", self.adj_list[vertex])

    def DFS_Traversal(self, v, visited):
        # Mark the current node as visited and print it
        visited.append(v)
        print(v, end=" ")

        # Recur for all the vertices, adjacent to this vertex
        for neighbour in self.adj_list[v]:
            if neighbour not in visited:
                self.DFS_Traversal(neighbour, visited)

    def DFS(self, s_vertex):
        size_of_graph = len(self.adj_list)
        # Create a list to store visited vertices
        visited = [] * size_of_graph

        # Call the recursive helper function to print DFS traversal
        self.DFS_Traversal(s_vertex, visited)


def main():
    nodes = ["1", "2", "3", "4", "5", "6", "7"]  # create a list of nodes
    my_graph = Graph(nodes)

    all_edges = [
        ("1", "2"), ("1", "3"), ("2", "4"), ("2", "5"), ("3", "6"), ("3", "7")
    ]

    # access tuple using u,v inside all_edges list
    for u, v in all_edges:
        my_graph.add_edge(u, v)

    my_graph.print_graph()
    print()

    start_vertex = "1"  # take care if graph node is str/int
    my_graph.DFS(start_vertex)
    print()


if __name__ == '__main__':
    main()
