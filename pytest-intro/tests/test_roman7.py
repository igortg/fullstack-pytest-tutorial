from roman7 import to_roman, from_roman


def test_roman_conversion():
    assert to_roman(3) == 'III'
    assert from_roman('IV') == 4
