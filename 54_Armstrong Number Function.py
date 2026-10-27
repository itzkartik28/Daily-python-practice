def armstrong(num):
    temp=num
    digits=len(str(digit))
    total=0

    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10


    if total==num:
     print(num,"it is armstrong number")

    else:
     print(num,"it is not a armstrong number")
     
     
     

number=int(input("enter a number"))
armstrong(number)