#linear search and sentinel searchfds pr ok 11a
def linear(a,key,size):
    flag=0
    for i in range (size):
        if a[i]==key:
            flag=1
            pos=i+1
            break
    if flag==1:
        print("Student is present at",pos,"Postion")
    else:
        print("Number Not found")

def sentinelSearch(a, size, key):
    last = a[size - 1]
    a[size - 1] = key
    i = 0
    while (a[i] != key):
        i += 1
    a[size- 1] = last 
    if ((i < size - 1) or (a[size - 1] == key)):
        print('''key''', "Student is present at position", i+1)
    else:
        print("Student is Absent")
#main.....................................
size=int(input("Total Students in Class:"))
a=[]
for i in range (size):
    val=int(input("Enter Roll No:"))
    a.append(val)
print(a)
key=int(input("Enter Roll No to be search :"))


print("\nThis is linear Search")
linear(a,key,size)

print("\nThis is Sentinel Search")
sentinelSearch(a, size, key)