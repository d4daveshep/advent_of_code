import parse
import pytest

from day_16 import parse_input_line

@pytest.fixture()
def test_data():
    with open("./day_16_test_data.txt") as data_file:
        data = data_file.readlines()
    return data

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



def test_parse_test_data(test_data):
    valves = parse_data(test_data)
    valves = [parse_input_line(line) for line in test_data]
    assert len(valves) == 10
