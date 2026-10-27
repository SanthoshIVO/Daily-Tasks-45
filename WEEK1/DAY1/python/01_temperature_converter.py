def main() -> None:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()
