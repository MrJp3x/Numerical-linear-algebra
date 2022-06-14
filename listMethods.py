from math import sqrt
import numpy as np


def getNorm2(vector):
    plusNumber = 0
    for var in vector:
        plusNumber += (var[0] ** 2)
    return sqrt(plusNumber)

def Transposed(matrix):  # pass
    """
    In this function, we first create an empty matrix to return.
    by 'getMatrixLength' function, we find the number of rows and columns of the input matrix.
    Then, the first loop makes the rows of the new matrix, and in the second loop
     which also has another loop, it has the task of placing the elements.
    :param matrix:
    :return:
    """
    def getEmptyTransposedMatrix(jLength):
        return [[] for _ in range(jLength)]

    lengthMatrix = getMatrixLength(matrix)
    newMatrix = getEmptyTransposedMatrix(lengthMatrix[1])
    for i in range(lengthMatrix[0]):
        for j in range(lengthMatrix[1]):
            newMatrix[j].append(matrix[i][j])
    return newMatrix

def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return None


def getEmptyMatrix(iLength):
    return [[] for _ in range(iLength)]

def getMatrixLength(matrix):
    iLength, jLength = len(matrix), 0
    for _ in matrix[0]:
        jLength += 1
    return iLength, jLength

