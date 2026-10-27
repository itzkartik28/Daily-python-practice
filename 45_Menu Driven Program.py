print("1.tea")
print("2.coffee")
print("3.juice")

choice=int(input("enter your choice!!: "))

match choice:
    case 1:
        print("you selected tea")

    case 2:
        print("you selected coffee")

    case 3:
        print("you selected juice")

    case _:
        print("invalid choice!!")
