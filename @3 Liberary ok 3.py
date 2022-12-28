def firs(Books,N):
    for i in range (N):
        for j in range(i+1,N):
            if(Books[i][1]>Books[j][1]):
                temp1=Books[i][0]
                Books[i][0]=Books[j][0]
                Books[j][0]=temp1
                
                temp2=Books[i][1]
                Books[i][1]=Books[j][1]
                Books[j][1]=temp2
        print ("the Books are...")
        print(Books)
        
def deleteduplicate(Books):
    finalbooks=[]
    for num in Books:
        if num not in finalbooks:
            finalbooks.append(num)
    print("Remove Duplicate");
    print(finalbooks)
    
def MoreCost(Books,N):
    cnt=0
    for isbn in range(N):
        if(Books[isbn][1]>500):
            cnt=cnt+1
    print("Books cost>500",cnt)
    
def LessCost(Books,N):
    cnt=0
    for isbn in range(N):
        if(Books[isbn][1]<500):
            cnt=cnt+1
    new=[[ 0 for cost in range(2)]for isbn in range(cnt)]
    for isbn in range(N):
        new[isbn][0] = Books[isbn][0]
        new[isbn][1] = Books[isbn][1]
    print("\n books having the cost less than 500 are");
    print("\n isbn\t Cost");
    for isbn in range(cnt):
        print("",new[isbn][0],"\t",new[isbn][1])
       
N=int(input("input No of books:"))
Books=[[ 0 for cost in range(2)]for isbn in range(N)]
for isbn in range(N):
    ISBN=int(input("Enter the isbn :"))
    Books[isbn][0]=ISBN
    COST=int(input("Enter the Cost :"))
    Books[isbn][1]=COST
print("The Books are...")
print(Books)
while(True):
    print("\n\t Library")
    print("\n 1.Delete Duplicate Entries")
    print("\n 2.Display Books ascending order on Costwise")
    print("\n 3.Display no of books with cost more than 500")
    print("\n 4.Display no of books with cost less than 500")
    print("\n Enter your choice")
    choice=int(input())
    if(choice == 1):
        deleteduplicate(Books)
    elif(choice==2):
        firs(Books,N)
        #Sorting(Books,N)
    elif(choice==3):
        MoreCost(Books,N)
    elif(choice==4):
        LessCost(Books,N)
    else:
        print("Exit")
        break
        
        