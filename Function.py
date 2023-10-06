def addition(a,b): #define function
    add=a+b
    print(add)
#addition(int(input('Enter 1st:')),int(input('Enter 2nd:'))). Easy way but have to put value from system not from users.
def substraction(c,d):
    sub=c-d
    print(sub)

def Multiplication(f,g):
    mul=f*g
    print(mul)

def Division(l,k):
    div=l/k
    print(div)
print('Hey! Welcome too easy calculator with using function.\n Currently it is avaible for two values.')

#condition=[str(input('Enter yes:')),]
#for i in condition:
#if i == 'yes':
e= int(input('Type 1 for Addition. Type 2 for Substraction. Type 3 for Multiplication. Type 4 for Division :'))
#i=1
#while i<10:
if e==1:
    addition(int(input('Enter 1st value for addition:')), int(input('Enter 2nd value for addition:')))
    #a=int(input('Enter 1st value:'))
    #b=int(input('Enter 2nd value:'))
    #addition()
elif e==2:
    substraction(int(input('Enter 1st value for substraction:')), int(input('Enter 2nd value for substraction:')))
 #   c=int(input('Enter 1st value:'))
 #   d=int(input('Enter 2nd value:'))
  #  print(substraction())

elif e==3:
    Multiplication(int(input('Enter 1st value for multiplication:')),int(input('Enter 2nd value for multiplication:')))
elif e==4:
    Division(int(input('Enter 1st value for division:')),int(input('Enter 2nd value for division:')))
else:
    print('Sorry! You are selected a unknown value')
    #if i == 'no':
     #   break