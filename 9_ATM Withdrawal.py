balance=5000
amount=int(input("enter the amount to withdraw:"))

if amount>balance:
    print("insuffieint balance")

elif amount % 100!=0:
    print("amount should be multiple by 100")

else:
    print("transation completed!!")