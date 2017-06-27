'''
Write an algorithm to find the ‘next’ node (e.g., in-order successor)
of a given node in a binary search tree where each node has a link to its parent.
pg 54
SOLUTION
We approach this problem by thinking very, very carefully about what happens on an in-order traversal.
 On an in-order traversal, we visit X.left, then X, then X.right.
So, if we want to find X.successor(), we do the following:
1. If X has a right child, then the successor must be on the right side of X
(because of the order in which we visit nodes). Specifically, the left-most child must be the first node visited in that subtree.
2. Else, we go to X’s parent (call it P).
2.a. If X was a left child (P.left = X), then P is the successor of X
2.b. If X was a right child (P.right = X), then we have fully visited P, so we call successor(P).
'''

def successor(x):
    if x is None:
        return None
    if x.right is not None:
        p = get_left_most_child(x.right)
        return p
    elif x.parent is None:
        return None
    else:
        p = x.parent
        if p.left == x:
            return p
        else:
            return successor(p)


def get_left_most_child(x):
    if x is None:
        return None
    while(x.left is not None):
        x=x.left
    return x
