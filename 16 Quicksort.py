#Quick sortfor fds practicals

def quick(a,low,high):   
    if(low<high):
        m=part(a,low,high)
        quick(a,low,m-1)
        quick(a,m+1,high)
def part(a,low,high):
    pivot=a[low]
    i=low+1
    j=high 
    flag=0
    while(not flag):
        while(i<=j and a[i]<=pivot):
            i=i+1
        while(i<=j and a[i]>=pivot):
            j=j-1
            
        if (j<i):
            flag=1
        else:
            t=a[i]
            a[i]=a[j]
            a[j]=t        
    t=a[low]
    a[low]=a[j]
    a[j]=t
    return j
    
size=int(input("Enter No of total Student:"))
a=[]
for i in range (size):
    val=float(input("Enter percentage:"))
    a.append(val)
    
quick(a,0,size-1)
print("Sorted list is :")
print(a)

def display_top_five(a):
    print("Top Five Percentages are : ")
    if len(a) < 5:
        start, stop = len(a) - 1, -1
    else:
        start, stop = len(a) - 1, len(a) - 6

    for i in range(start, stop, -1):
        print(a[i],sep = "\n")
display_top_five(a)