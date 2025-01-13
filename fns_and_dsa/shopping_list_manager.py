def display_menu():
    # Display the menu options to the user
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the shopping list as an empty list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == '3':
            # View the shopping list
            if shopping_list:
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
