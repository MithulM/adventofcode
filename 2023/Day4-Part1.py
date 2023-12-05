import re

def parse_card_string(card_string):
    # Define a regular expression pattern to match the card string
    pattern = r"Card +(\d+): (.+?) \| (.+)$"

    # Use re.match to find matches in the input string
    match = re.match(pattern, card_string)

    if match:
        # Extract the matched groups
        n = int(match.group(1))
        winnings = set(map(int, match.group(2).split()))
        scores = list(map(int, match.group(3).split()))

        return n, winnings, scores
    else:
        # Return None if no match is found
        return None
t = 0
for i in range(int(input())):
    x = parse_card_string(input())
    p = 1
    if x:
        n, winnings, scores = x
        for score in scores:
            if score in winnings:
                p *= 2
        t += p // 2
    else:
        print("Error parsing")
print(t)