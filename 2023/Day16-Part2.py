room = [list(i) for i in open(0).read().strip().splitlines()]
n, m = len(room), len(room[0])
def solve(sx, sy, dsx, dsy):
    s = {(sx, sy, dsx, dsy)}
    seen = {(sx, sy, dsx, dsy)}
    light = [(sx, sy)]
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
    return len(set(light))
h = 0
for i in range(n):
    h = max(h, solve(i, 0, 0, 1))
for i in range(n):
    h = max(h, solve(i, m - 1, 0, -1))
for i in range(m):
    h = max(h, solve(0, i, 1, 0))
for i in range(m):
    h = max(h, solve(n - 1, i, -1, 0))
print(h)
