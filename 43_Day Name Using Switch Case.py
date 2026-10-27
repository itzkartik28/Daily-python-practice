day=int(input("enter number of days(1-7):"))

match day:

    case 1:
        print("monday")

    case 2:
        print("tuesday")

    case 3:
        print("wes")

    case 4:
        print("turs")

    case 5:
        print("fri")

    case 6:
        print("satu")

    case 7:
        print("sunday")

    case _:
        print("invalid day/choice")