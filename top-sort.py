import graphs

def _dfs(vrtx, visited, visitedNodes, g):
    visited.add(vrtx)
    edges_out = g.graph[vrtx]
    for edgs in edges_out:
        if edgs not in visited:
            _dfs(edgs, visited, visitedNodes, g)
    visitedNodes.append(vrtx)

def top_sort(g):
    visited = set()
    n = len(g.vertices)
    stack = []
    for vrtx in g.vertices:
        if vrtx not in visited:
            visitedNodes = []
            _dfs(vrtx, visited, visitedNodes, g)
            for node in visitedNodes:
                stack.append(node)
    return stack[::-1]

if __name__ == '__main__':
    g = graphs.graph()
    g.addedge(30, 40)
    g.addedge(10,20)
    g.addedge(10, 30)
    g.addedge(20,40)
    g.addedge(40, 50)
    g.addedge(20, 50)
    g.addedge(10,50)
    #print(g.vertices)
    print(top_sort(g))
