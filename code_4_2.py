'''
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''
#dfs
def dfs(g,s,e):
    stack=[]
    visited=[]
    stack.append(s)
    while(len(stack)>0):
        u = stack.pop()
        if u is not None:
            visited.append(u)
            for n in g.getAdj(u):
                if n not in visited:
                    if n==e:
                        return True
                    else:
                        visited.append(n)
                        stack.append(n)

            visited.append(u)


