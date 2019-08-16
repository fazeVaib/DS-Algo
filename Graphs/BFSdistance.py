from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbour = defaultdict(list) 
        print("const done")

    def connect(self, x, y):
        self.neighbour[x].append(y)
        self.neighbour[y].append(x)
        print("connected", self.neighbour)

    def find_all_distances(self, start):
        q = Queue()
        visited = [False]*self.n
        distance = [0]*self.n

        q.put(start)
        visited[start] == True

        while not q.empty():
            k = q.get()
            print("Ran for ", k, "  queue: ", list(q.queue))
            print("Visited: ", visited)
            for node in self.neighbour[k]:
                if visited[node]:
                    continue
                visited[node] = True
                q.put(node)
                distance[node] = distance[k] + 6
                print("Distance: ", distance)

        for j in range(self.n):
            if j == start:
                continue
            elif not visited[j]:
                print(-1, end=' ')
            else:
                print(distance[j], end=' ')

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x-1, y-1)
        s = int(input())
        graph.find_all_distances(s-1)
