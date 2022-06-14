import numpy as np
from gramSchmidt import *


lst = [[1,1],
       [1,2],
       [1,3],
       [1,4]]


b = [[1],
     [3],
     [-1],
     [0]]

Matrix = np.array(lst)

hh = LeastSquares(Matrix, b).process()
print(hh[0])



# ================ ..::  Save ::.. ================

