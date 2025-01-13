def perform_operation(num1, num2, operation):
    # Handle the 'add' operation
    if operation == 'add':
        return num1 + num2
    # Handle the 'subtract' operation
    elif operation == 'subtract':
        return num1 - num2
    # Handle the 'multiply' operation
    elif operation == 'multiply':
        return num1 * num2
    # Handle the 'divide' operation, including division by zero
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    # Handle invalid operation
    else:
        return "Invalid operation"
