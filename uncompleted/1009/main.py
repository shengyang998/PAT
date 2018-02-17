# 1009 Product of Polynomials (25)

def mul(lhs, rhs):
    res = {}
    for i in lhs:
        if i in rhs:
            res[i] = lhs[i] + rhs[i]
        else:
            res[i] = lhs[i]
    for i in rhs:
        if i in lhs:
            res[i] = lhs[i] + rhs[i]
        else:
            res[i] = rhs[i]
    for i in lhs.values():

    return res

if __name__ == "__main__":

    d = [{}, {}]
    for k in range(2):
        s = input()
        s = s.split(' ')
        n = int(s[0])
        s = s[1:]
        ex = [int(x) for x in s[0::2]]
        co = s[1::2]
        for i in range(n):
            coeff = co[i]
            exp = ex[i]
            if coeff in d[k].keys(): # if coeff exists
                d[k][coeff] += exp
            else:
                d[k][coeff] = exp
    res = mul(d[0], d[1])
    keys = sorted(res.keys(),key=res.get , reverse=True)
    print(len(keys), end='')
    for i in keys:
        if res[i] != 0:
            print(" {1} {0}".format(i, res[i]), end='')
    print()
