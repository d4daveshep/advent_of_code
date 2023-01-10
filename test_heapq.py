import heapq

import pytest

class Valve_2:
    def __init__(self, name, flow=0):
        self.name = name
        self.flow = flow

    def __lt__(self, other):
        return self.flow < other.flow

    def __repr__(self):
        return f"Valve(name={self.name}, flow={self.flow})"


def test_sort_list_of_valves():
    v1 = Valve_2("A", 10)
    v2 = Valve_2("B", 30)
    v3 = Valve_2("C", 20)

    assert v1 < v2

    valves = [v3, v2, v1]
    heapq.heapify(valves)

    priority_valves = []

    heapq.heappush(priority_valves, v3)
    heapq.heappush(priority_valves, v2)
    heapq.heappush(priority_valves, v1)

    assert heapq.heappop(priority_valves) == v1
    assert heapq.heappop(priority_valves) == v3
    assert heapq.heappop(priority_valves) == v2

    pass