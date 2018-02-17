# Emergency
# You are required to print the shortest path and if it is not unique, you should print the path which you can gather as much as possible rescue team.
# Ysy 2017-08-24
from collections import deque


def get_route(graph, source, target, n_rescue_team):
    undef = "undef"
    route = deque()
    dist, prev, cost, dist_cnt = dij(graph, source, n_rescue_team)
    route.appendleft(target)
    while target is not None and prev[target] != undef:
        route.appendleft(prev[target])
        target = prev[target]
    return dist, route, cost, dist_cnt


def dij(graph, source, team):
    undef = "undef"
    Inf = float('inf')
    dist = {}
    dist_cnt = {}
    prev = {}
    Q_list = {}
    cost = {} # the min total cost from source to current vertex
    for i in graph:
        Q_list[i] = Inf
        dist[i] = Inf
        dist_cnt[i] = 1
        prev[i] = undef
        cost[i] = 0
        for v in graph[i]:
            dist[v] = Inf
            dist_cnt[v] = 1
            prev[v] = undef
            cost[v] = 0
    dist[source] = 0
    cost[source] = team[source]
    while Q_list:
        u = min(Q_list)
        Q_list.pop(u)
        for v in graph[u]:
            t = dist[u] + graph[u][v]
            if t <= dist[v]:                # you can modify here for your special problem
                if t == dist[v]:            # FIXED: if equals to now
                    dist_cnt[v] += 1
                    cost_t = cost[u] + team[v]
                    if cost_t > cost[v]:
                        cost[v] = cost_t
                else:                       # if shorter than now
                    dist_cnt[v] = 1
                dist[v] = t
                prev[v] = u
    return dist, prev, cost, dist_cnt       # return the min cost and min dist count for each vertex


if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    n_city = int(s[0])
    n_road = int(s[1])
    c_city = s[2]
    t_city = s[3]
    n_rescue_team = input()
    t = [int(x) for x in n_rescue_team.split(' ')]
    t_keys = [str(x) for x in range(len(t))]
    n_rescue_team = dict(zip(t_keys, t))
    # print("team: ", n_rescue_team)
    graph = {}
    for i in range(n_road):
        s = input()
        s = s.split(' ')
        s[2] = int(s[2])
        if s[0] in graph and graph[s[0]] is not None:
            graph[s[0]].update({s[1]: s[2]})
        else:
            graph[s[0]] = {s[1]: s[2]}
    dist, route, cost, dist_cnt = get_route(graph, c_city, t_city, n_rescue_team)
    print("route:{0}\ndist: {1}\ncost[target]: {2}\nmin_dist_cnt[target]: {3}".format(route, dist, cost[t_city], dist_cnt[t_city]))
    # print("{0} {1}".format(dist_cnt[t_city], cost[t_city]))

# 5 6 0 2
# 1 2 1 5 3
# 0 1 1
# 0 2 2
# 0 3 1
# 1 2 1
# 2 4 1
# 3 4 1
