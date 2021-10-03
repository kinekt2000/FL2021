from dataclasses import dataclass
from typing import Callable, Hashable

from queue import Queue
from itertools import product

@dataclass(frozen=True)
class Automata:
    states: set
    alphabet: set
    mapping: Callable[[Hashable, Hashable], Hashable]
    start_state: Hashable
    end_states: set


class find_equivalence_classes:
    def __init__(self):
        self.distinguishing_lines = {}


    def __call__(self, automata: Automata):
        # create backward transitions table
        back_transitions_table = {}
        for state in automata.states:
            whence_by_symbols = {}
            for symbol in automata.alphabet:
                whence = []
                for whence_state in automata.states:
                    if automata.mapping(whence_state, symbol) == state:
                        whence.append(whence_state)
                whence_by_symbols[symbol] = whence
            back_transitions_table[state] = whence_by_symbols

        # create table for quivalent states
        equivalence_table = {}
        for state0 in automata.states:
            for state1 in automata.states:
                if state1 != state0:
                    equivalence_table[frozenset([state0, state1])] = None

        # create queue for nonequivalent states
        pairs_queue = Queue()
        
        # fill initial queue
        not_end_states = automata.states - automata.end_states
        for end_state in automata.end_states:
            for state in not_end_states:
                pair = frozenset([state, end_state])
                pairs_queue.put(pair)
                equivalence_table[pair] = []

        # handle queue
        while(not pairs_queue.empty()):
            current_pair = pairs_queue.get()
            state0, state1 = current_pair
            for symbol in automata.alphabet:
                back0 = back_transitions_table[state0][symbol]
                back1 = back_transitions_table[state1][symbol]
                new_pairs = set(filter(lambda p: len(p) == 2 ,[frozenset(pair) for pair in product(back0, back1)]))
                for new_pair in new_pairs:
                    if equivalence_table[new_pair] is None:
                        pairs_queue.put(new_pair)
                        equivalence_table[new_pair] = [symbol] + equivalence_table[current_pair]

        self.distinguishing_lines = dict(map(
            lambda item: (tuple(item[0]), item[1]),
            dict(filter(lambda item: item[1] is not None, equivalence_table.items())).items()
        )) 

        return list(map(
            lambda x: tuple(x),
            list(dict(filter(lambda item: item[1] is None, equivalence_table.items())).keys())
        ))