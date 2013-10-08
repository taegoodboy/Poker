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
   
if __name__ == '__main__':
    unittest.main(exit=False)

