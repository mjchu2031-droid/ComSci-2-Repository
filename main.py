"""
StudyTrack - Student Task and Deadline Tracker
Computer Science 2
"""

import json
from datetime import date, timedelta
from pathlib import Path

# This is where the tasks will be saved.
DATA_FILE = Path(__file__).parent / "data" / "tasks.json"

PRIORITIES = ["Low", "Medium", "High"]
STATUSES = ["Pending", "In Progress", "Completed"]


def load_tasks():
    """Read the tasks from the JSON file."""
    DATA_FILE.parent.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        save_tasks([])
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("The tasks.json file is not valid JSON.")

    if not isinstance(tasks, list):
        raise ValueError("The tasks.json file should contain a list.")

    return tasks


def save_tasks(tasks):
    """Save the task list to the JSON file."""
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def check_task(task):
    """Check if the task information is valid."""
    if not task["title"].strip():
        raise ValueError("Task name cannot be empty.")

    if not task["subject"].strip():
        raise ValueError("Subject cannot be empty.")

    try:
        assigned = date.fromisoformat(task["date_assigned"])
        due = date.fromisoformat(task["due_date"])
    except ValueError:
        raise ValueError("Dates must use YYYY-MM-DD format.")

    if due < assigned:
        raise ValueError("The due date cannot be earlier than the assigned date.")

    if task["priority"] not in PRIORITIES:
        raise ValueError("Choose Low, Medium, or High for priority.")

    if task["status"] not in STATUSES:
        raise ValueError("Choose a valid task status.")

    if not isinstance(task["estimated_minutes"], int) or task["estimated_minutes"] <= 0:
        raise ValueError("Estimated minutes must be a positive whole number.")


def get_task_details():
    """Ask the user for the details of a new task."""
    title = input("Task name: ").strip()
    subject = input("Subject: ").strip()
    date_assigned = input("Date assigned (YYYY-MM-DD): ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()

    print("Priority choices:", ", ".join(PRIORITIES))
    priority = input("Priority: ").strip().title()

    print("Status choices:", ", ".join(STATUSES))
    status = input("Status: ").strip().title()

    try:
        estimated_minutes = int(input("Estimated minutes: "))
    except ValueError:
        raise ValueError("Estimated minutes must be a whole number.")

    task = {
        "title": title,
        "subject": subject,
        "date_assigned": date_assigned,
        "due_date": due_date,
        "priority": priority,
        "status": status,
        "estimated_minutes": estimated_minutes
    }

    check_task(task)
    return task


def add_task(tasks):
    """Add a new task to the list."""
    task = get_task_details()

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(item["task_id"] for item in tasks) + 1

    task["task_id"] = new_id
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def view_tasks(tasks):
    """Show all saved tasks."""
    if len(tasks) == 0:
        print("There are no saved tasks yet.")
        return

    print("\nID | Task | Subject | Due date | Priority | Status")
    print("-" * 75)

    for task in tasks:
        print(
            str(task["task_id"]) + " | " +
            task["title"] + " | " +
            task["subject"] + " | " +
            task["due_date"] + " | " +
            task["priority"] + " | " +
            task["status"]
        )


def search_tasks(tasks):
    """Find tasks using a word in the title, subject, or status."""
    word = input("Enter a word to search: ").lower()
    found = []

    for task in tasks:
        if (word in task["title"].lower()
                or word in task["subject"].lower()
                or word in task["status"].lower()):
            found.append(task)

    if len(found) == 0:
        print("No matching tasks found.")
    else:
        view_tasks(found)


def find_task(tasks, task_id):
    """Find and return a task using its ID."""
    for task in tasks:
        if task["task_id"] == task_id:
            return task
    return None


def update_task(tasks):
    """Change the details of a saved task."""
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print("Press Enter if you want to keep the current information.")

    fields = ["title", "subject", "date_assigned", "due_date",
              "priority", "status", "estimated_minutes"]

    changes = {}

    for field in fields:
        new_value = input(field.replace("_", " ").title()
                          + " [" + str(task[field]) + "]: ").strip()

        if new_value != "":
            if field == "estimated_minutes":
                try:
                    changes[field] = int(new_value)
                except ValueError:
                    print("Estimated minutes must be a whole number.")
                    return
            elif field in ["priority", "status"]:
                changes[field] = new_value.title()
            else:
                changes[field] = new_value

    updated_task = task.copy()
    updated_task.update(changes)

    try:
        check_task(updated_task)
    except ValueError as error:
        print("Could not update task:", error)
        return

    task.update(changes)
    save_tasks(tasks)
    print("Task updated!")


def delete_task(tasks):
    """Remove a task after asking the user to confirm."""
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    answer = input("Are you sure you want to delete this task? (y/n): ").lower()

    if answer == "y":
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Delete cancelled.")


def show_summary(tasks):
    """Count tasks and show some information about them."""
    total = len(tasks)
    completed = 0
    pending = 0
    in_progress = 0
    upcoming = 0
    overdue = 0
    subject_count = {}

    today = date.today()
    next_week = today + timedelta(days=7)

    for task in tasks:
        if task["status"] == "Completed":
            completed += 1
        elif task["status"] == "Pending":
            pending += 1
        elif task["status"] == "In Progress":
            in_progress += 1

        subject = task["subject"]
        if subject in subject_count:
            subject_count[subject] += 1
        else:
            subject_count[subject] = 1

        due = date.fromisoformat(task["due_date"])

        if task["status"] != "Completed":
            if today <= due <= next_week:
                upcoming += 1
            elif due < today:
                overdue += 1

    if total == 0:
        completion = 0
        average_time = 0
    else:
        completion = completed / total * 100
        total_time = sum(task["estimated_minutes"] for task in tasks)
        average_time = total_time / total

    print("\n----- TASK SUMMARY -----")
    print("Total tasks:", total)
    print("Pending:", pending)
    print("In Progress:", in_progress)
    print("Completed:", completed)
    print("Completion:", round(completion, 1), "%")
    print("Due in the next 7 days:", upcoming)
    print("Overdue:", overdue)
    print("Average estimated time:", round(average_time, 1), "minutes")

    print("\nTasks by subject:")
    if len(subject_count) == 0:
        print("No tasks saved.")
    else:
        for subject in subject_count:
            print(subject + ":", subject_count[subject])


def show_menu():
    """Display the choices."""
    print("\n==============================")
    print("          STUDYTRACK")
    print("==============================")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Search tasks")
    print("4. Update a task")
    print("5. Delete a task")
    print("6. View task summary")
    print("7. Exit")
    print("==============================")


def main():
    """Start the program and keep showing the menu."""
    try:
        tasks = load_tasks()
    except (ValueError, OSError) as error:
        print("Could not load tasks:", error)
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                search_tasks(tasks)
            elif choice == "4":
                update_task(tasks)
            elif choice == "5":
                delete_task(tasks)
            elif choice == "6":
                show_summary(tasks)
            elif choice == "7":
                print("Your tasks are saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose from 1 to 7.")
        except (ValueError, OSError) as error:
            print("Something went wrong:", error)


if __name__ == "__main__":
    main()
