def LongestWord():	
	str= []
	n = int(input("How many words in the list?"))
	for word in range(0,n):
		element=input("Enter the Words :")
		str.append(element)

	max_len = len(str[0])
	temp = str[0]
	for word in str:
		if(len(word)>max_len):
			max_len = len(word)
			temp = word
	print("The word with maximum length is: ",temp)
	print ("its length = ",max_len)

def Frequency():
	str = input("Enter some string: ")
	dict = {}
	for i in str:
		keys = dict.keys()
		if i in keys:
			dict[i] += 1
		else:
			dict[i] = 1
	print(dict)
#Frequency()
def Palindrome():
	str = input("\n Enter some string: ")
	if(str == str[::-1]):
		print("\n The given string is palindrome")
	else:
		print("\n The given string is not palindrome")
#
def Find_Substr():
	str = input("\n Enter some statement: ")
	word = input("\n Enter the substring to be searched: ")
	for i in range(len(str) - len(word)+1):
		if (str[i:i+len(word)] == word):
			return i
	return 'Not Found'

def OccurWords():
	str = input("\n Enter some statement: ")
	counts = dict()
	words = str.split()
	for word in words:
		if word in counts:
			counts[word]+= 1
		else:
			counts[word] = 1
	print(counts)
print("\n Program for String operations")
while(True):
	print("\n 1. To display word with the longest length")
	print("\n 2. To determine the frequency of occurrence of particular character in the string")
	print("\n 3. To check whether given string is palindrome or not")
	print("\n 4. To display index of first appearance of the substring")
	print("\n 5. To count the occurrences of each word in a given string")
	print("\n Enter your choice")
	choice = int(input())
	if(choice == 1):
		LongestWord()
	elif(choice == 2):
		Frequency()
	elif(choice == 3):
		Palindrome()
	elif(choice == 4):
		print(Find_Substr())
	elif(choice == 5):
		OccurWords()
	else:
		print("Exitting")
		break