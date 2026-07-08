import numpy as np

# Problem 1
a = np.array([1,2,3])
b = np.array([4,5,6])

vector_sum = a + b 
vector_dif = a - b

print("Problem 1")
print("Sum of vectors:")
print(vector_sum)
print("Difference of vectors:")
print(vector_dif)
print("")


# Problem 2
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

matrix_sum = A + B
matrix_dif = A - B

print("Problem 2")
print("Sum of matrices:")
print(matrix_sum)
print("Difference of vectors:")
print(matrix_dif)
print("")

# Problem 3
# a and b are already properly defined from Problem 1

dot_product = np.dot(a, b)

print("Problem 3")
print("Dot product of vectors:")
print(dot_product)
print("")

# Problem 4
A2 = np.array([[1,2,3],[4,5,6]])
B2 = np.array([[7,8,9,10],[11,12,13,14],[15,16,17,18]])

matrix_product = np.dot(A2, B2)

print("Problem 4")
print("Product of matrices:")
print(matrix_product)
print("")

# Problem 5
a2 = np.array([1,1,2])

magnitude = np.linalg.norm(a2)

print("Problem 5")
print("Magnitude of vector:")
print(magnitude)
print("")

# Problem 6
# A is already properly defined from Problem 2

transpose = A.T

print("Problem 6")
print("Transposition of matrix:")
print(transpose)
print("")