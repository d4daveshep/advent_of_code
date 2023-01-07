import parse


class Valve:
    def __init__(self):
        self.neighbours = None
        self.flow = None
        self.name = None

    pass


class ParseError(Exception):
    pass

def parse_input_line(line: str) -> Valve:
    valve = Valve()
    if "tunnels" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnels lead to valves {to_valves:D}", line)
    elif "tunnel" in line:
        result = parse.search("Valve {valve_name} has flow rate={flow:d}; tunnel leads to valve {to_valves:D}", line)
    else:
        raise ParseError(line)

    valve.name = result.named["valve_name"]
    valve.flow = result.named["flow"]
    valve.neighbours = result.named["to_valves"].split(", ")
    return valve
