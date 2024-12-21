# Step 1: Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task based on its priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". It is important, but not time-bound."
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder_message += " that requires attention today."
        else:
            reminder_message += ". It can be handled later today."
    case "low":
        reminder_message = f"Reminder: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder_message += " but it is time-sensitive, so consider completing it soon."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _:
        reminder_message = "Sorry, I don't recognize that priority level. Please choose 'high', 'medium', or 'low'."

# Step 3: Print the final reminder message
print(reminder_message)


