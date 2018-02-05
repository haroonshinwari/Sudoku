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


