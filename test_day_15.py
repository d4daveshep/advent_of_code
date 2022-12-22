import parse
import pytest

def test_parse_input_line():
    line = "Sensor at x=9, y=16: closest beacon is at x=10, y=16"
    result = parse.search("Sensor at x={x_s:d}, y={y_s:d}: closest beacon is at x={x_b:d}, y={y_b:d}",line)
    # result = {k[int(v)] for k,v in result.items()}
    print(result.named)

