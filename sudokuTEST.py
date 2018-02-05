import pytest
from sudoku import*

def testConvertToSets():
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    s = set(range(1, 10))
    assert[[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]] == convertToSets(ary)
    assert type(ary[0][0]) is int, "The original array has been changed."

def testConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    assert[[0, 3, 4], [1, 0, 2], [0, 2, 3]] == convertToInts(sets)
    assert type(sets[0][0]) is set, "The original array has been changed.")