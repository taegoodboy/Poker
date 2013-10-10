numberOfmember = input('Number of player(2-5): ')
while numberOfmember>5 or numberOfmember<2:
    numberOfmember = input('Number of player(2-5): ')
        
import random    

def randomCard(x):
    """
    ([hand, hand, ...])-> hands
    Return hands that random card for each hand
    """
    while len(x)<5:
        x.append(''+random.choice(['2','3','4','5','6','7','8','9','T','J','Q','K'])+random.choice(['C','D','H','S']))
    return x


def checkhand(hands):
    """
    ([hand, hand, ...])-> hands
    Return hands that not same as another hand
    """
    listcard=[]
    n=0
    for hand in hands:
        for card in hand:
            if card not in listcard:
                listcard.append(card)
                n+=1
            else:
                hands[n/5]=[]
                randomCard(hands[n/5])

def poker(hands):
    """
    ([hand, hand, ...])-> hands
 
    Return the best hand from list of hands
    """
    return allmax(hands)

def allmax(hands):
    """
    ([hand, hand, ...])-> hands

    Return winner hand
    """
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

def hand_rank(hand):
    """
    (hand)-> int

    Return the hand rank of a hand
    
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

    """
    return straight(hand) and flush(hand)

def straight(hand):
    """
    (hand)-> Bool

    Return True if hand is straight,
    False otherwise
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
    """

    suits = [s for r,s in hand]

    return len(set(suits)) == 1

def kind(n, ranks):
    """
    (ranks)-> int

    Return rank if hand is n kind,
    false otherwise
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
    """
    
    return True if kind(3, ranks) and kind(2, ranks) else False

def twopair(ranks):
    """
    (ranks)-> tuple

    Return tuple of highpair and lowpair if hand is twopair,
    false otherwise
    """
    ranks.sort(reverse=True)
    high_pair = kind(2, ranks)
    ranks.sort()
    low_pair = kind(2, ranks)
    ranks.sort(reverse=True)
    if high_pair != low_pair:
        return (high_pair, low_pair)
    return ()

def check_state_of_winner(hand):
    """
    (hand)-> str

    Return rank of Winner card
    """
    winnerhand = hands
    if hand_rank(winnerhand[0])[0]==8:
        return "Win by StraightFlush"
    elif hand_rank(winnerhand[0])[0]==7:
        return "Win by Four of a kinds"
    elif hand_rank(winnerhand[0])[0]==6:
        return "Win by FullHouse"
    elif hand_rank(winnerhand[0])[0]==5:
        return "Win by Flush"
    elif hand_rank(winnerhand[0])[0]==4:
        return "Win by Straight"
    elif hand_rank(winnerhand[0])[0]==3:
        return "Win by Three of a kinds"
    elif hand_rank(winnerhand[0])[0]==2:
        return "Win by Two pairs"
    elif hand_rank(winnerhand[0])[0]==1:
        return "Win by One pairs"
    else:
        return "Win by HighCard"
    

##operation
hands=[]
for i in xrange(numberOfmember):
    temp=[]
    hands.append(randomCard(temp))

for i in xrange(1000):
    checkhand(hands)

n=1
for i in hands:
    print 'Player'+str(n)+str(i)
    n+=1
print "Winner is who has card : "+str(poker(hands))
print check_state_of_winner(poker(hands))


