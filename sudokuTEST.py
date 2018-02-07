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

def testGetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    assert(set(lst), set(getRowLocations(5)))

def testGetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    assert(set(lst), set(getColumnLocations(5)))

def testGetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    assert(set(lst), set(getBoxLocations((3, 2))))