class Hand:
    def __init__(self, hand: str):
        self.hand: str = hand
        self.handType: int = self.handType()

    def __gt__(self, other):
        if self.hand == other.hand:
            return False
        if self.handType != other.handType:
            return self.handType > other.handType
        strengthMapping = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
        for h1, h2 in zip(self.hand, other.hand):
            if strengthMapping[h1] != strengthMapping[h2]:
                return strengthMapping[h1] > strengthMapping[h2]
        return False

    def __le__(self, other):
        return self == other or self < other

    def __lt__(self, other):
        return not (self == other or self > other)

    def __ge__(self, other):
        return self == other or self > other

    def __eq__(self, other):
        return self.hand == other.hand

    def __ne__(self, other):
        return self.hand != other.hand

    def __repr__(self) -> str:
        return f"({self.hand}, {self.handType})"

    def __str__(self) -> str:
        return f"({self.hand}, {self.handType})"

    def handType(self):
        s = list(set(self.hand))
        if len(s) == 1:
            return 7
        sym = ""
        curr = 0
        for i in s:
            if i != "J" and self.hand.count(i) > curr:
                curr = self.hand.count(i)
                sym = i
        print(sym)
        tmpHand = self.hand.replace("J", sym)
        print(tmpHand)
        if len(s) == 5:
            return 1
        s = list(set(tmpHand))
        if len(s) == 4:
            return 2
        if len(s) == 3:
            return 4 if 3 in (tmpHand.count(s[0]), tmpHand.count(s[1]), tmpHand.count(s[2])) else 3
        if len(s) == 2:
            print(tmpHand.count(s[0]))
            return 6 if tmpHand.count(s[0]) in (1, 4) else 5
        if len(s) == 1:
            return 7

class Node:
    def __init__(self, hand: Hand, bid: int) -> None:
        self.bid: int = bid
        self.hand: Hand = hand
        self.right: Node = None
        self.left: Node = None

    def addNode(self, other):
        if other.hand > self.hand:
            if self.right == None:
                self.right = other
            else:
                self.right.addNode(other)
        else:
            if self.left == None:
                self.left = other
            else:
                self.left.addNode(other)

    def __repr__(self, depth=1) -> str:
        indent = "\t" * depth
        s = f"{self.hand}"
        if self.right:
            s += f"\n{indent}Right: {self.right.__repr__(depth + 1)}"
        if self.left:
            s += f"\n{indent}Left: {self.left.__repr__(depth + 1)}"
        return s

    def totalWinnings(self, seen=1):
        if self.left == None and self.right == None:
            return (seen, seen * self.bid)
        if self.left == None:
            rightSeen, rightWinnings = self.right.totalWinnings(seen + 1)
            return (rightSeen, seen * self.bid + rightWinnings)
        leftSeen, leftWinnings = self.left.totalWinnings(seen)
        if self.right == None:
            return (leftSeen + 1, leftWinnings + (leftSeen) * self.bid)
        rightSeen, rightWinnings = self.right.totalWinnings(leftSeen + 2)
        return (rightSeen + 1, leftWinnings + (leftSeen + 1) * self.bid + rightWinnings)

class BST:
    def __init__(self) -> None:
        self.top: Node = None

    def addNode(self, node: Node):
        if self.top == None:
            self.top = node
        else:
            self.top.addNode(node)

    def totalWinnings2(self):
        if self.top == None:
            return(0, 0)
        else:
            return self.top.totalWinnings()

    def totalWinnings(self):
        def helper(root):
            if not root:
                return []
            return helper(root.left) + [root.bid] + helper(root.right)
        return sum((idx + 1) * value for idx, value in enumerate(helper(self.top)))

    def __repr__(self) -> str:
        return f"{self.top}"

bst = BST()
for i in range(int(input())):
    hand, bid = input().split()
    hand, bid = Hand(hand), int(bid)
    print(f"---------------------------------------------{hand}---------------------------------------------")
    bst.addNode(Node(hand, bid))
# print(bst)
print(bst.totalWinnings())