#1051 Pop Sequence
# 

if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    m, n, k = [int(x) for x in s]
    for _ in range(k):
        s = input()
        s = s.split(' ')
        out = [int(x) for x in s]
        # MARK: CORE
        c = 0
        r = []
        for i in range(1, n+1):
            r.append(i)
            if len(r) > m:
                break
            while(r != [] and r[-1] == out[c]):
                r.pop()
                c += 1
        if c >= len(out)-1:
            print("YES")
        else:
            print("NO")


