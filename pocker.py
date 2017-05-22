"""
a pocker hand game
"""

import random

DECK = [r+s for r in '23456789TJQKA' for s in 'SHCD']

def deal(numHands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHCD']):
    random.shuffle(deck)
    hands = []
    for x in range(numHands):
        hand = deck[n*x:n*(x+1)]
        h_str = ''
        for h in range(len(hand)):
            if h != len(hand)-1:
                h_str+=hand[h]+' '
            else:
                h_str += hand[h]
        hands.append(h_str)
    return hands

def max_hands(hands):
    """find the max hand in hands"""
    hands.sort(key=hand_rank, reverse=True)
    m = hands[0]
    return [x for x in hands if x == m]


def hand_rank(hand):
    "return a number rank of the hand"
    ranks = cards_rank(hand)
    if straight(ranks) and flush(ranks):
        return (9, max(ranks)[0])
    elif kind(4, ranks):
        return (8, kind(4, ranks), kind(1, ranks))
    elif full_house(ranks):
        return (7, kind(3, ranks), kind(2, ranks))
    elif flush(ranks):
        return (6, [x for x, y in ranks])
    elif straight(ranks):
        return (5, max(ranks)[0])
    elif kind(3, ranks):
        return (4, [x for x, y in ranks])
    elif pair(2, ranks):
        return (3, [x for x, y in ranks])
    elif pair(1, ranks):
        return (2, [x for x, y in ranks])
    else:
        return (1, [x for x, y in ranks])


def kind(n, ranks):
    "n kind of card in ranks"
    count = card_counter(ranks)
    for k, v in count:
        if v == n:
            return k
    return False

def full_house(ranks):
    "kind 3 and 1 pair"
    count = card_counter(ranks)
    max_c = 0
    min_c = 5
    for k, v in count:
        if v > max_c:
            max_c = v
        if v < min_c:
            min_c = v
    if max_c == 3 and min_c == 2:
        return True
    return False

def flush(ranks):
    suit = ''
    for k, s in ranks:
        if suit == '':
            suit = s
        elif suit != s:
            return False
    return True

def straight(hands):
    before = hands[0][0]+1
    for k, s in hands:
        if before-k != 1:
            return False
        before = k
    return True

def pair(n,hands):
    count = card_counter(hands)
    pairs = 0
    for k, v in count:
        if v == 2:
            pairs += 1
    if pairs == n:
        return True
    return False

def card_counter(ranks):
    "count card repeated, return list like [(1,3),(11,2)]"
    count = {}
    for rank in ranks:
        key = rank[0]
        count[key] = count.get(key, 0)+1
    return [x for x in count.items()]

def cards_rank(hand):
    "parse hand '2s 3d 4h 5c 6d' to rank(6,5,4,3,2,1)"
    cards = hand.split(' ')
    cards = [card_parse(x) for x in hand.split()]
    cards.sort(key=lambda x: x[0], reverse=True)
    if [x for x, y in cards] == [14, 5, 4, 3, 2]:
        cards[0] = (1, cards[0][1])
        cards.sort(key=lambda x: x[0], reverse=True)
    return cards

def card_parse(card):
    "convert card to number"
    num = '--23456789TJQKA'.index(card[0])
    return (num, card[1])


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


def test():
    "test max_hands"
    straight_flush = '2S 3S 4S 5S 6S'
    fh = "7S 7D 7H 5C 5C"
    fh2= "7S 7D 7C 6C 6C"
    k4 = "JS JH JC JD KH"
    p2 = "5S 5D TC TH 2S"
    assert card_parse('JH') == (11, 'H')
    assert cards_rank(straight_flush) == [(6, 'S'), (5, 'S'), (4, 'S'), (3, 'S'), (2, 'S')]
    assert cards_rank(p2) == [(10, 'C'), (10, 'H'), (5, 'S'), (5, 'D'), (2, "S")]
    assert [x for x, y in cards_rank(fh)] == [7, 7, 7, 5, 5]
    count = card_counter(cards_rank(p2))
    count.sort()
    assert count == [(2, 1), (5, 2), (10, 2)]
    assert card_counter(cards_rank(fh)) == [(5, 2), (7, 3)]
    assert kind(4, cards_rank(k4)) == 11
    assert kind(1, cards_rank(k4)) == 13
    assert kind(3, cards_rank(fh)) == 7
    assert kind(2, cards_rank(fh)) == 5
    assert full_house(cards_rank(fh2))
    assert flush(cards_rank(straight_flush))
    assert straight(cards_rank(straight_flush))
    assert pair(2, cards_rank(p2))
    assert pair(1, cards_rank(p2)) is False
    assert pair(1, cards_rank(fh))
    straight_a = "AD 2C 3H 4H 5S"
    assert straight(cards_rank(straight_a))
    #assert hand_rank(straight_flush) == (9, 6)
    assert max_hands([straight_a, p2]) == [straight_a]
    assert max_hands([fh, fh]) == [fh, fh]
    print(deal(4))
    print('OK')

if __name__ == '__main__':
    test()
    frequent(700000)

