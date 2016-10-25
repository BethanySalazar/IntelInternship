"""
    Trees - data that's connected through branches, collection of nodes
    Branches - the connection between nodes
    Nodes - structure of data, anything
    Root - The top node in a tree
    Child - A node directly connected to another node when moving away from the Root
    Parent - The converse notion of a child
    Siblings - A group of nodes with the same parent
    Descendant - A node reachable by repeated proceeding from parent to child, only going up
    Ancestor - A node reachable by repeated proceeding from child to parent , directly related
    Leaf - A node with no children
    Internal node - A node with at least one child
    External node - A node with no children
    Degree - The number of sub trees of a node
    Edge - The connection between one node and another
    Path - A sequence of nodes and edges connecting a node with a descendant
    Level - The level of a node is defined by 1 + (the number of connections between the node and the root).
    Height of node - The height of a node is the number of edges on the longest path between that node and a leaf
    Height of tree - The height of a tree is the height of its root node
    Depth - The depth of a node is the number of edges from the node to the tree's root node
    Forest - A forest is a set of n ≥ 0 disjoint trees.


"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    # add a child
    def add(self, node):
        if(not self.lChild):
            self.lChild = node
        elif(not self.rChild):
            self.rChild = node
        else:
            print("Cannot add more than two children")

# another way to attach these nodes
rootNode = Node(0)
aNode = Node(1)
rootNode.add(aNode)
# attach these Nodes
rootNode.add(Node(2)) # made as creating nodes

print(rootNode.lChild.data) #.data prints the stuff in node
print(rootNode.rChild)
print(aNode.lChild.data)