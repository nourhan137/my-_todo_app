# My To-Do List App
tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            num = int(input("Task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Removed: {removed}")

    elif choice == "4":
        print("Bye! Good job today!")
        break

    else:
        print("Invalid choice, try again.")
