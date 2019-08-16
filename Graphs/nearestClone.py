from collections import OrderedDict
from queue import Queue

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    neighbours = OrderedDict(list)
    visited = [False]*graph_nodes
    


if __name__ == '__main__':

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(str(ans))
