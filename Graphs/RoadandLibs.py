from queue import Queue
from collections import defaultdict


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n*c_lib
    else:
        q = Queue()
        visitedcity = [False]*n
        neighbours = defaultdict(list)
        totalCost = 0

        for road in cities:
            neighbours[road[0]].append(road[1])
            neighbours[road[1]].append(road[0])

        for i in range(n):
            if visitedcity[i]:
                continue
            visitedcity[i] == True
            q.put(i+1)
            totalCost += c_lib
            while not q.empty():
                d = q.get()
                totalCost += c_road
                for city in neighbours[d]:
                    if not visitedcity[city-1]:
                        q.put(city)
                        visitedcity[city-1]==True
        totalCost -= c_road
    return totalCost

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result))
