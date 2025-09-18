
## 1. Getting Started

**Running the Application:**
Clone or download the repository.
Open a terminal in the project directory.
Run the application: todoapp.py

# 2. Python To-Do Application

A simple, interactive command-line to-do list application written in Python. This app allows users to add, view, and delete tasks, with each task supporting categories (Work/Personal) and priority levels (High/Medium/Low). The interface uses color formatting for a more engaging user experience.

This rest of this page explains how the application meets the project rubric and how to use each feature correctly:

## 3. Fully implements all required features
- **Add:** Use the `add` command, then enter a description, category (Work/Personal), and priority (High/Medium/Low). Invalid entries are handled with clear error messages and defaults.
- **View:** Use the `view` command to see all tasks, with their category and priority, in a color-formatted list.
- **Delete:** Use the `delete` command, then enter the number of the task to remove. Invalid numbers are handled with error messages.
- **Quit:** Use the `quit` command to exit the program gracefully.

## 4. Additional enhancements
- **Task categories and priorities:** Every task includes a category and priority, set when adding a task. These are displayed in the task list.
- **Color formatting:** I had to do my own digging on this - `colorama` library (install with `pip install colorama`) and then I added the FORE.color to each corresponding text output to increase usability. 

## 5. Examples

```
Would you like to add, view, delete, or quit the program?
Enter your choice: add
Enter the task description: Finish homework
Enter category (Work/Personal): Work
Enter priority (High/Medium/Low): High
Task "Finish homework" added to the list.

Would you like to add, view, delete, or quit the program?
Enter your choice: view
To-Do List:
1. wake up | Category: Personal | Priority: High
2. eat breakfast | Category: Personal | Priority: Medium
3. go to work | Category: Work | Priority: High
4. go to park | Category: Personal | Priority: Low
Operation completed successfully.

Would you like to add, view, delete, or quit the program?
Enter your choice: delete
To-Do List:
1. wake up | Category: Personal | Priority: High
2. eat breakfast | Category: Personal | Priority: Medium
3. go to work | Category: Work | Priority: High
4. go to park | Category: Personal | Priority: Low
Enter the number of the task to delete: 3
Task "go to work" removed from the list.
Operation completed successfully.

Would you like to add, view, delete, or quit the program?
Enter your choice: quit
Exiting the program. Goodbye!
Thank you for using the To-Do Application.

```

## 6. Code Structure & Organization

- `add_item(todo_list)`: Adds a new task with description, category, and priority.
- `view_items(todo_list)`: Displays all tasks with details.
- `delete_item(todo_list)`: Removes a task by its number.
- Main: Handles user interaction and calls the appropriate function.
- Functions are modular, with clear variable names and comments for easy maintenance and upgrades.

## 7. Testing & Demo Instructions

- Run the program and try all commands (`add`, `view`, `delete`, `quit`).
- Try invalid inputs to see error handling in action.

## 8. Customization & Extensibility

- Easily extend the app to support more features, such as due dates, marking tasks as completed, or saving tasks to a file.
- The code is modular and well-commented for future improvements.

## Requirements Coverage

- All required features are implemented and tested.
- Code is modular, well-structured, and documented.
- Robust error handling for all edge cases.
- Added Color formatting, Priority Level, and Category as added features
- Ready for demo and further feedback.
