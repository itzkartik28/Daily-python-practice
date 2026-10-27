grade=input("enter a grade:")

match grade:

    case "a":
        print("exllent")

    case "b":
        print("very good")

    case "c":
        print("good")

    case"d":
        print("pass")

    case _:
        print("invalid grade!!")
        
