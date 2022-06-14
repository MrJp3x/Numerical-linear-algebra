from listMethods import *

class AQR:
    def __init__(self, matrix):
        self.matrix = matrix
        self.run()

    def run(self):
        return self.QR(self.matrix)

    def QR(self, matrix):
        matrixLength = matrix.shape
        NewA = matrix
        s = min(matrixLength[0] - 1, matrixLength[1])
        arr = [[] for _ in range(s)]
        for i in range(s):
            W = self.getWVector(NewA, i + 1)
            al = self.alpha(W)
            E = self.e(W)
            V = self.getV(W, al, E)
            HH = self.houseHolder(V)
            NewA = np.dot(HH, NewA)
            arr[i] = HH
        R = NewA
        Q = np.dot(arr[0], arr[1])
        for i in range(2, s):
            Q = np.dot(Q, arr[i])
        return Q, R

    def getVector(self, matrix, column):
        lst = []
        if column < matrix.shape[1]:
            for i in matrix:
                lst.append(i[column])
                continue
            return np.array(lst)
        else:
            return False

    def getWVector(self, Matrix, step):
        matrixLength = np.shape(Matrix)
        if step <= 0:
            raise ValueError('Steps must be greater than 0')
        elif step >= matrixLength[0]:
            raise ValueError('The number of steps in the getWVertex function is large')
        elif step < matrixLength[0]:
            emptyVertex = getEmptyMatrix(matrixLength[0])
            for i in range(step - 1):
                emptyVertex[i].append(0)
            for i in range(step - 1, matrixLength[0]):
                count = 0
                for newI in Matrix[i]:
                    if step - 1 == count:
                        emptyVertex[i].append(newI)
                        break
                    count += 1
            return np.array(emptyVertex)

    def e(self, w):
        lst = []
        flag = True
        for i in w:
            if (i[0] != 0) and (flag == True):
                lst.append([1])
                flag = False
            else:
                lst.append([0])
        return np.array(lst)

    def alpha(self, w):
        for i in w:
            if i[0] == 0:
                continue
            elif i[0] != 0:
                a = (-1 * (np.sign(i[0]))) * np.linalg.norm(w)
                return a

    def getV(self, W, Alpha, E):
        return W - (np.dot(Alpha, E))

    def houseHolder(self, v):
        length = v.shape
        return (np.eye(length[0])) - (2 * ((np.dot(v, v.T)) / np.dot(v.T, v)))


# ================ ..:: New ::.. ================


class LeastSquares:
    def __init__(self, Matrix, b):
        self.b = b
        self.Matrix = Matrix

    def process(self):
        Shapes = self.Matrix.shape
        m, n = Shapes[0], Shapes[1]
        if m < n:
            if len(self.b) == len(self.Matrix):
                return self.underDetermined(self.Matrix.T, self.b, m, n)
            else:
                raise ValueError('The length of the vector v is not equal to the number of rows in the matrix')
        else:
            if len(self.b) == len(self.Matrix):
                return self.overDetermined(self.Matrix, self.b, m, n)
            else:
                raise ValueError('The length of the vector v is not equal to the number of rows in the matrix')

    def overDetermined(self, matrix, b, m, n):
        Q, R = AQR(matrix).run()
        R1 = R[np.ix_(range(n), range(n))]
        Q1 = Q[np.ix_(range(m), range(n))]
        Q2 = Q[np.ix_(range(m), range(m - n + 1, m))]
        c = np.dot(Q1.T, b)
        d = np.dot(Q2.T, b)
        X = np.zeros((n, 1))
        n = n - 1
        X[n, 0] = np.array([c[n][0] / R1[n, n]])
        Sum = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                Sum = Sum + R1[i, j] * X[j]
            X[i, 0] = np.array([(c[i, 0] - Sum) / R1[i, i]])
        remaining = np.linalg.norm(d)
        return X, remaining

    def underDetermined(self, matrix, b, m, n):
        Qr = AQR(matrix).run()
        Q = Qr[0]
        R = Qr[1]
        R1 = R[np.ix_(range(m), range(m))]
        R1T = R1.T
        Q1 = Q[np.ix_(range(n), range(m))]
        y = [[b[0][0] / R1T[0, 0]]]
        Sum = 0
        for i in range(1, m):
            for j in range(0, i):
                Sum = R1T[i, j] * y[j][0]
            if R[i, i] == 0:
                raise ZeroDivisionError(f'Element ({i}) The matrix R is zero and does not define division')
            y.append([(b[i][0] - Sum) / R1T[i, i]])
        y = np.array(y)
        x = np.dot(Q1, y)
        return x

