# automata/nfa.py

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for next_state in self.transition_function.get(state, {}).get('', []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def validate_input(self, input_str):
        current_states = self._epsilon_closure({self.start_state})
        for symbol in input_str:
            next_states = set()
            for state in current_states:
                for target in self.transition_function.get(state, {}).get(symbol, []):
                    next_states.update(self._epsilon_closure({target}))
            current_states = next_states
        return bool(current_states & self.accept_states)
