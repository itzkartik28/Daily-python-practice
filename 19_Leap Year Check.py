year=int(input("enter the year"))

if year %400==0:
    print("leap year!!")

elif year%100==0:
    print("not leap year")

elif year%4==0:
    print("laep year")

else:
    print("not a leap year")