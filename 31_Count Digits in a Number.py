num=int(input("enter the numbers:"))

count=0

while num>0:
    count=count+1
    num=num//10

print("total digits in number:",count)