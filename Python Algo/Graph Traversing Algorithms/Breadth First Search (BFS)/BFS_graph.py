# Graph Traversal Technique
# Breadth First Search - BFS
# Applied on Undirected Graph

from collections import deque


class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        # add item to left side of queue (first in)
        self.container.appendleft(item)

    def deque(self):
        # remove item from right of queue (first out)
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        else:
            return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0  # checks if queue has items

    def get_length(self):
        return len(self.container)

    def front_element(self):
        # return element at front side (right side) of queue
        return self.container[-1]


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

    def BFS(self, s_vertex):
        size_of_graph = len(self.adj_list)
        visited = [] * size_of_graph # Mark all the vertices as not visited

        queue = Queue() # Create a queue for BFS
        # Mark the source node as visited and enqueue it
        queue.enqueue(s_vertex)
        visited.append(s_vertex)

        print("BFS = ", end=" ")

        while not queue.is_empty():
            # Dequeue a vertex from queue and print it
            s_vertex = queue.deque()
            print(s_vertex, end=" ")

            # Get all adjacent vertices of the dequeued vertex s.
            # If a adjacent vertex has not been visited, then mark it visited and enqueue it
            for v in self.adj_list[s_vertex]:
                if v not in visited:
                    queue.enqueue(v)
                    visited.append(v)


def main():
    nodes = ["0", "1", "2", "3", "4", "5", "6"]  # create a list of nodes
    my_graph = Graph(nodes)

    all_edges = [
        ("0", "1"), ("0", "2"), ("1", "3"), ("1", "4"), ("2", "5"), ("2", "6")
    ]

    # access tuple using u,v inside all_edges list
    for u, v in all_edges:
        my_graph.add_edge(u, v)

    my_graph.print_graph()
    print()

    start_vertex = "0" # take care if graph node is str/int
    my_graph.BFS(start_vertex)
    print()


if __name__ == '__main__':
    main()
