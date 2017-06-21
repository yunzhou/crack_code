'''
4.4 Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
 (eg, if you have a tree with depth D, you’ll have D linked lists).
'''

def generate_level_list(root):
    result = []
    level = 0
    level_list = [root]
    result.append(level_list)
    while True:
        level_list = []
        for n in result[level]:
            if n.left is not None:
                level_list.append(n.left)
            if n.right is not None:
                level_list.append(n.right)
        if len(level_list) > 0:
            result.append(level_list)
        else:
            break
        level+=1
    return result

