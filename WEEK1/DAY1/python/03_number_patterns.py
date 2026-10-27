def main() -> None:
    rows = int(input("Enter the number of rows: "))

    if rows < 1:
        print("Please enter a positive number of rows.")
        return

    print("\nStar pattern:")
    for row in range(1, rows + 1):
        print("* " * row)

    print("\nNumber pattern:")
    for row in range(1, rows + 1):
        numbers = " ".join(str(number) for number in range(1, row + 1))
        print(numbers)


if __name__ == "__main__":
    main()
