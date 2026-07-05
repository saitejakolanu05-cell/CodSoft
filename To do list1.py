
tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. {task['name']} [{status}]")

    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")
            try:
                num = int(input("Enter task number to mark as completed: "))
                tasks[num - 1]["completed"] = True
                print("Task marked as completed.")
            except:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                print(f"Deleted task: {removed['name']}")
            except:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")
