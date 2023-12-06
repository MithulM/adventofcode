import re
from math import ceil, floor

with open("read.txt", 'r') as file:
    pattern = r"Time:\s*((?:\d+(?: ?)+)+)\nDistance:\s*((?:\d+(?: ?)+)+)"
    x = file.read()
    match = re.match(pattern, x)
    if not match:
        print("Error parsing 1")
    times = tuple(int(i) for i in re.split(r"\s+", match.group(1)) if i != "")
    dists = tuple(int(i) for i in re.split(r"\s+", match.group(2)) if i != "")
    res = 1
    for t, d in zip(times, dists):
        p1 = (t + (t ** 2 - 4 * d) ** .5) / 2
        p2 = (t - (t ** 2 - 4 * d) ** .5) / 2
        if p1 > t / 2:
            tmp = (2 * abs(ceil(t / 2) - ceil(p1)))
        else:
            tmp = (2 * abs(floor(t / 2) - floor(p1)))
        tmp -= (t + 1) % 2
        res *= tmp
    print(res)