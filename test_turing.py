import unittest
from turing import TuringMachine

class TestTuringMachine(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.rules = [
            ['1RB', '1RC'],
            ['0RC', '1LA'],
            ['HLT', '0LB']
        ] # should halt after 3 steps
        self.tm = TuringMachine(self.rules)

    def test_initial_state(self):
        # Test the initial state of the Turing machine
        for i in range(2):
            self.tm.next_move()

        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")
        self.assertEqual(self.tm.number_of_moves, 3)
        self.assertEqual(self.tm.done, True)

    def test_2states_2symbols(self):
        # Test the Turing machine with 2 states and 2 symbols
        self.rules = [
            ['1RB', '1LB'],
            ['1LA', '---']
        ] # Should halt after 6 steps
        self.tm = TuringMachine(self.rules)

        for i in range(5):
            self.tm.next_move()
        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")
        self.assertEqual(self.tm.number_of_moves, 6)
        self.assertEqual(self.tm.done, True)

    def test_busy_beaver_4(self):
        #self.rules = [['1R1', '1L1'], ['1L2', '0L0'], ['1R3', '1L0'], ['1R0', 'HLT']] # Should halt after 107 steps
        self.rules = [
            ['1RB', '1LB'],
            ['1LA', '0LC'],
            ['---', '1LD'],
            ['1RD', '0RA']
        ] # BB(4) champion, should halt after BB(4)=107 steps
        self.tm = TuringMachine(self.rules)

        for i in range(106):
            self.tm.next_move()
        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")
        self.assertEqual(self.tm.number_of_moves, 107)
        self.assertEqual(self.tm.done, True)

if __name__ == '__main__':
    unittest.main()
