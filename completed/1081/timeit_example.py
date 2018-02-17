### timeit repeat() 示例
### 2017.07.23 by Ysy

import timeit as timeit

def fun():
    s = 0
    for i in range(1000):
        s += i

t2 = timeit.repeat('fun()', 'from __main__ import fun', repeat=5, number=10000)
print("max time: ", max(t2), " min time: ", min(t2), " subtraction: ", max(t2)-min(t2))
