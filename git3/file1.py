todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '2':
        if not todo_list:
            print("No tasks.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
    elif choice == '3':
        if not todo_list:
            print("No tasks to delete.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

