#Triangle,Rectangle,Parallelogram Mesurement

a=float(input("Enter Data(Base/width):"))
b=float(input("Enter Data(height/width):"))
result= input ("Enter Types (T For Tringle/ R for rectangle/ P for Parallelogram) : ")

#Equation

T_area= 0.5*a*b
R_area= a*b
P_area=a*b

if result =='T':
    print(T_area)
if result =='R':
    print(R_area)
if result =='P':
    print(P_area)