import numpy as np
# Создать простую матрицу

matrix = np.array([[1,2],
                   [2,3]])
print(matrix)
matrix2 = np.array([[2,3],
                    [3,4]])

print(matrix + matrix2)
print(matrix * matrix2)
print(matrix.T)
print(matrix2)
print(np.dor(matrix.T, matrix2))
