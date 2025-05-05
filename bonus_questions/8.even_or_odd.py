def check_even_odd():
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        print("EVEN" if number % 2 == 0 else "ODD")
    else:
        print("Please enter a valid integer.")

check_even_odd()