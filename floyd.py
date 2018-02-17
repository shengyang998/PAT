# dij to find the shortest path
#


def dij(graph, source, target, cost):
    INF = float('inf')
    UNDEF = 'undef'
    # init
    prev = {}
    max_cost = {}
    dist = {}
    q = {}
    for i in graph:
        prev[i] = UNDEF
        dist[i] = INF
        max_cost[i] = 0
        for j in graph[i]:
            prev[j] = UNDEF
            dist[j] = INF
            max_cost[j] = 0

    q = 





if __name__ == "__main__":
    # s = input()
    # s = s.split(' ')
    graph = {
        '0': {'1': 1, '2': 2, '3': 1},
        '1': {'2': 1},
        '2': {'4': 1},
        '3': {'4': 1}
    }
    cost = {
        '0': 1,
        '1': 2,
        '2': 1,
        '3': 5,
        '4': 3
    }

