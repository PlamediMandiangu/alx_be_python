import datetime

def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    # Prompt the user to enter the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_datetime = datetime.datetime.now()
        # Calculate the future date by adding the days
        future_date = current_datetime + datetime.timedelta(days=days_to_add)
        # Format the future date as "YYYY-MM-DD"
        future_date_str = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {future_date_str}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()

