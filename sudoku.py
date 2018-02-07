#HAROON SHINWAR

def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem):
    for row in problem:
        for index, element in enumerate(row):
            if element == 0:
                row[index] = {1,2,3,4,5,6,7,8,9}
            else:
                row[index] = {element}
    return problem

def convertToInts(problem):
    for row in problem:
        for index, element in enumerate(row):
            if len(element) == 1:
                row[index] = (list(element)[0])
            else:
                row[index] = 0
    return problem

def getRowLocations(rowNumber):
    lst = [(rowNumber, 0), (rowNumber, 1), (rowNumber, 2), (rowNumber, 3),(rowNumber, 4), (rowNumber, 5), (rowNumber, 6), (rowNumber, 7), (rowNumber, 8)]
    return lst

def getColumnLocations(columnNumber):
    lst = [(0, columnNumber), (1, columnNumber), (2, columnNumber), (3, columnNumber),(4, columnNumber), (5, columnNumber), (6, columnNumber), (7, columnNumber), (8, columnNumber)]
    return lst