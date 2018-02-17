# 1074 Reversing Linked List
# One of check points is out of time

from collections import deque


if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    f_addr = int(s[0])
    N = int(s[1])
    K = int(s[2])
    l = deque()
    for i in range(N):
        s = input()
        s = s.split(' ')
        l.append((int(s[0]), int(s[1]), int(s[2])))
    r = []
    Q = [x for x in l if x[0] == f_addr][0]
    r.append(Q)
    while Q[2] != -1:
        for i in l:
            if i[0] == Q[2]:
                r.append(i)
                Q = i
    # reversing
    for u in range(int(len(r) / K)):  # 1 2 3
        c = 0
        for i in range(u * K, int(u * K + (K / 2))):  # uK -> uK+(K/2)
            c += 1
            t = r[i]
            r[i] = r[u * K + K - c]
            r[u * K + K - c] = t

    for i in range(len(r) - 1):
        print("{0:0>5} {1} {2:0>5}".format(r[i][0], r[i][1], r[i+1][0]))
    print("{0:0>5} {1} -1".format(r[-1][0], r[-1][1]))
    
