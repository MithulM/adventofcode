room = [list(i) for i in open(0).read().strip().splitlines()]
s = {(0, 0, 0, 1)}
seen = {(0, 0, 0, 1)}
light = [(0, 0)]
n, m = len(room), len(room[0])
for r in room:print(*r, sep="")
while s:
    x, y, dx, dy = s.pop()
    seen.add((x, y, dx, dy))
    if room[x][y] == "-":
        dirs = [(0, 1), (0, -1)]
    elif room[x][y] == "|":
        dirs = [(1, 0), (-1, 0)]
    elif room[x][y] == "\\":
        dirs = [(dy, dx)]
    elif room[x][y] == "/":
        dirs = [(-dy, -dx)]
    else:
        dirs = [(dx, dy)]
    for ndx, ndy in dirs:
        nx, ny = x + ndx, y + ndy
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny, ndx, ndy) not in seen:
                light.append((nx, ny))
                s.add((nx, ny, ndx, ndy))
print()
for i, j in light:
    room[i][j] = "#"
for r in room:print(*r, sep="")
print(len(set(light)))
