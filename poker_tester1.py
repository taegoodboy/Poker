import unittest
import poker

class Testpoker(unittest.TestCase):
    '''Example unittest test method for poker'''
    
    #kind of card ==> sf = straight flush > fk = four of a kind > fh = full house >
    #fl = flush > st = straight > tk = three of a kind > tp = two pair > op = one pair > hc = high card
    #type of card ==> S = spear card > H = heart card > D = diamond card > C = clover card
    #value of card ==> A = 14 > K = 13 > Q = 12 > J = 11 > T = 10 > 9...2 > A = 1

    def test_poker_tester_1(self):
        '''testcase poker1
        sf = ['TS','9S','8S','7S','6S']
        fk = ['9S','9C','9D','9H','KS']
        '''
        sf = ['TS','9S','8S','7S','5S']
        fk = ['9S','9C','9D','9H','KS']
        actual = poker.poker([sf,fk])
        expected = ['TS','9S','8S','7S','6S']
        self.assertEqual (actual,expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
