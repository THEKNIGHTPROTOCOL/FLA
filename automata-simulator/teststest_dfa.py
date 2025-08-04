import unittest
from automata.dfa import DFA

class TestDFA(unittest.TestCase):
    def setUp(self):
        self.dfa = DFA(
            {'q0', 'q1'},
            {'0', '1'},
            {
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q1', '1': 'q0'}
            },
            'q0',
            {'q0'}
        )

    def test_valid_string(self):
        self.assertTrue(self.dfa.validate_input("1100"))

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.dfa.validate_input("1102")

if __name__ == '__main__':
    unittest.main()
