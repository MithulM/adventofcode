t = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    t += arr[-1]
    arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    while any(i for i in arr):
        t += arr[-1]
        arr = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
print(t)