from copy import deepcopy

import numpy as np

from leastSquare import *


class GSProcess:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrixShape = self.matrix.shape
        self.m = self.matrixShape[0]
        self.n = self.matrixShape[1]
        self.steps = self.n

    def process(self):
        Xi = np.array(deepcopy(self.matrix.T))
        Vi = np.zeros((self.n, self.m))
        Vi[0] = Xi[0]
        for i in range(1, self.steps):
            xi = Xi[i]
            process = self.sumV(xi, Vi, i)
            final = xi + process
            Vi[i] = final
        Wi = self.getW(Vi)
        qr = self.QR(Wi)
        return qr

    def sumV(self, Xn, v, step):
        initialCompute = 0
        finalCompute = 0
        for i in range(step):
            numerator = np.dot(Xn, v[i])
            denominator = np.linalg.norm(v[i]) ** 2
            initialCompute = np.dot(numerator / denominator, v[i])
            finalCompute = finalCompute - initialCompute
        return finalCompute


    def getW(self, Vi):
        Wi = np.zeros((self.n, self.m))
        for i in range(self.steps):
            Wi[i] = Vi[i] / np.linalg.norm(Vi[i])
        return Wi

    def QR(self, Wi):
        Q = Wi.T
        R = np.dot(Q.T, self.matrix)
        return Q, R

class AXb:
    def __init__(self, matrix, vectorB):
        self.matrix = matrix.T
        self.vectorB = vectorB
        self.m = matrix.shape[0] - 1
        self.n = matrix.shape[1] - 1


    def getX(self):
        Q, R = GSProcess(matrix=self.matrix).process()
        bPrim = np.dot(Q.T, self.vectorB)
        X = np.zeros((self.n, 1))
        self.n = self.n - 1
        X[self.n, 0] = np.array([bPrim[self.n][0] / R[self.n, self.n]])
        Sum = 0
        for i in range(self.n - 1, -1, -1):
            for j in range(i + 1, self.n + 1):
                Sum = Sum + R[i, j] * X[j]
            X[i, 0] = np.array([(bPrim[i, 0] - Sum) / R[i, i]])
        return X



lst = np.array(
    [[0,1,-1,1],
     [1,1,-1,-1],
     [1,0,1,1]]
)
print(GSProcess(lst).process()[0])