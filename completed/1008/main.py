# 1008 Elevator

if __name__ == "__main__":
    s = input()
    s = [int(x) for x in s.split(' ')][1:]

    c = 0
    t = 0
    for i in s:
        if i > c:
            t += 6 * (i-c)
            c = i
        elif i < c:
            t += 4 * (c-i)
            c = i
    t += len(s) * 5
    print(t)

