
#BUBBLE SORT
size=int(input("Enter No of Total Students:"))
a=[]
for i in range (size):
    val=float(input("Enter percentage:"))
    a.append(val)

for i in range(size):
    for j in range (0,size-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
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