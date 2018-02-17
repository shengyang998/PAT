# Polynomials plus
# Ysy 2017-08-08

def polynomials(t):
    a_dict = dict()
    count = 0
    while count != len(t):
        t[count] = t[count].split(" ")
        na = int(t[count][0])
        t[count] = t[count][1:]
        for i in range(na): 
            a1 = t[count][2 * i]
            a2 = t[count][2 * i + 1]
            if(a1 in a_dict.keys()):
                a_dict[a1] = str(float(a2) + float(a_dict[a1]))
            else:
                a_dict.update({a1: a2})
        count += 1
    b_dict = {}
    for i in a_dict:
        if float(a_dict[i]) != 0:
            b_dict.update({i: a_dict[i]})
    a_dict = b_dict
    return a_dict


def output(a_dict):
    print(len(a_dict), end='')

    a1 = [int(x) for x in a_dict.keys()]
    a1.sort(reverse=True)
    for i in a1:
        print(' ' + str(i), "%.1f" % float(a_dict[str(i)]), end='')
    print()


def test():
    output(polynomials(['2 1 2.4 0 3.2', '2 2 1.5 1 0.5']))
    output(polynomials(['2 1 2.4 0 3.2', '2 1 -2.4 0 -3.2']))


if __name__ == "__main__":
    # a_dict = polynomials([input(), input()])
    # output(a_dict)
    test()
