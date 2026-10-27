username=input("enter the name:")
password=input("enter password")

if username=="student" and password=="python123":
    print("login suceessfully")

elif username=="student":
    print("incorecct password")

else:
    print("user not found")