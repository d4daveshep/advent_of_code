from day_4 import Section


def test_section():
    section = Section("2-4")
    assert section.start == 2
    assert section.end == 4


def test_section_contains_section():
    assert not Section("2-4").contains(Section("6-8"))
    assert not Section("6-8").contains(Section("2-4"))

    assert not Section("2-3").contains(Section("4-5"))
    assert not Section("4-5").contains(Section("2-3"))

    assert not Section("5-7").contains(Section("7-9"))
    assert not Section("7-9").contains(Section("5-7"))

    assert Section("2-8").contains(Section("3-7"))
    assert not Section("3-7").contains(Section("2-8"))

    assert not Section("6-6").contains(Section("4-6"))
    assert Section("4-6").contains(Section("6-6"))

    assert not Section("2-6").contains(Section("4-8"))
    assert not Section("4-8").contains(Section("2-6"))


def test_section_overlaps_section():
    assert not Section("2-4").overlaps(Section("6-8"))

    assert not Section("2-3").overlaps(Section("4-5"))

    assert Section("5-7").overlaps(Section("7-9"))

    assert Section("2-8").overlaps(Section("3-7"))

    assert Section("6-6").overlaps(Section("4-6"))

    assert Section("2-6").overlaps(Section("4-8"))
