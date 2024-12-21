# Step 1: Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task based on its priority and time sensitivity
match priority:
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




