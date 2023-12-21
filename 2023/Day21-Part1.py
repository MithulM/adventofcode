from collections import deque
garden = list(map(list, open(0).read().strip().splitlines()))
n, m = len(garden), len(garden[0])
ai, aj = (-1, -1)
for i, r in enumerate(garden):
    for j, c in enumerate(r):
        if c == "S":
            ai, aj = i, j
            break
    else:
        continue
    break
steps = 64
t = 0
start = deque([(ai, aj, 0, 0, steps)])
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
if not (steps % 2):
    garden[ai][aj] = "O"
    t += 1
while start:
    bi, bj, di, dj, step = start.popleft()
    for dx, dy in dirs:
        if (dx, dy) != (di, dj):
            ci, cj = bi + dx, bj + dy
            if 0 <= ci < n and 0 <= cj < m and garden[ci][cj] == "." and step > 0:
                if step & 1:
                    garden[ci][cj] = "O"
                    t += 1
                start.append((ci, cj, -dx, -dy, step - 1))
    # for r in garden:print(*r, sep="")
    # print()
for r in garden:print(*r, sep="")
print(t)
