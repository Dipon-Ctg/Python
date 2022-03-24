#Declaraion

numOfLetters=0
numOfDigits=0
numOfWords=0

#input
n=input("Enter your Dialogue or text (in one line): ")

#define
for list in n:
    if list>='a' and list<='z':
        list= list.lower()
        numOfLetters=numOfLetters+1
    elif list>='0' and list<='9':
        numOfDigits=int(numOfDigits+1)
    elif list==' ':
        numOfWords=numOfWords+1
#output
print("Number of Leter in this text is: ",numOfLetters)
print("Number of Digit in this text is: ",numOfDigits)
print("Number of Words in this text is: ",numOfWords+1)

