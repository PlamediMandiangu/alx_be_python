# match_case_calculator.py

# Prompt the user for the first number
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Ask for the type of operation they would like to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation"

# Output the result
#print("Result:", result)
print("The result is", result)
