num=int(input("enter a number:"))
sum=0

while num>0:
    digit=num%10
    sum=digit+sum
    num=num//10

print(f"sum of digits :{sum}")