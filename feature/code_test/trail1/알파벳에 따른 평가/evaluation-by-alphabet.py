grade=input()

match grade:
    case "S":
        print("Superior")
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Usually")
    case "D":
        print("Effort")
    case _:
        print("Failure")