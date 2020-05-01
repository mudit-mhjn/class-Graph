from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)
        while queue:
            s= queue.pop(0)
            print(s, end = " ")
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for vertex in self.graph[v]:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)
    def DFS(self, s):
        visited = set()
        self.DFSUtil(s, visited)


def DFSutil(v, visited, g):
    visited.add(v)
    print(v, end = " ")
    for vertex in g.graph[v]:
        if vertex not in visited:
            DFSutil(vertex, visited, g)
def dfs(node ,g):
    visited = set()
    DFSutil(node, visited, g)

def bfs(g, node):
    visited = set()
    queue = []
    queue.append(node)
    visited.add(node)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")
        nbrs = g.graph[vertex]
        for nbr in nbrs:
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)

g = graph()
g.addedge(30, 40)
g.addedge(10,20)
g.addedge(10, 30)
g.addedge(20,40)
g.addedge(40, 50)
g.addedge(20, 50)
g.addedge(10,50)
#g.DFS(10)
#g.BFS(10)
#bfs(g, 10)
print(g.graph[10])
#   dfs(10, g)
