import parse
import pytest

from day_16 import parse_input_line


def test_parse_input_line_1():
    line = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    result = parse.search("Valve {valve_label} has flow rate={flow:d}; tunnels lead to valves {to_valves:D}", line)
    assert result.named["valve_label"] == "AA"
    assert result.named["flow"] == 0
    assert result.named["to_valves"] == "DD, II, BB"

    line = "Valve HH has flow rate=22; tunnel leads to valve GG"
    result = parse.search("Valve {valve_label} has flow rate={flow:d}; tunnel leads to valve {to_valves:D}", line)
    assert result.named["valve_label"] == "HH"
    assert result.named["flow"] == 22
    assert result.named["to_valves"] == "GG"



def test_parse_input_line():
    line1 = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    line2 = "Valve HH has flow rate=22; tunnel leads to valve GG"

    valve_AA = parse_input_line(line1)
    assert valve_AA.name == "AA"
    assert valve_AA.flow == 0
    assert valve_AA.neighbours == ["DD", "II", "BB"]

    valve_HH = parse_input_line(line2)
    assert valve_HH.name == "HH"
    assert valve_HH.flow == 22
    assert valve_HH.neighbours == ["GG"]
