# Calculator Project

A simple Python calculator including four typed functions: `add`, `subtract`, `multiply` and `divide`.

# Setup

1. Install uv. 
2. The project was created with `uv init calculator-project`.
3. Open the project folder in VS Code.

# Usage

Run the file from the project folder:

    uv run calculator.py

If everything works, it prints: `All 6 assertions passed.` 

choose an option from the menu, and add your desired set of numbers. choose number 5 to quit. 

# Tests

Six assertions are written next to the functions:

- Normal cases: add, subtract, multiply, divide
- Boundary case: multiplying by zero
- Invalid case: dividing by zero raises a `ValueError`

# Notes

`divide(a, b)` raises a `ValueError` when `b` is 0.