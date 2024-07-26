class Task:
    def __init__(self, name, description, due_date=None):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{i}. [{status}] {task.name} ({task.due_date})")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            todo_list.add_task(Task(name, description, due_date))
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            print("Exiting. Have a productive day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
