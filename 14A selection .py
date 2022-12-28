#SELECTION SORT
marks=int(input("Enter Total No Of Students:"))
a=[]
for i in range (marks):
    val=float(input("Enter Percentage:"))
    a.append(val)

for i in range(marks):
    min=i #first element consider min
    for j in range (i+1,):#i+1,continue with end of size
        if (a[j]<a[min]):# <  main'
            min=j    #min j
            t=a[i]    
            a[i]=a[min] 
            a[min]=t   
print("Sorted list is :")

for i in range(len(a)-1, -1, -1):     
    print(a[i])
