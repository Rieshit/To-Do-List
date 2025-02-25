import os
TASKS_FILE = "tasks.txt"
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!")
def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks.pop(index)}' marked as done!")
            save_tasks(tasks)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks.pop(index)}' deleted successfully!")
            save_tasks(tasks)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def main():
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting... Have a productive day! 😊")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
