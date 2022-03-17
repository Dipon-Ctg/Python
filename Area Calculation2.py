#Circle,Sector, Square Mesurement

r=float(input("Enter Data(Radius/Length of side):"))
result= input ("Enter Types (S for Square/ C for Circle/ Se for Sector) : ")


if result =='S':
    S_area = r * r
    print(S_area)
if result =='C':
    C_area = 3.1416 * r * r
    print(C_area)
if result =='Se':
    e=float(input("Enter angle in radians: "))
    Se_area = 0.5 * r * r * e
    print(Se_area)





