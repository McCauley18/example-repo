# Basic arithmetic program with checks

# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition = num1 + num2
print("Addition:", addition)

# Subtraction
subtraction = num1 - num2
print("Subtraction:", subtraction)

# Multiplication
multiplication = num1 * num2
print("Multiplication:", multiplication)

# Division with a safety check
if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")
