# Binary Search Tree (BST) Linked implementation
# For numbers

from BinaryTreePrinter import BinaryTreePrinter  # Just for printing a Binary Tree
import math


class TreeNode:
    # Tree node containing left and right child
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:

    def __init__(self):
        self.root = None  # initially root is None
        self.number_of_nodes = 0

    # ----------------------- INSERT INTO BST ------------------

    def __insert_value(self, node, data):
        if data == node.val:
            # BST cannot have duplicate values
            return
        elif data < node.val:
            # add data to the left side of node - recursively

            # when we come to left
            # check if left side is empty

            # if empty - create a node and insert it
            if node.left is None:
                node.left = TreeNode(data)
                self.number_of_nodes += 1
                return

            # otherwise, enter the recursive loop
            # until u find an empty space in left/right side of node

            self.__insert_value(node.left, data)
        else:
            # add data to the right side of node - recursively

            # when we come to right
            # check if right side is empty

            # if empty - create a node and insert it
            if node.right is None:
                node.right = TreeNode(data)
                self.number_of_nodes += 1
                return

            # otherwise, enter the recursive loop
            # until u find an empty space in left/right side of node

            self.__insert_value(node.right, data)

    def insert_node(self, val):

        if self.root is None:
            self.root = TreeNode(val)
            self.number_of_nodes += 1
        else:
            # we will insert the nodes recursively
            # for that we need a helper function - __insert_node()
            # we can create functions using __
            self.__insert_value(self.root, val)

    # ------------------- MIN AND MAX NODE ------------------

    def __minNode(self, node):
        # keep traversing left
        if node.left is None:
            pass
        else:
            # there is a left child - visit that node recursively
            # we keep going until none, then return the value
            return self.__minNode(node.left)  # recursive call, as we are returning values - return
        # as we are traversing to leftmost node, we need to return that node
        # first. Only then can we return the node's value
        return node.val

    def getMinNode(self):
        # in BST, left sub tree is smaller than right sub tree

        # if we going left left left, leftmost node is minimum
        if self.root is None:
            return
        else:
            return self.__minNode(self.root)

    def __maxNode(self, node):
        # keep traversing right
        if node.right is None:
            pass
        else:
            # there is a right child - visit that node recursively
            return self.__maxNode(node.right)  # recursive call, as we are returning values - return

        return node.val

    def getMaxNode(self):
        # if we going right right right, rightmost node is maximum
        if self.root is None:
            return
        else:
            return self.__maxNode(self.root)

    # ---------------------------------------------

    # ------------------ Removing Node --------------------

    def __minNode_for_removal(self, node):
        # keep traversing left
        if node.left:
            return self.__minNode(node.left)  # recursive call, as we are returning values - return
        # Python will by default return None - if condition fails
        return node.val

    def getMinNode_for_removal(self, node):
        if node is None:
            return
        else:
            return self.__minNode_for_removal(node)

    def __remove_node(self, node, data):
        if data < node.val:
            # if value < current node - search in left sub-tree
            # check if left sub-tree is available
            if node.left is None:
                pass
            else:
                # After deletion, we get a new left sub-tree
                node.left = self.__remove_node(node.left, data)
        elif data > node.val:
            # if value > current node - search in right sub-tree
            # check if right sub-tree is available
            if node.right is None:
                pass
            else:
                # After deletion, we get a new right sub-tree
                node.right = self.__remove_node(node.right, data)
        else:
            if node.left is None and node.right is None:
                # case 1 - delete node with no child
                # we are at last node - leaf node
                print("Removing a leaf node")
                return None
            elif node.left is None:
                # case 2 - delete node with one child
                # right child is returned back to parent node, so that our current node gets deleted
                print("Removing a node with single right child")
                return node.right
            elif node.right is None:
                # case 2 - delete node with one child
                # left child is returned back to parent node, so that our current node gets deleted
                print("Removing a node with single left child")
                return node.left

            print("Removing node with two children")
            # find min value from right-sub tree
            min_val = self.getMinNode_for_removal(node.right)
            # Copy the min value
            node.val = min_val
            # Delete duplicate
            # after deletion, new right sub-tree is formed
            node.right = self.__remove_node(node.right, min_val)

        # after deleting node, return remaining nodes to the recursive loop
        # to form a new sub tree
        return node

    def remove_node(self, data):
        # Helper Function
        if self.root is None:
            return
        else:
            self.__remove_node(self.root, data)

    # -----------------------------------------------------------

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
            # print("PreOrder = ", end=" ")
            # self.PreOrder(self.root)
            # print()
            # print("PostOrder = ", end=" ")
            # self.PostOrder(self.root)
            # print()

    def InOrder(self, root_node):
        # Prints BST in sorted order

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

    # --------------------------------------------------------------------

    def __search_value(self, node, data):
        if data == node.val:
            return True
        elif data < node.val:
            # value might be in left sub-tree
            # when we come to left - check if left side is empty

            # otherwise, there is a left sub-tree
            # search for the value recursively, until u find a matching value

            if node.left:
                return self.__search_value(node.left,
                                           data)  # as we are returning values, return before recursive function
            else:
                return False
        else:
            # value might be in right sub-tree
            # when we come to right - check if right side is empty

            # otherwise, there is a right sub-tree
            # search for the value recursively, until u find a matching value

            if node.right:
                return self.__search_value(node.right, data)
            else:
                return False

    def search_node(self, val):  # O(logn)
        # Helper Method to search value
        if self.root is None:
            return
        else:
            return self.__search_value(self.root, val)

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
        # String representation of Tree (printing objects as string)
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)  # string returned


def main():
    bst_tree = BinarySearchTree()
    input_tree = [17, 4, 20, 9, 23, 18, 1, 34, 17]
    for num in input_tree:
        bst_tree.insert_node(num)
        # print(bst_tree)
    print(bst_tree)
    bst_tree.traverse_tree()
    print(f"Number of Nodes in BST = {bst_tree.tree_node_number()}")
    search_value = 100
    print(f"Does {search_value} exist? = {bst_tree.search_node(search_value)}")
    print(f"Min node = {bst_tree.getMinNode()}")
    print(f"Max node = {bst_tree.getMaxNode()}")
    delete_value = 20
    bst_tree.remove_node(delete_value)

    print(f"After deleting {delete_value}")
    print(bst_tree)
    bst_tree.traverse_tree()
    # remember height  of a tree starts from 0
    print(f"Height of Tree = {bst_tree.height()}")


if __name__ == '__main__':
    # if file is main file, then call main function
    main()

# height
