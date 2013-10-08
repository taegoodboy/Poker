FP = ['5S', '3H', '9D', '8C', '8S']
SP = ['5S', '5H', '9D', '8C', '8S']
hands =[FP,SP]

def poker(hands):
    """
   ([hand, hand, ...])-> hands
 
   Return the best hand from list of hands
    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> fk = ['5S', '5H', '5D', '5C', 'KS']
    >>> sf2 = ['JS', 'TS', '9S', '8S', '7S']
    >>> poker([sf, sf2])
    [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
    >>> poker([sf, fk])
    [['JC', 'TC', '9C', '8C', '7C']]
    >>> fh = ['5S', '5H', '5D', '8C', '8S']
    >>> poker([fh, fk])
    [['5S', '5H', '5D', '5C', 'KS']]
    >>> s1 = ['JC', 'TC', '9C', '8S', '7C']
    >>> poker([fh, s1])
    [['5S', '5H', '5D', '8C', '8S']]
    >>> op = ['5S', '3H', '9D', '8C', '8S']
    >>> tp = ['5S', '5H', '9D', '8C', '8S']
    >>> hc = ['4S', '3H', '9D', '8C', 'TS']
    >>> poker([op, tp])
    [['5S', '5H', '9D', '8C', '8S']]
   """
    return allmax(hands)

def allmax(hands):
    winhand = max(hands, key=hand_rank)
    # for StraightFlush that 
    # same hand_rank
    if hand_rank(hands[0])==hand_rank(hands[1]):
        # same high card
        if hand_rank(hands[0])[1]==hand_rank(hands[1])[1]:
            if hands[0][0][1]<hands[1][0][1]:
                windhand = hands[1]
                hands.pop(0)
            else:
                winhand = hands[0]
                hands.pop(1)
                
    maxval = hand_rank(winhand)
    return [hand for hand in hands if hand_rank(hand)==maxval]
    
##    result = []
##    for hand in hands:
##        if hand_rank(hand) == maxval:
##            result.append(hand)
##    return result

def hand_rank(hand):
    """
    (hand)-> int

    Return the hand rank of a hand
    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> hand_rank(sf)
    (8, 11)
    >>> fk = ['5S', '5H', '5D', '5C', 'KS']
    >>> hand_rank(fk)
    (7, 5)
    >>> fh = ['5S', '5H', '5D', '8C', '8S']
    >>> hand_rank(fh)
    (6, 5)
    >>> f1 = ['JC', '5C', '9C', '8C', '7C']
    >>> hand_rank(f1)
    (5, [11, 9, 8, 7, 5])
    >>> s1 = ['JC', 'TC', '9C', '8S', '7C']
    >>> hand_rank(s1)
    (4, 11)
    """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
        
    if straight_flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks)
    elif fullhouse(ranks):
         return 6, kind(3, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(hand):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif twopair(ranks):
        return 2, twopair(ranks)[0], twopair(ranks)[1], kind(1, ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks
   

def straight_flush(hand):
    """
    (hand)-> Bool

    Return True if hand is straight_flush,
    False otherwise

    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> straight_flush(sf)
    True
    >>> fk = ['7S', '5H', '5D', '5C', '5S']
    >>> straight_flush(fk)
    False
    """
    return straight(hand) and flush(hand)

def straight(hand):
    """
    (hand)-> Bool

    Return True if hand is straight,
    False otherwise

    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> straight(sf)
    True
    >>> fk = ['4S','4D','4C','4H','AD']
    >>> straight (fk)
    False
    """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5    

def flush(hand):
    """
    (hand)-> Bool

    Return True if hand is flush, False otherwise.

    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> flush(sf)
    True
    >>> fk = ['5S', '5H', '5D', '5C', 'KS']
    >>> flush(fk)
    False
    """

    suits = [s for r,s in hand]

    return len(set(suits)) == 1

def kind(n, ranks):
    """
    (ranks)-> int

    Return rank if hand is n kind,
    false otherwise

    >>> sf_ranks = [11, 10, 9, 8, 7]
    >>> kind(4, sf_ranks)
    0
    >>> fk_ranks = [5, 5, 5, 5, 13]
    >>> kind(4, fk_ranks)
    5
    >>> fh_ranks = [5, 5, 5, 8, 8]
    >>> kind(3, fh_ranks)
    5
    >>> op_ranks = [5, 3, 9, 8, 8]
    >>> kind(2, op_ranks)
    8
    """
    
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return 0

def fullhouse(ranks):
    """
    (ranks)-> Bool

    Return True if hand is fullhouse,
    false otherwise

    >>> sf_ranks = [11, 10, 9, 8, 7]
    >>> fullhouse(sf_ranks)
    False
    >>> fk_ranks = [5, 5, 5, 5, 13]
    >>> fullhouse(fk_ranks)
    False
    >>> fh_ranks = [5, 5, 5, 8, 8]
    >>> fullhouse(fh_ranks)
    True
    """
    
    return True if kind(3, ranks) and kind(2, ranks) else False

def twopair(ranks):
    """
    (ranks)-> tuple

    Return tuple of highpair and lowpair if hand is twopair,
    false otherwise

    >>> sf_ranks = [11, 10, 9, 8, 7]
    >>> twopair(sf_ranks)
    ()
    >>> tp_ranks = [5, 5, 9, 8, 8]
    >>> twopair(tp_ranks)
    (8, 5)
    """
    ranks.sort(reverse=True)
    high_pair = kind(2, ranks)
    ranks.sort()
    low_pair = kind(2, ranks)
    ranks.sort(reverse=True)
    if high_pair != low_pair:
        return (high_pair, low_pair)
    return ()

print poker(hands)


