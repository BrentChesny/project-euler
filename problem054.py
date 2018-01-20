from collections import namedtuple

class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)

STRAIGHT_FLUSH = 9
FOUR_OF_A_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_OF_A_KIND = 4
TWO_PAIRS = 3
ONE_PAIR = 2
HIGH_CARD = 1 

suit = ['H', 'D', 'C', 'S']
face = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
lowace = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

face_order = lambda f: face.index(f)
is_sublist = lambda l1, l2: any(l1 == l2[i:j] for i in range(len(l2)) for j in range(i, len(l2)))

def straightflush(hand):
    fs = lowace if any(card.face == '2' for card in hand) else face
    ordered = sorted(hand, key=lambda card: (fs.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if all(card.suit == first.suit for card in rest) and is_sublist([card.face for card in ordered], fs):
        return STRAIGHT_FLUSH, ordered[-1].face
    return False

def fourofakind(hand):
    allfaces = [f for f, s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return FOUR_OF_A_KIND, [f, allftypes.pop()]
    else:
        return False

def fullhouse(hand):
    allfaces = [f for f, s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return FULL_HOUSE, [f, allftypes.pop()]
    else:
        return False

def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f, s in hand]
        return FLUSH, sorted(allfaces, key=face_order, reverse=True)
    return False

def straight(hand):
    fs = lowace if any(card.face == '2' for card in hand) else face
    ordered = sorted(hand, key=lambda card: (fs.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if is_sublist([card.face for card in ordered], fs):
        return STRAIGHT, ordered[-1].face
    return False

def threeofakind(hand):
    allfaces = [f for f, s in hand]
    allftypes = set(allfaces)
    if len(allftypes) <= 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return (THREE_OF_A_KIND, [f] + sorted(allftypes, key=face_order, reverse=True))
    else:
        return False

def twopair(hand):
    allfaces = [f for f, s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return TWO_PAIRS, pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other

def onepair(hand):
    allfaces = [f for f, s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return ONE_PAIR, pairs + sorted(allftypes, key=face_order, reverse=True)

def highcard(hand):
    allfaces = [f for f, s in hand]
    return HIGH_CARD, sorted(allfaces, key=face_order, reverse=True)

def rank(hand):
    possible_hands = [
        straightflush,
        fourofakind,
        fullhouse,
        flush,
        straight,
        threeofakind,
        twopair,
        onepair,
        highcard
    ]

    for func in possible_hands:
        rank = func(hand)
        if rank:
            break
    return rank

def parse_input():
    hands = []
    for line in open('resources/p054_poker.txt').readlines():
        cards = line.strip().split()
        hand1 = [Card(f, s) for f,s in cards[:5]]
        hand2 = [Card(f, s) for f,s in cards[5:]]
        hands.append((hand1, hand2))
    return hands

def solve():
    result = 0
    for hand1, hand2 in parse_input():
        rank1, tiebreaker1 = rank(hand1)
        rank2, tiebreaker2 = rank(hand2)
        if rank1 > rank2:
            result += 1
        elif rank1 == rank2:
            for t1, t2 in zip(tiebreaker1, tiebreaker2):
                if face.index(t1) == face.index(t2):
                    continue
                elif face.index(t1) > face.index(t2):
                    result += 1
                break
            
    return result

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
