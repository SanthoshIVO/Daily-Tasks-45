def main() -> None:
    entry = input("Enter numbers separated by commas: ")
    if not entry.strip():
        print("Enter at least one number.")
        return

    try:
        numbers = [float(value.strip()) for value in entry.split(",")]
    except ValueError:
        print("Enter valid numbers separated by commas.")
        return

    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
