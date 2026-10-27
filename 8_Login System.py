age=int(input("enter age:"))
citizen=input("you are an a indian citizen (yes/no):")

if age>=18 and citizen=="yes":
    print("your are now eligible for voting")

elif age<18:
    print("not eligible - age under 18")

else:
    print("not eligible- not a indian")