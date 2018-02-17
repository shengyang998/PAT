if __name__ == "__main__":
    s = input()
    n_city, m_road, k_p = [int(x) for x in s.split(' ')]
    roads = [-1][-1]*1000
    for _ in range(m):
        s = input()
        c1, c2 = [int(x) for x in s.split(' ')]
        roads[c1][c2] = 1
    # get del city
    s = input()
    s = [int(x) for x in s.split(' ')]
    for i in s: # each city
        roads[i]
        c = 0
        for j in range(len(t)):
            c = t[j]
