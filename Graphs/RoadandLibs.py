from queue import Queue
from collections import defaultdict


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return c_lib*n
    else:
        tempd = defaultdict(list)
        for road in cities:
            tempd[road[0]].append(road[1])
            tempd[road[1]].append(road[0])

        look = [False]*n
        q = Queue()
        tot = 0
        for i in range(n):
            if look[i]:
                continue
            q.put(i+1)
            look[i] = True
            tot += c_lib
            while not q.empty():
                k = q.get()
                tot += c_road
                for d in tempd[k]:
                    if not look[d-1]:
                        q.put(d)
                        look[d-1] = True
            tot -= c_road
        return tot


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
