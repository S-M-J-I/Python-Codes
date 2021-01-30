# Binary Tree Linked implementation - Balanced Tree
# for string


from collections import deque  # Using a Queue
from BinaryTreePrinter import BinaryTreePrinter  # Just for printing a Binary Tree


class TreeNode:
    # Tree node containing left and right child
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:

    def __init__(self):
        self.root = None  # initially root is None
        self.number_of_nodes = 0

    def insert(self, val):
        if self.root is None:
            # if root is empty, add new node to root
            self.root = TreeNode(val)
            self.number_of_nodes += 1
        else:
            # root node is present
            # We will use a Queue here to form the binary tree - as a BFS (breath first search)
            nodes = deque()
            nodes.appendleft(self.root)  # first - enqueue root to queue

            while True:
                checking_node = nodes.pop()  # dequeue a node from queue
                # check if left or right side is empty
                # if any side empty - add node to that side, then exit function
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    self.number_of_nodes += 1
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    self.number_of_nodes += 1
                    return
                else:
                    # if not empty - then we have 2 child nodes
                    # Add the remaining nodes to queue - to be added later to Tree
                    nodes.appendleft(checking_node.left)
                    nodes.appendleft(checking_node.right)

                    # keep iterating, until the nodes are added to either side

    # ---------------------- TREE TRAVERSAL TECHNIQUES --------------------

    def traverse_tree(self):
        # ----- Helper Function ----
        if self.root is None:
            return
        else:
            # we can input choice here to choose traversal techniques
            print("InOrder = ", end=" ")
            self.InOrder(self.root)
            print()
            print("PreOrder = ", end=" ")
            self.PreOrder(self.root)
            print()
            print("PostOrder = ", end=" ")
            self.PostOrder(self.root)
            print()

    def InOrder(self, root_node):
        # visit left sub-tree
        if root_node.left:
            self.InOrder(root_node.left)

        # visit root (base) node
        print(root_node.val, end=" ")

        # visit right sub-tree
        if root_node.right:
            self.InOrder(root_node.right)

    def PreOrder(self, root_node):
        # visit root (base) node
        print(root_node.val, end=" ")

        # visit left sub-tree
        if root_node.left:
            self.PreOrder(root_node.left)

        # visit right sub-tree
        if root_node.right:
            self.PreOrder(root_node.right)

    def PostOrder(self, root_node):
        # visit left sub-tree
        if root_node.left:
            self.PostOrder(root_node.left)

        # visit right sub-tree
        if root_node.right:
            self.PostOrder(root_node.right)

        # visit root (base) node
        print(root_node.val, end=" ")

    # ------------------------ Height of tree --------------------

    def __maxDepth(self, x, y):
        # return the maximum of the height of the left and right sub-trees,
        if x > y:
            return x
        else:
            return y

    def height_of_tree(self, node):
        if node.left is None and node.right is None:
            # if there is no node
            return 0
        else:
            # The height of a sub-tree is found by recursively calling the function,
            # and passing the child node as the parameter.
            return self.__maxDepth(self.height_of_tree(node.left), self.height_of_tree(node.right)) + 1
            # plus 1 to account for the current node.

    def height(self):
        if self.root is None:
            return None
        else:
            return self.height_of_tree(self.root)

    # -------------------------------------------------------------

    def tree_node_number(self):
        return self.number_of_nodes

    def __str__(self):
        # String representation of Tree
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)  # string returned


def main():
    my_tree = BinaryTree()
    input_tree = ["A", "B", "C", "D", "E", "F", "G"]
    for char in input_tree:
        my_tree.insert(char)
        # print(my_tree)
    print(my_tree)
    my_tree.traverse_tree()
    print(f"Number of Nodes in Tree = {my_tree.tree_node_number()}")
    print()
    print(f"Height of Tree = {my_tree.height()}")


if __name__ == '__main__':
    # if file is main file, then call main function
    main()
