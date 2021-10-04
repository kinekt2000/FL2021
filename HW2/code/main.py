from automata import Automata, find_equivalence_classes

not_minimized = Automata(
    states=set([
            "S", "10", "11", "01", "20", "21", "12",
            "02", "30", "31", "22", "13", "03", "X",
            "32", "23", "14", "04", "3a", "2a", "1a"
        ]),
    alphabet=set(["a", "b"]),
    mapping=lambda state, symbol: ({
        "S" : { "a": "10", "b": "01" },
        "10": { "a": "20", "b": "11" },
        "11": { "a": "21", "b": "12" },
        "01": { "a": "11", "b": "02" },
        "20": { "a": "30", "b": "21" },
        "21": { "a": "31", "b": "22" },
        "12": { "a": "22", "b": "13" },
        "02": { "a": "12", "b": "03" },
        "30": { "a": "X" , "b": "31" },
        "31": { "a": "X" , "b": "32" },
        "22": { "a": "32", "b": "23" },
        "13": { "a": "23", "b": "14" },
        "03": { "a": "13", "b": "04" },
        "X" : { "a": "X" , "b": "X"  },
        "32": { "a": "X" , "b": "3a" },
        "23": { "a": "3a", "b": "2a" },
        "14": { "a": "2a", "b": "1a" },
        "04": { "a": "14", "b": "04" },
        "3a": { "a": "X" , "b": "3a" },
        "2a": { "a": "3a", "b": "2a" },
        "1a": { "a": "2a", "b": "1a" }
    }[state][symbol]),
    start_state="S",
    end_states=set(["13", "03", "23", "14", "04", "3a", "2a", "1a"])
)

minimized = Automata(
    states=set([
        "S" , "01", "02", "0a",
        "10", "11", "12", "1a",
        "20", "21", "22", "2a",
        "30", "31", "32", "3a",
        "X"
    ]),
    alphabet=set(["a", "b"]),
    mapping=lambda state, symbol: ({
        "S" : { "a": "10", "b": "01"},
        "01": { "a": "11", "b": "02"},
        "02": { "a": "12", "b": "0a"},
        "0a": { "a": "1a", "b": "0a"},

        "10": { "a": "20", "b": "11"},
        "11": { "a": "21", "b": "12"},
        "12": { "a": "22", "b": "1a"},
        "1a": { "a": "2a", "b": "1a"},
        
        "20": { "a": "30", "b": "21"},
        "21": { "a": "31", "b": "22"},
        "22": { "a": "32", "b": "2a"},
        "2a": { "a": "3a", "b": "2a"},
        
        "30": { "a": "X" , "b": "31"},
        "31": { "a": "X" , "b": "32"},
        "32": { "a": "X" , "b": "3a"},
        "3a": { "a": "X" , "b": "3a"},
        
        "X" : { "a": "X" , "b": "X" }
    }[state][symbol]),
    start_state="S",
    end_states=set(["0a", "1a", "2a", "3a"])
)



if __name__ == "__main__":
    print(find_equivalence_classes(minimized))
    for pair, line in find_equivalence_classes.distinguishing_lines.items():
        if(line):
            print(f"({pair[0]}, {pair[1]}): \"{''.join(line)}\"")

