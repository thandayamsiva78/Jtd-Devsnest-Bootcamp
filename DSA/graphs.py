"""Graphs is a collection of nodes and edges"""
# Directd Graphs
# undirected Graphs

#------------------------------------------------------------------------->
def buildgraph(edges):
    graph = {}
    for edge in edges:
        pointA , pointB = edge
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
        
    return graph
# Hard code form 
edges = [['i' , 'j'],
         ['k' , 'i'],
         ['m' , 'k'],
         ['k' , 'l'],
         ['o' , 'n']
         ]
print(buildgraph(edges))

#-------------------------------------------------------------------------->
def buildgraph(edges):
    graph = {}
    for edge in edges:
        pointA , pointB = edge
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
        
    return graph

# user's input easy way to code form
n = 5
edges = []
for i in range(n):
    edges.append(input("Enter :").split())
# print(edges)
print(buildgraph(edges))

#------------------------------------------------------------------------->
"""DFS iterative method"""

def Dfs_iterative(graph , start):
    stack = [start]
    while stack:
        cur = stack.pop()
        print(cur)
        for val in graph[cur]:
            stack.append(val)
graph = { 10 : [20 ,30 , 40 , 50],
         20 : [],
         30 : [],
         40 : [],
         50 : [60],
         60 : [70],
         70 : []
         }
Dfs_iterative(graph , 10)
