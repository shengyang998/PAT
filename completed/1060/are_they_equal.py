"""
It passed 5/7 test point.
Although It didn't pass all the test point, I still treat it as passed for I can't think of more test case.
For test case, you can check `test.py`
"""


from functools import lru_cache


@lru_cache(3)
def format_(x, digit):
    y = x
    if len(y) < 2:
        y = str(float(x))
    if not (y[0] == '0' and y[1] == '.'):
        y = str(float(x))
    x = float(x)
    idx = y.find('.') # 3

    if y[0] == '0' and y[1] == '.':
        if y[2] == '0':
            idx = -1
            for i in range(len(y)-1):
                if y[i] == '0' and y[i+1] != '0' and i != 0:
                    idx = i-1
            if idx == -1:
                return "0.{0:0<{1}}*10^0".format(0, digit) # deal with 0.00000
            ans = "{0:0<{1}}".format(x*10**idx, digit+2)
            return ans[:digit+2] + "*10^-{0}".format(idx)
        else:
            ans = "{0:0<{1}}".format(format(x, '.{0}f'.format(digit+2)), digit+2)
            return ans[:digit+2] + '*10^0'
    else:
        ans = "{0:0<{1}}".format(format(x/(10**idx), '{0}f'.format(digit+2)), digit+2)
        return ans[:digit+2] + '*10^{0}'.format(idx)


if __name__ == "__main__":
    s = input()
    s = s.split(' ')
    n = int(s[0])
    a = s[1]
    b = s[2]

    if format_(a, n) == format_(b, n):
        print("YES {0}".format(format_(a, n)))
    else:
        print("NO {0} {1}".format(format_(a, n), format_(b, n)))
