#CGPA to German Grade convertor

print("             ------Welcome to CGPA converter-------    \nThis Standard Grading Systems according to ZAB(Certral Office for Foreign Education)\n")
#Declaration
HM=float(input("Enter your Highest possible mark: "))
NM=float(input("Enter your Lowest pass mark:"))
GM=float(input("Enter your Obtain Grade:"))

#Define
result=(((HM-GM)/(HM-NM))*3)+1

#Output
print("\nYour German Grade CGPA is: ",result)
print("\n  Wish your higest success  ")
