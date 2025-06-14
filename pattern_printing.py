def print_lower_triangle(rows):
    print("\nPrinting Lower Triangular:")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

def print_upper_triangle(rows):
    print("\nPrinting Upper Triangular:")
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def print_pyramid(rows):
    print("\nPrinting Pyramid Pattern:")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def main():
    print("Choose which pattern you want to print:")
    print("1. Upper Triangular Pattern")
    print("2. Lower Triangular Pattern")
    print("3. Pyramid Pattern")

    choice = int(input("Enter your choice (1/2/3): "))
    rows = int(input("Enter number of rows: "))

    if choice == 1:
        print_upper_triangle(rows)
    elif choice == 2:
        print_lower_triangle(rows)
    elif choice == 3:
        print_pyramid(rows)
    else:
        print("Oops Invalid choice!!! Please enter 1, 2, or 3.")

main()
