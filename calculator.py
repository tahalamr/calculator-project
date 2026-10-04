def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


assert add(2, 3) == 5


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


assert subtract(10, 4) == 6


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


assert multiply(3, 4) == 12
assert multiply(5, 0) == 0  # boundary: multiplying by zero


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


assert divide(10, 4) == 2.5

# invalid case: dividing by zero must raise an error
error_raised = False
try:
    divide(1, 0)
except ValueError:
    error_raised = True
assert error_raised

print("All 6 assertions passed.")

while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter 1-5: ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    else:
        try:
            print("Result:", divide(a, b))
        except ValueError as error:
            print(error)
