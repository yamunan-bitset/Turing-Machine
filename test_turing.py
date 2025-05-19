import unittest
from turing import TuringMachine

class TestTuringMachine(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.rules = [
            ['1R1', '1R2'],
            ['0R2', '1L0'],
            ['HLT', '0L1']
        ] # should halt after 3 steps
        self.tm = TuringMachine(self.rules)

    def test_initial_state(self):
        # Test the initial state of the Turing machine
        for i in range(2):
            self.tm.next_move()

        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")


    def test_2states_2symbols(self):
        # Test the Turing machine with 2 states and 2 symbols
        self.rules = [
            ['1R1', '1L1'],
            ['1L0', '1RH']
        ] # Should halt after 6 steps
        self.tm = TuringMachine(self.rules)

        for i in range(5):
            self.tm.next_move()
        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")

    def test_busy_beaver_4(self):
        #self.rules = [['1R1', '1L1'], ['1L2', '0L0'], ['1R3', '1L0'], ['1R0', 'HLT']] # Should halt after 107 steps
        self.rules = [
            ['1R1', '1L1'],
            ['1L0', '0L2'],
            ['1RH', '1L3'],
            ['1R3', '0R0']
        ] # should halt after 107 steps
        self.tm = TuringMachine(self.rules)

        for i in range(106):
            self.tm.next_move()
        x = self.tm.next_move()
        self.assertEqual(x, "HLT!! Turing machine halted.")
        

if __name__ == '__main__':
    unittest.main()
