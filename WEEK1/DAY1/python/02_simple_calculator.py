def main() -> None:
    print("Simple Calculator")
    first = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()
    second = float(input("Enter the second number: "))

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unknown operation. Choose +, -, *, or /.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()