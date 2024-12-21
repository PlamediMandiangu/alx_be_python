# daily_reminder.py

# Step 1: Ask user for task description
task = input("Enter your task: ")

# Step 2: Ask user for priority level
priority = input("Priority (high/medium/low): ").lower()

# Step 3: Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 4: Process task and provide reminder based on priority and time sensitivity

# Use match-case for priority
match priority:
<<<<<<< HEAD
    case 'high':
        priority_message = "high priority task"
    case 'medium':
        priority_message = "medium priority task"
    case 'low':
        priority_message = "low priority task"
    case _:
        priority_message = "unknown priority level"

# If the task is time-bound, modify the reminder message
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

# Step 5: Output the reminder message
print(reminder)  # This print statement should work

=======
    case "high":
        Reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            Reminder += " that requires immediate attention today!"
        else:
            Reminder += ". It is important, but not time-bound."
    case "medium":
        Reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            Reminder += " that requires attention today."
        else:
            Reminder += ". It can be handled later today."
    case "low":
        Reminder = f"Reminder: '{task}' is a low priority task"
        if time_bound == "yes":
            Reminder += " but it is time-sensitive, so consider completing it soon."
        else:
            Reminder += ". Consider completing it when you have free time."
    case _:
        #reminder_message = "Sorry, I don't recognize that priority level. Please choose 'high', 'medium', or 'low'."
         Reminder: 'Finish project report'

# Step 3: Print the final reminder message
print(Reminder)
>>>>>>> af2f5dd6506371e7d3295fe3b89341252f84297e




