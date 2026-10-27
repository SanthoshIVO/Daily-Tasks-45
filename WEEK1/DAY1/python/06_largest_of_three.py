def main() -> None:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))

    largest = max(first, second, third)
    print(f"The largest number is {largest}.")


if __name__ == "__main__":
    main()
