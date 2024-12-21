# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match Case for task priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level"

#HEAD
# Step 3: Print the final reminder message with the correct format
print(reminder_message)


# Check if the task is time-bound and update reminder
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound.lower() == "no":
    reminder += " Consider completing it when you have free time."

# Print the final reminder
print(reminder)

