def print_pattern():
    rows = input("Enter the number of rows: ")
    if rows.isdigit():
        rows = int(rows)
        for i in range(1, rows + 1):
            print(str(i) * i)
    else:
        print("Please enter a valid integer.")

print_pattern()
