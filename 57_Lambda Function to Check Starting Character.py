starts_with=lambda text,ch:text.startswith(ch)

string=input("enter a string:")
character=input("enter a character:")

if starts_with(string,character):
    print("the string start with",character)

else:
    print("the string does not start with ",character)