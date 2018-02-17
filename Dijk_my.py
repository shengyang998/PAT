from collections import deque

def get_result(graph, source, target):
    undef = u"undef"
    dist, prev = dij(graph, source)
    prev_deque = deque(target)
    while prev[target] != undef:
        prev_deque.appendleft(prev[target])
        target = prev[target]
    return dist[target], prev_deque

def dij(graph, source):
    """Dijkstra"""
    Inf = 2**32
    undef = u"undef"
    dist = {}
    prev = {}
    Q_list = {}

    for v in graph:
        dist[v] = Inf
        prev[v] = undef
        Q_list[v] = Inf
    dist[source] = 0

    while Q_list:
        u = min(dist[])
        u = min(Q_list)                         # problem here: should choose the u that has the min dist[u]
        Q_list.pop(u)
        for v in graph[u]:
            new_dist = dist[u] + graph[u][v]    # If the prev should not be saved, you can change it to: new_dist = max(new_dist, dist[u]+graph[u][v])
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
    return dist, prev

if __name__ == "__main__":
