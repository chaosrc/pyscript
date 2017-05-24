"""
a pocker hand game
"""

import random

DECK = [r+s for r in '23456789TJQKA' for s in 'SHCD']

def deal(numHands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHCD']):
    #random.shuffle(deck)
    shuffle(deck)
    hands = []
    for x in range(numHands):
        hands.append(deck[n*x:n*(x+1)])
    return hands

def max_hands(hands):
    """find the max hand in hands"""
    hands.sort(key=hand_rank, reverse=True)
    m = hands[0]
    return [x for x in hands if x == m]


def hand_rank(hand):
    "return a number rank of the hand"
    ranks, suits = cards_rank(hand)
    count = card_counter(ranks)
    isstraight = straight(ranks)
    isflush = flush(suits)
    return (9 if isstraight and isflush else
            8 if count == [4, 1] else
            7 if count == [3, 2] else
            6 if isflush else
            5 if isstraight else
            4 if count == [3, 1, 1] else
            3 if count == [2, 2, 1] else
            2 if count == [2, 1, 1, 1] else
            1, ranks)
    # if straight(ranks) and flush(suits):
    #     return (9, max(ranks))
    # elif kind(4, ranks):
    #     return (8, ranks)
    # elif full_house(ranks):
    #     return (7, ranks)
    # elif flush(suits):
    #     return (6, ranks)
    # elif straight(ranks):
    #     return (5, ranks)
    # elif kind(3, ranks):
    #     return (4, ranks)
    # elif pair(2, ranks):
    #     return (3, ranks)
    # elif pair(1, ranks):
    #     return (2, ranks)
    # else:
    #     return (1, ranks)


def kind(n, ranks):
    "n kind of card in ranks"
    count = card_counter(ranks)
    for v in count:
        if v == n:
            return True
    return False

def full_house(ranks):
    "kind 3 and 1 pair"
    count = card_counter(ranks)
    max_c = 0
    min_c = 5
    for v in count:
        if v > max_c:
            max_c = v
        if v < min_c:
            min_c = v
    if max_c == 3 and min_c == 2:
        return True
    return False

def flush(suits):
    start = ''
    for s in suits:
        if start == '':
            start = s
        elif start != s:
            return False
    return True

def straight(hands):
    before = hands[0]+1
    for k in hands:
        if before-k != 1:
            return False
        before = k
    return True

def pair(n,hands):
    count = card_counter(hands)
    pairs = 0
    for v in count:
        if v == 2:
            pairs += 1
    if pairs == n:
        return True
    return False

def card_counter(ranks):
    "count card repeated, return list like [(1,3),(11,2)]"
    count = [ranks.count(x) for x in set(ranks)]
    count.sort(reverse=True)
    return count

def cards_rank(hand):
    "parse hand '2s 3d 4h 5c 6d' to rank(6,5,4,3,2,1)"
    if isinstance(hand, str):
        hand = hand.split()
    ranks = []
    suits = []
    for x, y in hand:
        ranks.append(card_parse(x))
        suits.append(y)
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks, suits

def card_parse(card):
    "convert card to number"
    num = '--23456789TJQKA'.index(card)
    return num


def frequent(n):
    f = [0]*9
    category = ['high card', 'one pair', 'two pair', 'three of kind', \
    'straight', 'flush', 'full house', 'four of kind', 'straight flush']
    for i in range(n):
        hand = deal(1)
        kd = hand_rank(hand[0])[0]
        f[kd-1] += 1
    for k in range(9):
        print('%s : %.4f%%'%(category[k], f[k]*100/n))

def shuffle(li):
    length = len(li)
    isstr = isinstance(li, str)
    if isstr:
        li = list(li)
    for x in range(length):
        r = random.randrange(x, length)
        li[x], li[r] = li[r], li[x]
    if isstr:
        return ''.join(li)


def test():
    "test max_hands"
    straight_flush = '2S 3S 4S 5S 6S'
    fh = "7S 7D 7H 5C 5C"
    fh2= "7S 7D 7C 6C 6C"
    k4 = "JS JH JC JD KH"
    p2 = "5S 5D TC TH 2S"
    assert card_parse('J') == 11
    assert cards_rank(straight_flush) == ([6, 5, 4, 3, 2], ['S', 'S', 'S', 'S', 'S'])
    assert cards_rank(p2) == ([10, 10, 5, 5, 2], ['S', 'D', 'C', 'H', 'S'])
    assert cards_rank(fh)[0] == [7, 7, 7, 5, 5]
    count = card_counter(cards_rank(p2)[0])
    assert count == [2, 2, 1]
    assert card_counter(cards_rank(fh)[0]) == [3, 2]
    assert kind(4, cards_rank(k4)[0])
    assert kind(1, cards_rank(k4)[0])
    assert kind(3, cards_rank(fh)[0])
    assert kind(2, cards_rank(fh)[0])
    assert full_house(cards_rank(fh2)[0])
    assert flush(cards_rank(straight_flush)[1])
    assert straight(cards_rank(straight_flush)[0])
    assert pair(2, cards_rank(p2)[0])
    assert pair(1, cards_rank(p2)[0]) is False
    assert pair(1, cards_rank(fh)[0])
    straight_a = "AD 2C 3H 4H 5S"
    assert straight(cards_rank(straight_a)[0])
    #assert hand_rank(straight_flush) == (9, 6)
    assert max_hands([straight_a, p2]) == [straight_a]
    assert max_hands([fh, fh]) == [fh, fh]
    print(deal(4))
    print('OK')

def test_shuffle(num):
    freq = {}
    for _ in range(num):
        t = shuffle('abc')
        freq[t] = freq.get(t, 0)+1
    for k, v in freq.items():
        freq[k] = v/num*100
    print(freq) 

if __name__ == '__main__':
    test()
    #frequent(700)
    test_shuffle(6000)

