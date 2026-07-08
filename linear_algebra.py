import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])

vector_sum = a + b 
vector_dif = a - b

print("Problem 1")
print(f"Sum of vectors: {vector_sum}")
print(f"Difference of vectors: {vector_dif}")
print("")

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

matrix_sum = A + B
matrix_dif = A - B

print("Problem 2")
print(f"Sum of matrices: {matrix_sum}")
print(f"Difference of vectors: {matrix_dif}")
print("")
