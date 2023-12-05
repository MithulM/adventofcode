from itertools import product
board = ["." + input() + "." for _ in range(int(input()))]
m = len(board[0])
board = ["." * m] + board + ["." * m]
starts = [(i, j) for i, r in enumerate(board) for j, c in enumerate(r) if c == "*"]
t = 0
for startX, startY in starts:
    visited = set()
    nums = []
    for i, j in product(range(-1, 2), range(-1, 2)):
        if (i, j) != (0, 0):
            if board[startX + i][startY + j].isdigit() and (startX + i, startY + j) not in visited:
                num = ""
                tx, ty = startX + i, startY + j
                while board[tx][ty].isdigit():
                    visited.add((tx, ty))
                    num = board[tx][ty] + num
                    ty -= 1
                tx, ty = startX + i, startY + j + 1
                while board[tx][ty].isdigit():
                    visited.add((tx, ty))
                    num += board[tx][ty]
                    ty += 1
                nums.append(int(num))
    prod = 0
    if len(nums) == 2:
        prod = nums[0] * nums[1]
    t += prod
print(t)