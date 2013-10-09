import unittest
import poker

class Testpoker(unittest.TestCase):
    '''Example unittest test method for poker'''
    
    #kind of card ==> sf = straight flush > fk = four of a kind > fh = full house >
    #fl = flush > st = straight > tk = three of a kind > tp = two pair > op = one pair > hc = high card
    #type of card ==> S = spades card > H = heart card > D = diamond card > C = club card
    #value of card ==> A = 14 > K = 13 > Q = 12 > J = 11 > T = 10 > 9...2 > A = 1

    def test_poker_tester_1(self):
        '''testcase poker1 normal poker
        sf = ['JC', 'TC', '9C', '8C', '7C']
        fk = ['5S', '5H', '5D', '5C', 'KS']
        '''
        sf = ['JC', 'TC', '9C', '8C', '7C']
        fk = ['5S', '5H', '5D', '5C', 'KS']
        actual = poker.poker([sf,fk])
        expected = [['JC', 'TC', '9C', '8C', '7C']]
        self.assertEqual (actual,expected)
        
    def test_poker_tester_2(self):
        '''testcase poker2 normal flush
        sf = ['AC', '2C', '3C', '4C', '5C']
        fk = ['5S', '5H', '5D', '5C', 'KS']
        ''' 
        sf = ['AC', '2C', '3C', '4C', '5C']
        fk = ['5S', '5H', '5D', '5C', 'KS']
        actual1 = poker.flush(sf)
        actual2 = poker.flush(fk)
        expected1 = True
        expected2 = False
        self.assertEqual (actual1,expected1)
        self.assertEqual (actual2,expected2)
        
    def test_poker_tester_3(self):
        '''testcase poker3 normal
        sf = ['2C','3C','4C','5C','6C']
        fk = ['9S','9C','9D','9H','KS']
        '''
        sf = ['2C','3C','4C','5C','6C']
        fk = ['9S','9C','9D','9H','KS']
        actual = poker.poker([sf,fk])
        expected = [['2C','3C','4C','5C','6C']]
        self.assertEqual (actual,expected)

    def test_poker_straight(self):
        '''testcase poker normal
        sf = ['JC','TC','9C','8C','7C']
        fk = ['4S','4D','4C','4H','AD']
        '''
        actual = poker.straight(['JC','TC','9C','8C','7C'])
        expected = True
        self.assertEqual (actual,expected)

    def test_poker_tester_4(self):
        '''testcase poker4 same rank
        sf = ['JC', 'TC', '9C', '8C', '7C']
        sf2 = ['JS', 'TS', '9S', '8S', '7S']
        '''
        sf = ['JC','TC','9C','8C','7C']
        sf2 = ['JS', 'TS','9S','8S','7S']
        actual = poker.poker ([sf,sf2])
        expected = [['JS', 'TS','9S','8S','7S']]
        self.assertEqual (actual,expected)

