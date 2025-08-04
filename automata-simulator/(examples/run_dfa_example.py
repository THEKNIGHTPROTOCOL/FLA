from automata.dfa import DFA

states = {'q0', 'q1'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q1', '1': 'q0'}
}
start_state = 'q0'
accept_states = {'q0'}

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

print(dfa.validate_input("1100"))  # Output: True
