import json
import os

TASKS_FILE = 'tasks.json'

# Load existing tasks or create empty list
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks = load_tasks()
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print("✅ Task added!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️ Completed" if task["completed"] else "❌ Pending"
        print(f"{i}. {task['title']} - {status}\n   {task['description']}")

# Mark task as completed
def mark_completed():
    tasks = load_tasks()
    view_tasks()
    idx = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    else:
        print("❌ Invalid task number.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['title']}")
    else:
        print("❌ Invalid task number.")

# Menu loop
def main():
    while True:
        print("\n--- Task Tracker CLI ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, try again.")

if __name__ == '__main__':
    main()
