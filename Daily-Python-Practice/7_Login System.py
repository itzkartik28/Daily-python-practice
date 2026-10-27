username=input("enter the username:")
password=int(input("enter the password:"))

if username=="admin" and password==1234:
    print("login sucessfully")

elif username =="admin":
    print("incorrect username")

else:
    print("failed to login!!")