import parse


class Valve:
    def __init__(self, name=None, flow=0, neighbours=[] ):
        self.neighbours = neighbours
        self.flow = flow
        self.name = name

    def __repr__(self):
        return f"Valve(name={self.name}, flow={self.flow}, neighbours={self.neighbours})"

class ParseError(Exception):
    pass

def parse_input_line(line: str) -> Valve:
    valve = Valve()
    if "tunnels" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnels lead to valves {to_valves:D}", line.strip())
    elif "tunnel" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnel leads to valve {to_valves:D}", line.strip())
    else:
        raise ParseError(line)

    valve.name = result.named["valve_name"]
    valve.flow = result.named["flow"]
    valve.neighbours = result.named["to_valves"].split(", ")
    return valve

def parse_data(test_data:list)->list:


