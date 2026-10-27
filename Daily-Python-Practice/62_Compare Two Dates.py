from datetime import datetime

date1=input("enter first date dd/mm/yyyy":)
date2=input("enter secound date dd/mm/yyyy":)

d1=datetime.strptime(date1,"%d%m%y")
d2=datetime.strptime(date2,"%d%m%y")

if d1<d2:
    print("first date is eailer")

elif d2<d2:
    print("secound date is eailer")

else:
    print("both date are same")