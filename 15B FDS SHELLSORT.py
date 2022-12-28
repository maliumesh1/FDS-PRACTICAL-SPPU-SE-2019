#fdsSHELLSORTtop5ok
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)

d=size//2
while d>0:
    for i in range (d,size):
        t=a[i]
        j=i 
        while(j >= d and a[j-d] > t):
            a[j]=a[j-d]
            j-=d
        a[j]=t
    d=d//2
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
