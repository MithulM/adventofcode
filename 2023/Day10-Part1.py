layout = ["." + input() + "." for _ in range(int(input()))]
layout = ["." * len(layout[0])] + layout + ["." * len(layout[0])]
start = tuple()
for i, r in enumerate(layout):
    for j, c in enumerate(r):
        if c == "S":
            start = (i, j)
            break
    else:
        continue
    break
h = -1
s = [start]
dirs = [(0, 1, {"S":{"-", "7", "J"},
                "|":set(),
                "J":set(),
                "7":set(),
                "F":{"-", "7", "J"},
                "L":{"-", "7", "J"},
                "-":{"-", "7", "J"}}),
        (0, -1, {"S":{"L", "F", "-"},
                 "|":set(),
                 "J":{"L", "F", "-"},
                 "7":{"L", "F", "-"},
                 "F":set(),
                 "L":set(),
                 "-":{"F", "L", "-"}}),
        (1, 0, {"S":{"|", "L", "J"},
                 "|":{"|", "L", "J"},
                 "J":set(),
                 "7":{"|", "L", "J"},
                 "F":{"|", "L", "J"},
                 "L":set(),
                 "-":set()}),
        (-1, 0, {"S":{"|", "7", "F"},
                 "|":{"|", "7", "F"},
                 "J":{"|", "7", "F"},
                 "7":set(),
                 "F":set(),
                 "L":{"|", "7", "F"},
                 "-":set()})]
visited = {start}
print(s)
while s:
    tmp = []
    for i, j in s:
        for dx, dy, accept in dirs:
            nx, ny = i + dx, j + dy
            if layout[nx][ny] in accept[layout[i][j]] and (nx, ny) not in visited:
                # print((nx, ny), layout[nx][ny], (i, j), layout[i][j], accept[layout[i][j]])
                visited.add((nx, ny))
                tmp.append((nx, ny))
    print(tmp)
    s = tmp
    h += 1
print(h)