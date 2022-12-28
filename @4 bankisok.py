b = 0
while True:
 str = input("Enter transaction: ")
 # seprated by space eg; D 300 for print N 000
 t = str.split(" ")
 
 type = t[0]
 a= int (t [1])
 # "D" for deposit, "W" for withdrawal 
 if (type=="D" or type=="d"):
    b+= a
 elif (type=="W" or type=="w"):
        if (b<a):
            print("Withdrawal is not possible")
        else:
            b -= a
 else:
     print("Exitting")
     break
print ("Total Balance: ",b)