# 有向权重图 Dijkstra 算法 Python 实现
# Dijkstra 算法是单源到所有节点的最短路径算法。
# 该算法从一个节点遍历所有节点，计算所有节点的最短路径，保存在 prev 列表中，需要时倒序取出。
#   另外一种合适的思路可能应该是使用回溯法，建立解空间树，如果剪枝函数设定得好，应该能做到比 Dijkstra 算法更快。
#   感觉很难剪枝，如果不能剪枝的话，时间复杂度将会变成 O(n^2)
#   1. 判断连通性，需要……
#   错了！DFS 不适合找最短路径，虽然未证明，但是下面的代码却显示了 DFS 找最短路径的缺陷
#   1. 因为语言限制不能使用迭代器访问
#   2. 不能使用优化的栈
#   看起来 BFS 可以搜索最短路径，虽然需要耗费很大的内存空间。BFS 的实现待续……
# by Ysy at 2017.09.02 23:05

from collections import deque

def dij(graph, source, target):
    d, prev = get_d_prev(graph, source)
    print("dist[]: {0} \nprev[]: {1}".format(d, prev))
    return d[target], get_result(target, prev)


def get_result(target, prev):
    S = deque()
    # print("prev[A]: {0}".format(prev['A']))
    S.appendleft(target)
    while prev.get(target) != None:
        # print("prev[{0}]: {1}".format(target, prev[target]))
        S.appendleft(prev[target])
        target = prev[target]
    return S


def get_d_prev(graph, source):
    Inf = pow(2, 32)
    undef = u"undef"
    dist = {}
    prev = {}
    Q_list = {}
    for i in graph:
        Q_list[i] = Inf     # 所有节点（Inf 是未访问节点）
        dist[i] = Inf       # v 节点到起点的距离
        prev[i] = undef     # v 节点的前接节点
        for v in graph[i]:         # 初始化
            dist[v] = Inf       # v 节点到起点的距离
            prev[v] = undef     # v 节点的前接节点
    dist[source] = 0        # 初始节点置零
    while Q_list:
        u = min(dist, key=dist.get)
        Q_list.pop(u)       # get min of Q 访问一个未访问的节点
        for v in graph[u]:  # get u neighbor
            new_dist = dist[u] + graph[u][v]    # t是 当前节点的dist + 当前节点和临接节点的权重
            # new_dist = dist[u] + 1            # t是 当前节点的dist + 当前节点和临接节点的权重 此处假设权重是一
            if new_dist < dist[v]:              # 如果 当前节点的dist + 当前节点和临接节点的权重 < 临接节点的dist：
                dist[v] = new_dist              # 将 当前节点的dist + 当前节点和临接节点的权重 赋值给临接节点的dist
                prev[v] = u                     # 将 当前节点 赋值给临接节点的prev[]
    return dist, prev


if __name__ == "__main__":
    # 图结构：{节点A：{节点B：节点 A 到 B 的权重}}
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'C': 4},
        'C': {'D': 2, 'E': 3},
        'D': {'F': 1},
        'E': {'F': 2}
    }
    dist, route = dij(graph, 'A', 'F')
    print("The distance from {0} to {1} is {2}\nThe route is: {3}".format('A', 'F', dist, route))
    # print(shortest_backtrack(graph, 'A', 'F'))
    # print(dfs(graph, 'A', 'F'))


# # 下面的函数，因为 Python 的 for in 迭代器特性，不能成功执行
# def shortest_backtrack(graph, source, target):
#     t_list = deque()
#     dist = 0
#     Inf = pow(2, 32)
#     shortest_dist = Inf
#     shortest_list = deque()
#     t_list.append(source)
#     u = source
#     Q = deque()
#     Q.extend(graph[u])
#     while Q:  # u -> i
#         i = Q.pop()
#         t_list.append(i)
#         Q.extend(graph[i])
#         dist += graph[u][i]
#         print('u: {0}, i: {1}'.format(u, i))
#         u = i
#         if i == target:
#             if dist < shortest_dist:
#             shortest_dist = dist
#             shortest_list = t_list
#             dist -= # 此时需要返回到 Q.pop() 那一层，距离怎么计算？最好能分别记录每个节点的 dist，但是若如此，此算法与 Dijkstra 算法将没有区别

#     return shortest_list


# # dfs 不适合找最短路径🙂 by Ysy at 2017.09.03 02:18:31
# def dfs(graph, source, target):
#     dist = 0
#     max_dist = 0

#     res_dist = 0
#     res_S = deque()

#     for i in graph:
#         for j in graph[i]:
#             max_dist += graph[i][j]

#     for the_dist in range(max_dist):
#         S = deque()       # 已访问节点
#         Q = list()      # 将访问节点
#         u = source
#         Q.append(u)
#         dist = 0
#         while Q and dist <= the_dist:
#             last = u
#             u = Q.pop()
#             if u in S:
#                 continue
#             if u == target:
#                 break
#             else:
#                 S.append(u)
#                 if last != u:
#                     dist += graph[last][u]
#                 Q.extend(graph[u])
#         if dist < res_dist and u == target:
#             res_dist = dist
#             res_S = S
#     return res_S
