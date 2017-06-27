class TreeNode:
    def __init__(self, data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        #return "data {} --> [left : {} --- right : {}]".format(self.data,self.left,self.right)
        return "data {}".format(self.data)




def levelOrderPrint(root):
    results = []
    level = 0
    list = [root]
    results=list
    while True:
        list = []
        print(str(level) + ":" + str(results))
        for node in results:
            if node.left is not None:
                list.append(node.left)
            if node.right is not None:
                list.append(node.right)

        if len(list)==0:
            break
        else:
            results=list
        level += 1


if __name__ == '__main__':
    n1 = TreeNode('x')
    n2 = TreeNode('y')
    n3 = TreeNode('z')
    n4 = TreeNode('a')
    n5 = TreeNode('b')
    n6 = TreeNode('c')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    print(n1)
    levelOrderPrint(n1)


