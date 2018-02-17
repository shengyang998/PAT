# A+B Format
# Ysy 2017-08-04

if __name__ == '__main__':
    t = input()
    a, b = t.split(' ')
    a = int(a)
    b = int(b)
    c = a + b
    res = []
    if c < 0:
        res.append('-')
        c = -c
    c = str(c)
    count = 1
    
    for i in c:
        res.append(i)
        if ((len(c) - count ) % 3 == 0) and (count != len(c)):
            res.append(',')
        count += 1

    for i in res:
        print(i, end='')
    print()
