# Example data structure
tasks = []

# Example function for adding tasks
def add_task():
    task_name = input("Enter task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"task": task_name, "due_date": due_date})

# Example function for displaying tasks
def display_tasks():
    for task in tasks:
        print(f"{task['task']} - Due: {task['due_date']}")

# Example function for removing completed tasks
def remove_task():
    task_to_remove = input("Enter the task to mark as completed: ")
    tasks[:] = [task for task in tasks if task['task'] != task_to_remove]

# Example menu system
while True:
    print("\n1. Add Task\n2. Display Tasks\n3. Remove Completed Task\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        # Save to file before exiting
        with open('todo_list.txt', 'w') as file:
            for task in tasks:
                file.write(f"{task['task']} - Due: {task['due_date']}\n")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
