import json

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks left to do! :)")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['text']}")

def add_task(tasks):
    text = input("Enter your task: ")
    tasks.append({"text": text, "done": False})

def mark_done(tasks):
    view_tasks(tasks)
    idx = int(input("Which task is done? (Number): ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True

def delete_task(tasks):
    view_tasks(tasks)
    idx = int(input("Which task do you want to delete? (Number): ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using my app! Bye! :)")
            print("This app was made by Toby! Github profile: Toby8-dev :)")
            break

if __name__ == "__main__":
    main()      
