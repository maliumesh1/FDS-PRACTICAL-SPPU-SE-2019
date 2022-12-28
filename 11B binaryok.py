#fds group b 11b binary ok
def binary(a,key,size):
    i=0
    j=size-1
    flag=0
    
    while i<=j and flag==0:
        mid=(i+j)//2
        
        if a[mid]==key:         
            pos=mid+1
            flag=1
            
        if a[mid]<key:
            i=mid+1
            
        if a[mid]>key:
            j=mid-1
            
       
    if flag==1:
        print ("Student is present ")  
    else:
        print ("Student is absent ")
#main....................................
size=int(input("Total Students in the class:"))
a=[]
for i in range (size):
    val=int(input("Enter Roll No:"))
    a.append(val)
key=int(input("Enter Roll Number to be Search:    "))
binary(a,key,size)