### Function hand_rank

    def test_hand_rank_tester_1(self):
        '''testcase hand_rank high straight flush
        sf = ['JS', 'TS', '9S', '8S', '7S']
        '''
        sf = ['JS', 'TS', '9S', '8S', '7S']
        actual = poker.hand_rank(sf)[0]
        expected = 8
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_2(self):
        '''testcase hand_rank low straight flush
        sf = ['AC', '2C', '3C', '4C', '5C']
        '''
        sf = ['AC', '2C', '3C', '4C', '5C']
        actual = poker.hand_rank(sf)[0]
        expected = 8
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_3(self):
        '''testcase hand_rank low straight flush 
        sf = ['2C','3C','4C','5C','6C']
        '''
        sf = ['2C','3C','4C','5C','6C']
        actual = poker.hand_rank(sf)[0]
        expected = 8
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_4(self):
        '''testcase hand_rank normal four_of_a_kind 
        fk = ['5S', '5H', '5D', '5C', 'KS']
        '''
        fk = ['5S', '5H', '5D', '5C', 'KS']
        actual = poker.hand_rank(fk)[0]
        expected = 7
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_5(self):
        '''testcase hand_rank highest four_of_a_kind 
        fk = ['AS','AC','AD','AH','KS']
        '''
        fk = ['AS','AC','AD','AH','KS']
        actual = poker.hand_rank(fk)[0]
        expected = 7
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_6(self):
        '''testcase hand_rank lowest four_of_a_kind 
        fk = ['2S','2C','2D','2H','3S']
        '''
        fk = ['2S','2C','2D','2H','3S']
        actual = poker.hand_rank(fk)[0]
        expected = 7
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_7(self):
        '''testcase hand_rank normal full_house
        fh = ['5S', '5H', '5D', '8C', '8S']
        '''
        fh = ['5S', '5H', '5D', '8C', '8S']
        actual = poker.hand_rank(fh)[0]
        expected = 6
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_8(self):
        '''testcase hand_rank highest full_house
        fh = ['AS', 'AC', 'AD', 'KH', 'KS']
        '''
        fh = ['AS', 'AC', 'AD', 'KH', 'KS']
        actual = poker.hand_rank(fh)[0]
        expected = 6
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_9(self):
        '''testcase hand_rank normal flush
        fl = ['JC', '5C', '9C', '8C', '7C']
        '''
        fl = ['JC', '5C', '9C', '8C', '7C']
        actual = poker.hand_rank(fl)[0]
        expected = 5
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_10(self):
        '''testcase hand_rank normal straight
        st = ['JC', 'TC', '9C', '8S', '7C']
        '''
        st = ['JC', 'TC', '9C', '8S', '7C']
        actual = poker.hand_rank(st)[0]
        expected = 4
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_11(self):
        '''testcase hand_rank normal three_of_a_kind
        tk = ['5S', '7H', '8D', '8C', '8S']
        '''
        tk = ['5S', '7H', '8D', '8C', '8S']
        actual = poker.hand_rank(tk)[0]
        expected = 3
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_12(self):
        '''testcase hand_rank normal two_pair
        tp = ['5S', '5H', '9D', '8C', '8S']
        '''
        tp = ['5S', '5H', '9D', '8C', '8S']
        actual = poker.hand_rank(tp)[0]
        expected = 2
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_13(self):
        '''testcase hand_rank normal one_pair
        op = ['5S', '3H', '9D', '8C', '8S']
        '''
        op = ['5S', '3H', '9D', '8C', '8S']
        actual = poker.hand_rank(op)[0]
        expected = 1
        self.assertEqual (actual,expected)

    def test_hand_rank_tester_14(self):
        '''testcase hand_rank normal high_card
        hc = ['4S', '3H', '9D', '8C', 'TS']
        '''
        hc = ['4S', '3H', '9D', '8C', 'TS']
        actual = poker.hand_rank(hc)[0]
        expected = 0
        self.assertEqual (actual,expected)
        
### Function straight_flush

    def test_straight_flush_tester_1(self):
        '''testcase lowest straight_flush
        sf = ['AC','2C','3C','4C','5C']
        '''
        sf = ['AC','2C','3C','4C','5C']
        actual = poker.straight_flush(sf)
        expected = True
        self.assertEqual (actual,expected)

    def test_straight_flush_tester_2(self):
        '''testcase normal straight_flush
        sf = ['5H','6H','7H','8H','9H']
        '''
        sf = ['5H','6H','7H','8H','9H']
        actual = poker.straight_flush(sf)
        expected = True
        self.assertEqual (actual,expected)

    def test_straight_flush_tester_3(self):
        '''testcase highest straight_flush
        sf = ['AS','KS','QS','JS','TS']
        '''
        sf = ['AS','KS','QS','JS','TS']
        actual = poker.straight_flush(sf)
        expected = True
        self.assertEqual (actual,expected)

### Function straight

    def test_straight_tester_1(self):
        '''testcase high straight
        st = ['AC','KD','QH','JS','TS']
        '''
        st = ['AC','KD','QH','JS','TS']
        actual = poker.straight(st)
        expected = True
        self.assertEqual (actual,expected)

    def test_straight_tester_2(self):
        '''testcase normal straight_flush
        sf = ['5H','6H','7H','8H','9H']
        '''
        sf = ['5H','6H','7H','8H','9H']
        actual = poker.straight(sf)
        expected = True
        self.assertEqual (actual,expected)

    def test_straight_tester_3(self):
        '''testcase normal flush
        fl = ['4H','6H','7H','8H','9H']
        '''
        fl = ['4H','6H','7H','8H','9H']
        actual = poker.straight(fl)
        expected = False
        self.assertEqual (actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)

