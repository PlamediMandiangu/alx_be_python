# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."

