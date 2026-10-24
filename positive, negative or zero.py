while True:
    num = float(input("Enter your number: "))
    if num < 0:
        print("Your number is negative")
    elif num > 0:
        print("Your number is positive")
    else:
        print("Your number is zero")

    check_again = (input("Want to check for another number (y/n) : "))
    if check_again != "y":
        print("Thank you for using this program")
        break