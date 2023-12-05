board = ["." + input() + "." for i in range(int(input()))]
m = len(board[0])
board = ["." * m] + board + ["." * m]
checkNum = {}
for i, r in enumerate(board[1:-1], 1):
    for j, c in enumerate(r[1:-1], 1):
        if c.isdigit() and not board[i][j - 1].isdigit():
            num = ""
            currX, currY = i, j
            while board[currX][currY].isdigit():
                num += board[currX][currY]
                currY += 1
            checkNum[(i, j, len(num))] = int(num)

def hasSym(cell):
    return not cell.isdigit() and cell != "."

t = 0
for (i, j, l), k in checkNum.items():
    add = hasSym(board[i][j - 1]) or hasSym(board[i][j + l])
    for r in range(l + 2):
        if hasSym(board[i - 1][j + r - 1]) or hasSym(board[i + 1][j + r - 1]):
            add = True
            break
    if add:
        t += k
print(t)