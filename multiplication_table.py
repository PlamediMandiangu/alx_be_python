# multiplication_table.py

# Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):  # Loop through numbers 1 to 10
    result = number * i  # Calculate the product
    print(f"{number} * {i} = {result}")  # Print the multiplication
