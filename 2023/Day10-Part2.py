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
h = 0
s = [start]
loop = visited = {start}
while s:
    tmp = []
    for i, j in s:
        for dx, dy, accept in dirs:
            nx, ny = i + dx, j + dy
            if layout[nx][ny] in accept[layout[i][j]] and (nx, ny) not in visited:
                visited.add((nx, ny))
                tmp.append((nx, ny))
    s = tmp
inside = False
edge = None
outside = set()
for i, r in enumerate(layout):
    for j, c in enumerate(r):
        if (i, j) in loop:
            if c == "|":
                inside = not inside
            elif c in "FL":
                edge = c == "L"
            elif c in "7J":
                if c != ("J" if edge else "7"):
                    inside = not inside
                edge = None
        else:
            h += inside
print(h)