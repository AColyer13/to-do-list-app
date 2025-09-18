# Color formatting setup
from colorama import init, Fore, Style
init(autoreset=True)

# Initialize the to-do list with some default tasks (each task is a dict)
todo_list = [
    {"description": "wake up", "category": "Personal", "priority": "High"},
    {"description": "eat breakfast", "category": "Personal", "priority": "Medium"},
    {"description": "go to work", "category": "Work", "priority": "High"}
]

# Function to add an item to the to-do list
def add_item(todo_list):
    desc = input(Fore.CYAN + "Enter the task description: ").strip()
    if not desc:
        print(Fore.RED + "Invalid input. Description cannot be empty.")
        return
    while True:
        category = input(Fore.CYAN + "Enter category (Work/Personal): ").strip().capitalize()
        if category in ["Work", "Personal"]:
            break
        print(Fore.RED + "Invalid category. Please enter 'Work' or 'Personal'.")
    while True:
        priority = input(Fore.CYAN + "Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print(Fore.RED + "Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

    todo_list.append({
        "description": desc,
        "category": category,
        "priority": priority
    })
    print(Fore.GREEN + f'Task "{desc}" added to the list.')

# Function to display all items in the to-do list
def view_items(todo_list):
    if todo_list:
        print(Fore.MAGENTA + "To-Do List:")
        idx = 1
        for item in todo_list:
            print(Fore.WHITE + f"{idx}. {item['description']} | Category: {item['category']} | Priority: {item['priority']}")
            idx += 1
    else:
        print(Fore.YELLOW + "The to-do list is empty.")

# Function to delete an item from the to-do list
def delete_item(todo_list):
    if not todo_list:
        print(Fore.YELLOW + "No items to delete.")
    else:
        view_items(todo_list)
        while True:
            try:
                num = input(Fore.CYAN + "Enter the number of the task to delete: ").strip()
                if not num.isdigit() or int(num) < 1 or int(num) > len(todo_list):
                    print(Fore.RED + "Invalid number. Please try again.")
                    print("")
                    continue
                num = int(num)
                removed = todo_list.pop(num-1)
                print(Fore.GREEN + f'Task "{removed["description"]}" removed from the list.')
                break
            except:
                print(Fore.RED + "An error occurred while deleting. Please try again.")

# Main: repeatedly prompt the user for actions until they choose to quit
while True:
    try:
        print(Fore.CYAN + Style.BRIGHT + "Would you like to add, view, delete, or quit the program?")
        user_input = input(Fore.WHITE + "Enter your choice: ").strip().lower()
        success = False
        # Call the appropriate function based on user input
        if user_input == "add":
            add_item(todo_list)
            success = True
        elif user_input == "view":
            view_items(todo_list)
            success = True
        elif user_input == "delete":
            delete_item(todo_list)
            success = True
        elif user_input == "quit":
            print(Fore.GREEN + "Exiting, Thank you for using the To-Do Application.")
            print(Fore.YELLOW + "Operation completed successfully.")
            break
        else:
            print(Fore.RED + "Invalid option. Please select add, view, delete, or quit.")
            print("")
    except:
        print(Fore.RED + "An error occurred.")
        print(Fore.RED + "Please try again.")
    else:
        if success:
            print(Fore.YELLOW + "Operation completed successfully.")
            print("")


