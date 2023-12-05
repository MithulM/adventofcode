import re
def parse_card_string(card_string):
    pattern = r"Card +(\d+): (.+?) \| (.+)$"
    match = re.match(pattern, card_string)
    if match:
        n = int(match.group(1))
        winnings = set(map(int, match.group(2).split()))
        scores = list(map(int, match.group(3).split()))
        return n, winnings, scores
n = int(input())
t = 0
runSum = 0
accum = [0] * (n + 1)
accum[0] = 1
cards = [x for _ in range(n) if (x := parse_card_string(input()))]
for n, winnings, scores in cards:
    p = sum(int(score in winnings) for score in scores)
    runSum += accum[n - 1]
    accum[n] += runSum
    accum[n + p] -= runSum
    t += runSum
print(t)