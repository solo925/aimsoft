def print_pattern():
    try:
        rows = int(input("Enter the number of rows: "))
        for i in range(1, rows + 1):
            print(str(i) * i)
    except ValueError:
        print("Please enter a valid integer.")

print_pattern()