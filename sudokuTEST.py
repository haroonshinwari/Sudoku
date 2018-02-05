import pytest
from sudoku import*

def testConvertToSets():
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    s = set(range(1, 10))
    assert[[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]] == convertToSets(ary)
    assert type(ary[0][0]) is int, "The original array has been changed."