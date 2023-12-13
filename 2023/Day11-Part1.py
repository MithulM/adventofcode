grid = open(0).read().strip().splitlines()
n, m = len(grid), len(grid[0])
rowEmpty = [1] * (m + 1)
colEmpty = [1] * (n + 1)
galaxies = []
for i, r in enumerate(grid):
    for j, c in enumerate(r):
        if c == "#":
            galaxies.append((i, j))
            colEmpty[i + 1] = 0
            rowEmpty[j + 1] = 0
for i in range(n):
    colEmpty[i + 1] += colEmpty[i]
for j in range(m):
    rowEmpty[j + 1] += rowEmpty[j]
t = 0
size = 2
for i, (x1, y1) in enumerate(galaxies):
    for j, (x2, y2) in enumerate(galaxies[i + 1:], i + 1):
        t += abs(x1 - x2) + abs(y1 - y2) + (size - 1) * (abs(colEmpty[x1] - colEmpty[x2]) + abs(rowEmpty[y1] - rowEmpty[y2]))
print(t)