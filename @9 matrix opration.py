rownum=int(input("Enter Number of Rows:"))
colnum=int(input("Enter Number of column:"))

A = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
	for col in range(colnum):
		item = int(input("Enter the elements in first matrix: "))
		A[row][col]= item
print("The first matrix is...")
print(A)
			   			   
B= [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
	for col in range(colnum):
		item = int(input("Enter the elements in Second matrix: "))
		B[row][col]= item
print("The Second matrix is...")
print(B)

def add(A,B):
	result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
	print("The Addition of Two Matrices...")
	for r in result: 
		print(r)
add(A,B)
#subtraction of two matrices
def sub(A,B):
	result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
	print("The Substraction of Two Matrices...")
	for r in result: 
		print(r)
sub(A,B)

#transpose of matrix
def trans(A):
 	result = [[0 for col in range(colnum)] for row in range(rownum)]
 	for i in range(len(A)): 
 		for j in range(len(A[0])): 
 			result[j][i] = A[i][j]
 	print("Transpose Matrix is")
 	for r  in result:
 		print(r)
trans(A)
			
def mul(A,B):
	result = [[0 for col in range(colnum)] for row in range(rownum)]

	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
			   	result[i][j] += A[i][k] * B[k][j]
	print("Matrix Multiplication is ...")
	for r in result:
		print(r)
mul(A,B)
		

    	