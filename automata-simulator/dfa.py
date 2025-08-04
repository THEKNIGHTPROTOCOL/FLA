# automata/dfa.py

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def validate_input(self, input_str):
        current_state = self.start_state
        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(f"Invalid symbol: {symbol}")
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states
