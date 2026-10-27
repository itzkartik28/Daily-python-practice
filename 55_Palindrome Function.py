def palindrome(num):
    orignal=num
    reverse=0

    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10

    if orignal==reverse:
        print(orignal,"it is palindrome number")

    else:
        print(orignal,"it is not a palindrome number")

number=int(input("enter a number:"))
palindrome(number)
    