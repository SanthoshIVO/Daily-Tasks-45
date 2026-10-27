# Python Exercises

Ten beginner exercises are provided as separate programs:

1. `01_temperature_converter.py` - convert Celsius to Fahrenheit.
2. `02_simple_calculator.py` - add, subtract, multiply, or divide two numbers.
3. `03_number_patterns.py` - print star and number patterns.
4. `04_grade_calculator.py` - assign a grade with `if`/`elif`/`else`.
5. `05_even_or_odd.py` - check whether an integer is even.
6. `06_largest_of_three.py` - find the largest of three numbers.
7. `07_multiplication_table.py` - print a multiplication table.
8. `08_factorial.py` - calculate a factorial using a loop.
9. `09_prime_checker.py` - check whether an integer is prime.
10. `10_sum_and_average.py` - calculate the sum and average of comma-separated numbers.

## Requirements

- Python 3.11 or newer.
- Visual Studio Code with Microsoft's **Python** extension.
- No extra Python packages are needed; these exercises use the standard library only.

## Virtual environment

The workspace Python environment is configured at `E:\Ivoyant\.venv` and uses Python 3.14.5, which meets the Python 3.11+ requirement. In a new PowerShell terminal, activate it and verify the interpreter:

```powershell
cd E:\Ivoyant
.\.venv\Scripts\Activate.ps1
python --version
```

In VS Code, install Microsoft's **Python** extension (and **Pylance** for language support), open the Command Palette with `Ctrl+Shift+P`, choose **Python: Select Interpreter**, and select `E:\Ivoyant\.venv\Scripts\python.exe`.

If you need to create a separate environment, first install Python 3.11 or newer, then from the repository root run:

```powershell
py -3 -m venv .python-env
.\.python-env\Scripts\Activate.ps1
python --version
```

Confirm that the reported version is 3.11 or newer. The environment is isolated; these exercises do not require a `pip install` step.

## Run an exercise

With the environment activated:

```powershell
cd E:\Ivoyant\WEEK1\DAY1\python
python .\01_temperature_converter.py
```

Replace the filename with any of the other numbered `.py` files to run that exercise. Enter the requested values in the terminal.
