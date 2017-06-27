""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    prev = None
    return isBSTUtil(root, prev)


# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, prev):
    # An empty tree is BST
    if node is None:
        return True
    else:
        if not isBSTUtil(node.left, prev):
            return False
        if (prev is not None and prev.data >= node.data):
            return False
        prev = node
        return isBSTUtil(node.right, prev)