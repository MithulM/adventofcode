import re
from collections import defaultdict

file_path = 'read.txt'
with open(file_path, 'r') as file:
    digitListPattern = r"((?:\d+ ?\n?)+)"
    wordPattern = r"[a-zA-Z]+"
    mapPattern = rf"(?:({wordPattern})-to-({wordPattern}) +map:\n{digitListPattern}\n?)*"
    inputPattern = rf"^seeds:\s*{digitListPattern}\n+({mapPattern})$"
    match = re.match(inputPattern, file.read())
    res = []
    if not match:
        print("Error Parsing 1")
    startSeeds = [int(i) for i in re.split(r"\s+", match.group(1)) if i != ""]
    sourceMap = None
    destMap = None
    for seed in startSeeds:
        fixed = False
        for line in match.group(2).split("\n"):
            titlePattern = rf"({wordPattern})-to-({wordPattern}) +map:"
            mapMatch = re.match(titlePattern, line)
            if mapMatch:
                sourceMap = mapMatch.group(1)
                destMap = mapMatch.group(2)
                fixed = False
            else:
                v = tuple(int(i) for i in re.split(r"\s+", line) if i != "")
                if v:
                    dest, source, length = v
                    diff = dest - source
                    print(v)
                    if source <= seed < (source + length):
                        if not fixed:
                            fixed = True
                            seed += diff
        res.append(seed)
    #     print()
    # print(res)
    print(min(res))