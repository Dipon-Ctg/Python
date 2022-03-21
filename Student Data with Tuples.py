students = (
    ("Dipon Barua \nEmail-abc@gmail.com.\nMobile:123456\nDepartment-EEE"),
    ("Dipta Barua \nEmail-dc@gmail.com.\nMobile:156496\nDepartment-ECE"),
    ("Afrah Islam \nEmail-ert@gmail.com.\nMobile:896496\nDepartment-CSE"),

)
print("------Welcome To Student Server------")
n = int(input("Enter Registered Matriculation Number:"))

if n == 101:
    print(students[0])
elif n == 102:
    print(students[1])
elif n == 103:
    print(students[2])
else:
    print("Your are not Registered yet")