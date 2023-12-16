def getIdx(word):
    t = 0
    for c in word:
        t += ord(c)
        t *= 17
        t %= 256
    return t
mapping = {}
box = [[] for _ in range(256)]
for word in input().split(","):
    if word[-1] == "-":
        idx = getIdx(word[:-1])
        box[idx] = [(l, v) for (l, v) in box[idx] if l != word[:-1]]
    else:
        label, value = word.split("=")
        value = int(value)
        idx = getIdx(label)
        mapping[word[:-1]] = value
        new = True
        for i, (l, v) in enumerate(box[idx]):
            if l == label:
                box[idx][i] = (label, value)
                new = False
                break
        if new:
            box[idx].append((label, value))
t = 0
for i, items in enumerate(box, 1):
    for j, (label, value) in enumerate(items, 1):
        x = i * j * value
        t += x
print(t)