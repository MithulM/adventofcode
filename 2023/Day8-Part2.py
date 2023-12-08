import re
from math import gcd
from functools import reduce

mapping = {}
instructions = list(map(int, input().replace("L", "0").replace("R", "1")))
starts = []
for i in range(int(input())):
    x = input()
    print(x)
    match = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", x)
    if not match:
        print("Error")
    if match.group(1)[-1] == "A":
        starts.append(match.group(1))
    mapping[match.group(1)] = (match.group(2), match.group(3))
res = []
for curr in starts:
    idx = 0
    while curr[-1] != "Z":
        curr = mapping[curr][instructions[idx % len(instructions)]]
        idx += 1
    res.append(idx)

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

print(reduce(lcm, res))