def main() -> None:
    number = int(input("Enter an integer from 0 to 18: "))

    if number < 0 or number > 18:
        print("Enter a whole number from 0 to 18.")
        return

    factorial = 1
    for value in range(1, number + 1):
        factorial *= value

    print(f"{number}! = {factorial}")


if __name__ == "__main__":
    main()
