age=int(input("enter age:"))
fitness=input("fitness passed (yes/no):")

if age<=25 and fitness=="yes":
    print("selected")

elif age>25:
    print("not selected-age limit extended")

else:
    print("not selected-fitness failed")