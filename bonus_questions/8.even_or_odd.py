def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print("EVEN")
        else:
            print("ODD")
    except ValueError:
        print("Please enter a valid integer.")

check_even_odd()