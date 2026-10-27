amount=int(input("enter the purchase amount:"))

if amount>=5000:
    print("free shipping and 20% discount")

elif amount>=1000:
    print("free shiping")

else:
    print("shipping charges avalible")