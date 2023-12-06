import re

file_path = 'read.txt'
with open(file_path, 'r') as file:
    digitListPattern = r"((?:\d+ ?\n?)+)"
    wordPattern = r"[a-zA-Z]+"
    mapPattern = rf"(?:({wordPattern})-to-({wordPattern}) +map:\n{digitListPattern}\n?)*"
    inputPattern = rf"^seeds:\s*{digitListPattern}\n+({mapPattern})$"
    match = re.match(inputPattern, file.read())
    res = float('inf')
    if not match:
        print("Error Parsing 1")
    startSeeds = [int(i) for i in re.split(r"\s+", match.group(1)) if i != ""]
    seen = 0
    for i in range(len(startSeeds) // 2):
        for seed in range(startSeeds[2 * i], startSeeds[2 * i] + startSeeds[2 * i + 1]):
            seen += 1
            fixed = False
            for line in match.group(2).split("\n"):
                titlePattern = rf"({wordPattern})-to-({wordPattern}) +map:"
                mapMatch = re.match(titlePattern, line)
                if mapMatch:
                    fixed = False
                else:
                    v = tuple(int(i) for i in re.split(r"\s+", line) if i != "")
                    if v:
                        dest, source, length = v
                        diff = dest - source
                        if source <= seed < (source + length):
                            if not fixed:
                                fixed = True
                                seed += diff
            res = min(res, seed)
    print(res)