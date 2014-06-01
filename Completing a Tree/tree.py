'''
Problem
Figure 2. A labeled tree with 6 vertices and 5 edges.
An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.

We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

Sample Dataset
10
1 2
2 8
4 10
5 9
6 10
7 9

Sample Output
3
'''

def dfs(u):
    w.add(u)
    for v in range( len(a[u]) ):
        if a[u][v] not in w:
            dfs( a[u][v] )

f = open('in.txt', 'r')
n = int(f.readline())
a = []
for i in range(n + 1):
    a.append( [] )
for line in f:
    t = [int(x) for x in line.split()]
    a[ t[0] ].append( t[1] )
    a[ t[1] ].append( t[0] )
w = set()
dfs(1)
res = 0
for i in range(1, n + 1):
    if i not in w:
        dfs(i)
        res += 1 
print res
