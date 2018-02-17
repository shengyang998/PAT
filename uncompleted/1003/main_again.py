# dij to find the shortest path
#


def get_min_key_of(dist):
    """dist should be a dict"""
    return min(dist, key=dist.get)


def get_result(graph, source, target, cost):
    """
    return: dist, route, max_cost
    """
    dist, prev, min_dist_cnt, max_cost = dij(graph, source, cost)
    route = get_route(prev, source, target)
    return dist, route, min_dist_cnt, max_cost


def get_route(prev, source, target):
    """
    prev should be a dict with values of list
    source and target should be the same type as the key of prev
    """
    res = []
    # need a dfs to search it, or you can only find one route
#    while prev[target][0]:
#        res.append(prev[target][0])
#        target = prev[target][0]
    return res


def dij(graph, source, cost):
    """
    graph should be a dict
    source and should be the same type as the key of graph
    cost should be a dict that consist the cost of each vertex in the graph
    return: dist, prev, min_dist_cnt, max_cost
    """
    INF = float('inf')
    UNDEF = 'undef'
    # init
    prev = {}
    max_cost = {}
    dist = {}
    min_dist_cnt = {}
    for i in graph:
        prev[i] = []
        dist[i] = INF
        max_cost[i] = 0
        min_dist_cnt[i] = 0
        for j in graph[i]:
            prev[j] = []
            dist[j] = INF
            max_cost[j] = 0
            min_dist_cnt[i] = 0
    # init completed
    dist[source] = 0
    min_dist_cnt[source] = 1
    max_cost[source] = cost[source]
    q = dist.copy() # remember to update the dictionary q when a shorter dist is found
#   while q:
#       u = get_min_key_of(q)
#       q.pop(u)
#       for v in graph.get(u, 'Z'):
#           if v == 'Z':
#               break
    for u in graph:
        for v in graph[u]:
            t = dist[u] + graph[u][v]
            # MARK: !!! core !!!
            if (t < dist[v]):
                # 下面的逻辑应该没有漏洞，但是先按照如下方法更新： min_dist_cnt： `min_dist_cnt[v] += min_dist_cnt[u]` 另外，所有 min_dist_cnt 应该初始化为0，但是源点为1
#                if t == dist[v]: # 如果路径的距离相同，+1
#                    min_dist_cnt[v] += 1
#                else: # 如果路径的距离不同，重置
#                    min_dist_cnt[v] = 1
                min_dist_cnt[v] = min_dist_cnt[u]
                prev[v] = []
                dist[v] = t
                max_cost[v] = max_cost[u] + cost[v]
                # print("max_cost[{0}] = max_cost[{1}] + cost[{0}]".format(v, u))
                # print("max_cost[{0}] = {1}".format(v, max_cost[v]))
                # print("max_cost[{0}] = {1}".format(u, max_cost[u]))
                # print("cost[{0}] = {1}".format(v, cost[v]))
            elif (t == dist[v] and max_cost[v] < max_cost[u] + cost[v]):
                min_dist_cnt[v] += min_dist_cnt[u]
                prev[v].append(u)
                max_cost[v] = max_cost[u] + cost[v]
    return dist, prev, min_dist_cnt, max_cost


if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    n_city = int(s[0])
    n_road = int(s[1])
    source = s[2]
    target = s[3]
    n_rescue_team = input()
    t = [int(x) for x in n_rescue_team.split(' ')]
    cost = dict(zip([str(x) for x in range(len(t))], t))
    t_graph = {}
    for i in range(n_road):
        s = input()
        s = s.split(' ')
        s[2] = int(s[2])
        if s[0] in t_graph and t_graph[s[0]] is not None:
            t_graph[s[0]].update({s[1]: s[2]})
        else:
            t_graph[s[0]] = {s[1]: s[2]}
    graph = t_graph.copy()
    for i in t_graph:
        for j in t_graph[i]:
            if j not in t_graph.keys():
                graph[j] = {}
    dist, route, min_dist_cnt, max_cost = get_result(graph, source, target, cost)
    print("{0} {1}".format(min_dist_cnt[target], max_cost[target]))
    # print("min_dist_cnt:{0}  max_cost:{1}\nAND it's route: {2}".format(min_dist_cnt[target], max_cost, route))
    # print("max_cost: {0}\ncost: {1}".format(max_cost, cost))

