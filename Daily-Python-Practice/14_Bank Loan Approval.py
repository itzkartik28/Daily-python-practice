salary=int(input("enter the salary:"))
cibil=int(input("enter the cibil score:"))

if salary>=25000 and cibil>=750:
    print("loan approved")

elif salary<25000:
    print("loan not approved-low salary")

else :
    print("loan not approved-low cibil score")