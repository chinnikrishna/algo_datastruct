from collections import deque

class GNode:
    def __init__(self, val):
        self.value = val
        self.connectedTo = dict()
        self.color = 0 # 0-Not visited, 1-Visiting, 2-Visited
    
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getNbrs(self):
        return [keys for keys in self.connectedTo.keys()]


class Graph:
    def __init__(self):
        self.nodeList = dict()
        self.numNodes = 0
    
    def addNode(self, val):
        n = GNode(val)
        self.nodeList[val] = n
        self.numNodes += 1
        return n
    
    def addEdge(self, frm, to, cost=0):
        if frm not in self.nodeList:
            self.addNode(frm)
        if to not in self.nodeList:
            self.addNode(to)
        self.nodeList[frm].connectedTo[self.nodeList[to]] = cost
    
    def dfs(self, strtNode, goal):
        # Add start node to stack
        nodeStack = [self.nodeList[strtNode]]
        # Iterate until the stack has nodes
        while nodeStack:
            # Get the node from stack
            node = self.nodeList[nodeStack.pop().value]
            # Mark it as visited
            node.color = 1
            # Get the node neighbors and add it to stack
            nbrs = node.getNbrs()
            for vert in nbrs:
                if vert.color == 0:
                    nodeStack.extend([vert])
            # Print the node value
            print(node.value)


    def bfs(self, strtNode):
        qu = deque()
        qu.append(self.nodeList[strtNode])

        while qu:
            # Get the node from qu
            node = self.nodeList[qu.popleft().value]
            # Mark it as visited
            node.color = 1
            # Get the neighbors of the node
            nbrs = node.getNbrs()
            for vert in nbrs:
                if vert.color == 0:
                    qu.append(vert)
            print(node.value)
    

            


g = Graph()
for i in range(6):
    g.addNode(i)
g.addEdge(0,5,1)
g.addEdge(0,1,1)   
g.addEdge(0,4,1)
g.addEdge(1,4,1)
g.addEdge(1,3,1)
g.addEdge(3,2,1)
g.addEdge(3,4,1)
g.addEdge(2,1,1) 

print(g.nodeList.keys())
print(g.nodeList[0].getNbrs())

g.bfs(0)
g.dfs(0)