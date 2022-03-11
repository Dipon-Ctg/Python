#Calculator

num1= int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
types=input("Enter types(+,-,*,/) :")

#Define
sum= num1+num2
minus=num1-num2
mul=num1*num2
div=num1/num2


if types== '+':
    print(sum)
if types=='-':
    print(minus)
if types== '*':
    print(mul)
if types=='/':
    print(div)
