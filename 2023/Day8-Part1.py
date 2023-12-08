import re
mapping = {}
instructions = list(map(int, input().replace("L", "0").replace("R", "1")))
for i in range(int(input())):
    x = input()
    print(x)
    match = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", x)
    if not match:
        print("Error")
    mapping[match.group(1)] = (match.group(2), match.group(3))
idx = 0
curr = "AAA"
while curr != "ZZZ":
    curr = mapping[curr][instructions[idx % len(instructions)]]
    idx += 1
print(idx)