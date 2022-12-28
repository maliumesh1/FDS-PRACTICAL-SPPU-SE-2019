marksinFDS=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    marksinFDS.append(marks)
print(".................program.....................")
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("\n\nTotal Marks : ", sum)
    print("\nAverage Marks : {:.2f}".format(avg))
average(marksinFDS)

def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)
print("\nMaximum Marks",Maximum(marksinFDS))

def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)
print("\nMinimum marks",Minimum(marksinFDS))

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
            count+=1
    return(count)
print("\nAbsent Student",absentcount(marksinFDS))

def maxFrequency(listofmarks):
    i=0
    Max=0
    print("\nMarks  |  Frequency")
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j,"    |  ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,Max)
#print(maxFrequency(marksinFDS))
mark,fr = maxFrequency(marksinFDS)
print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))

