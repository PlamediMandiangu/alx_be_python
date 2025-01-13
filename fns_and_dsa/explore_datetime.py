from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()  # Use datetime.now() to get current date and time
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # Format as specified
    print(f"Current date and time: {current_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user to enter the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_datetime = datetime.now()
        # Calculate the future date by adding the days
        future_date = current_datetime + timedelta(days=days_to_add)
        # Format the future date as "YYYY-MM-DD"
        future_date_str = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {future_date_str}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()


