# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

print(A)

# Convert Array of Edges -> Adjacency Matrix
M = []
for i in range(n):
    M.append([0]*n)

for u,v in A:
    M[u][v] = 1 

 #uncomment the following line if the graph is undirected 
#M[u][v] =  1 
 
print(M)

from collections import defaultdict 

D = defaultdict(list)

for u , v in A :
    D[u].append(v)
    #uncomment the following line if the graph is undirected
    #D[v].append(u)

    print(D)

    print(D[3])

# DFS with recursion - O(V+E) where V is the number of nodes and E is  the number of edges 

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

    source = 0
    seen = set()
    seen.add(source)
    dfs_recursive(source)


    source = 0 

    seen = set()
    seen.add(source)
    stack = [source]

    while stack : 
        node = stack.pop()
        print(node)
        for nei_node in D[node]:
            if nei_node not in seen:
                seen.append(nei_node)
                stack.append(nei_node)

    
    #BFS (Queue) - O(v+e)
 
    source = 0

    from collections import dequeue
    seen = set()
    seen.add(source)
    q = dequeue()
    q.append(source)

    while q :
        node = q.popleft()
        print(node)
        for nei_node in D[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)

class Node :
    def __init__(self , value ):
        self.value = value 
        self.neighbors = []

        def __str__(self):
            return f'NOde{self.value})'

    def display(self):
        connections = [node.vlaue for node in self.neighbors]
        return f'{self.value} is connected to : {connections}'
    

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(B.display()) 

