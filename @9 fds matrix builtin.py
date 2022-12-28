import numpy
# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# using add() to add matrices
print("The element wise addition of matrix is : ")
print(numpy.add(x, y))

# using subtract() to subtract matrices
print("The element wise subtraction of matrix is : ")
print(numpy.subtract(x, y))

# using dot() to multiply matrices
print ("The product of matrices is : ")
print (numpy.dot(x,y))


# using "T" to transpose the matrix
print("The transpose of given matrix is : ")
print(x.T)
