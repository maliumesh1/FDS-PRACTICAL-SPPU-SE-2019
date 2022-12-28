
#INSERTION SORT👌💐
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=float(input("Enter No:"))
    a.append(val)

for i in range(1,size):
     t=a[i] #पहिला Element👍
     j=i-1 #पहिला-1,element👍
     while j>=0 and t<a[j]:# J हा 0 पेक्षा मोठा & पहिला
                         # element हा दुसऱ्यापेक्षा मोठा👌
        a[j+1]=a[j] #Swap
        j=j-1       #
        a[j+1]=t
print("Sorted list is :")
print(a)






    