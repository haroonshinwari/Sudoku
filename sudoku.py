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

def getBoxLocations(location):
    if location[0] == 0 or location[0] == 1 or location[0] == 2:
        if location[1] == 0 or location[1] == 1 or location[1] == 2:
            lst = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        elif location[1] == 3 or location[0] == 4 or location == 5:
            lst = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
        else:
            lst = [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]

    elif location[0] == 3 or location[0] == 4 or location[0] == 5:
        if location[1] == 0 or location[1] == 1 or location[1] == 2:
            lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
        elif location[1] == 3 or location[1] == 4 or location[1] == 5:
            lst = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        else:
            lst = [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]

    else:
        if location[1] == 0 or location[1] == 1 or location[1] == 2:
            lst = [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
        elif location[1] == 3 or location[1] == 4 or location[1] == 5:
            lst = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
        else:
            lst = [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    return lst

def eliminate(problem, location, listOfLocations):
    eliminate_count = 0
    convertToSets(problem)
    if len(problem[location[0]][location[1]]) == 1:
        x = problem[location[0]][location[1]]
        x = list(x)
        x = x[0]
        listOfLocations.remove(location)
        print(x)
        for element in listOfLocations:
            if x in problem[element[0]][element[1]]:
                problem[element[0]][element[1]].remove(x)
                eliminate_count += 1
                print(problem[element[0]][element[1]])
    return eliminate_count