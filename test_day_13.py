def parse_packet(packet_str:str)->list:
    # r = repr(packet_str)
    l = eval(packet_str)
    return l


def test_create_list_from_string():
    packet_str = "[1,1,3,1,1]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [1, 1, 3, 1, 1]

    packet_str = "[[1],[2,3,4]]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[1],[2,3,4]]
    pass

    packet_str = "[[[]]]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[[]]]

    packet_str = "[[4,4],4,4,4]"
    packet_list = parse_packet(packet_str)
    assert packet_list == [[4,4],4,4,4]


