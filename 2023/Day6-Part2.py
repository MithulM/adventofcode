import re
from math import ceil, floor

with open("read.txt", 'r') as file:
    ts, ds = file.read().replace(" ", "").split('\n')
    t = int(ts.split(":")[1])
    d = int(ds.split(":")[1])
    res = 1
    p1 = (t + (t ** 2 - 4 * d) ** .5) / 2
    p2 = (t - (t ** 2 - 4 * d) ** .5) / 2
    if p1 > t / 2:
        tmp = (2 * abs(ceil(t / 2) - ceil(p1)))
    else:
        tmp = (2 * abs(floor(t / 2) - floor(p1)))
    tmp -= (t + 1) % 2
    res *= tmp
    print(res)