def main() -> None:
    number = int(input("Enter an integer: "))

    if number < 2:
        print(f"{number} is not a prime number.")
        return

    is_prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


if __name__ == "__main__":
    main()
