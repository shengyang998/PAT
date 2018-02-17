# 1039 To Fill or not to Fill
# 存在返回非零和超时

if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    if int(s[0]) == 0:
        print(0)
        exit(0)
    s = int(s[1])
    if s == 0:
        print(0)
        exit(0)
    index = {}
    for i in range(s): # courses
        s = input()
        s = s.split(' ')
        ind = int(s[0])
        s = input()
        s = s.split(' ')
        index[ind] = s

    stu = {}
    s = input()
    s = s.split(' ')
    for i in s:
        stu[i] = [keys for keys in index if i in index[keys]]
        stu[i].sort()

    for i in s:
        print("{0} {1}".format(i, len(stu[i])), end='')
        for j in stu[i]:
            print(" {0}".format(j), end='')
        print()
