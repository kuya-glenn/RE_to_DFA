from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA



dfa0 = VisualDFA(
states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"
        , "q8", "q9", "q10", "q11", "q12", "q13", "q14","q15"},
input_symbols={"a", "b"},
transitions={
"q0": {"a": "q1", "b": "q1"},
"q1": {"a": "q2", "b": "q3"},
"q2": {"a": "q4", "b": "q3"},
"q3": {"b": "q4", "a": "q2"},
"q4": {"a": "q5", "b": "q6"},
"q5": {"b": "q7", "a": "q4"},
"q6": {"a": "q7", "b": "q4"},
"q7": {"a": "q8", "b": "q9"},
"q8": {"a": "q7", "b": "q10"},
"q9": {"b": "q7", "a": "q11"},
"q10": {"a": "q13", "b": "q12"},
"q11": {"a": "q14", "b": "q12"},
"q12": {"b": "q12", "a": "q12"},
"q13": {"a": "q15", "b": "q15"},
"q14": {"a": "q15", "b": "q15"},
"q15": {"a": "q15", "b": "q15"},
},
initial_state="q0",
final_states={"q14", "q15"},
        )

def first_dfa(input_text):
    user_input = input_text
    dfa0.show_diagram(str(user_input), view = True)

dfa1 = VisualDFA(
states={"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"
        , "q8", "q9", "q10", "q11"},
input_symbols={"1", "0"},
transitions={
"q0": {"0": "q2", "1": "q1"},
"q1": {"0": "q3", "1": "q4"},
"q2": {"1": "q3", "0": "q4"},
"q3": {"0": "q3", "1": "q3"},
"q4": {"0": "q6", "1": "q5"},
"q5": {"0": "q8", "1": "q7"},
"q6": {"0": "q6", "1": "q7"},
"q7": {"0": "q8", "1": "q9"},
"q8": {"0": "q10", "1": "q11"},
"q9": {"0": "q10", "1": "q11"},
"q10": {"0": "q10","1":"q11"},
"q11": {"1": "q11","0":"q10"},
},
initial_state="q0",
final_states={"q10", "q11"},
)

def second_dfa(input_text):
    user_input = input_text
    dfa1.show_diagram(str(user_input), view = True)
    

