
def Magic(s,size):
 for i in range(0,size):
    for j in range( 0,size):
        s[i][j] = 0
 nr = 0 #Top most row to start with */
 nc = Size // 2 # Compute middle of top row */
 s[nr][nc] = 1
 for i in range(2,(Size*Size)+1):
     Row = nr
     Col = nc
     nr=nr-1
     if (nr < 0 ):
         nr= Size - 1
     nc=nc-1
     if ( nc < 0 ):
        nc = Size - 1
     if ( s[nr][nc] != 0):
        nr = Row+1
        nc =Col
     s[nr][nc] = i
#driver code
print("Enter the size of the matrix ( No. of rows) :")
Size = int(input())
row =0
col =0
sq = [[0 for col in range(Size)]for row in range(Size)]
if ( Size % 2 == 0 ):
    print("Error, Number of rows/cols should be odd\n")
    print("Press any key to terminate")
    exit()
Magic(sq,Size)
print("\n Magic Square is ...")
for i in range(0,Size):
 for j in range( 0,Size): 
    print(sq[i][j],end =" ")
 print()
sum = 0
#displaying the sum
for j in range(0,Size): 
 sum =sum + sq[0][j]
 
print("\n Sum = ",sum)
