# Ask the user to enter the size of the pattern (positive integer)
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to keep track of the current row
row = 0

# Use a while loop to iterate through each row of the square pattern
while row < size:
    # Use a for loop to print the asterisks for the current row
    for column in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after printing all asterisks in the row
    
    # Move to the next row
    row += 1
