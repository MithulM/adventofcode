import re
ins = open(0).read()

oneline = r"(\w+)\{((?:(?:[xmas])(?:[><])(?:\d+):\w+,)+)(\w+)\}"
functionRegex = r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}"
match = re.match(rf"((?:{oneline}\n)+)\n((?:{functionRegex}\n)+)", ins)
mapping, functions = (i.split("\n")[:-1] for i in match.group(1, 5))
path = {}
for maps in mapping:
    match = re.match(oneline, maps)
    path[match.group(1)] = (match.group(2) + match.group(3)).split(",")
t = 0
for function in functions:
    match = re.match(functionRegex, function)
    x, m, a, s = map(int, match.groups())
    curr = "in"
    while curr not in "AR":
        for cond, nxt in (i.split(":") for i in path[curr][:-1]):
            exec(f"condV={cond}")
            if condV:
                curr=nxt
                break
        else:
            curr=path[curr][-1]
    if curr == "A":
        t += x + m + a + s
print(t)