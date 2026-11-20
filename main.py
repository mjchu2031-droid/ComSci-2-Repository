"""
StudyTrack: Student Task and Deadline Tracker

Computer Science 2 project
Prepared by: Markellus Jhames D. Chu

A command-line program that stores school tasks in a JSON file.
It supports Create, Read, Update, and Delete (CRUD) operations
and displays simple summaries of the saved tasks.
"""

import json
from datetime import date, timedelta
from pathlib import Path


# Keep the data file beside this program, inside the data folder.
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"

VALID_PRIORITIES = ("Low", "Medium", "High")
VALID_STATUSES = ("Pending", "In Progress", "Completed")


def parse_date(value, field_name):
    """Convert YYYY-MM-DD text into a date, or raise a helpful error."""
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must use YYYY-MM-DD format.")


def validate_task(task):
    """Check that a task record has valid values."""
    for field in ("title", "subject"):
        if not isinstance(task.get(field), str) or not task[field].strip():
            raise ValueError(f"{field.replace('_', ' ').title()} cannot be empty.")

    assigned = parse_date(task.get("date_assigned"), "Date assigned")
    due = parse_date(task.get("due_date"), "Due date")

    if due < assigned:
        raise ValueError("Due date cannot be earlier than the date assigned.")

    if task.get("priority") not in VALID_PRIORITIES:
        raise ValueError("Priority must be Low, Medium, or High.")

    if task.get("status") not in VALID_STATUSES:
        raise ValueError("Status must be Pending, In Progress, or Completed.")

    minutes = task.get("estimated_minutes")
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes <= 0:
        raise ValueError("Estimated minutes must be a positive whole number.")

    task_id = task.get("task_id")
    if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Task ID must be a positive whole number.")


class TaskManager:
    """Loads, saves, and manages task records in a JSON file."""

    def __init__(self, data_file=DATA_FILE):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.tasks = self.load_tasks()

        # Create an empty JSON file the first time the program is used.
        if not self.data_file.exists():
            self.save_tasks()

    def load_tasks(self):
        """Read task records from JSON without overwriting damaged data."""
        if not self.data_file.exists():
            return []

        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                records = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"The data file contains invalid JSON: {self.data_file}. "
                "Please repair or restore the file before continuing."
            ) from error

        if not isinstance(records, list):
            raise ValueError("The JSON data must contain a list of task records.")

        for record in records:
            if not isinstance(record, dict):
                raise ValueError("Every task record in the JSON file must be an object.")
            validate_task(record)

        return records

    def save_tasks(self):
        """Write all current tasks to the JSON file."""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            file.write("\n")

    def add_task(self, details):
        """Create a task, assign its ID, and save it."""
        next_id = max((task["task_id"] for task in self.tasks), default=0) + 1
        new_task = {"task_id": next_id, **details}
        validate_task(new_task)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def get_task(self, task_id):
        """Return a task with the selected ID, or None if it does not exist."""
        return next(
            (task for task in self.tasks if task["task_id"] == task_id),
            None
        )

    def update_task(self, task_id, changes):
        """Update selected fields in an existing task and save the result."""
        task = self.get_task(task_id)
        if task is None:
            return False

        updated_task = {**task, **changes}
        validate_task(updated_task)
        task.update(changes)
        self.save_tasks()
        return True

    def delete_task(self, task_id):
        """Delete a task by ID and save the result."""
        task = self.get_task(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        self.save_tasks()
        return True


def calculate_summary(tasks, today=None):
    """Calculate counts and descriptive summaries for the task list."""
    today = today or date.today()
    total = len(tasks)

    status_counts = {
        status: sum(1 for task in tasks if task["status"] == status)
        for status in VALID_STATUSES
    }

    subject_counts = {}
    for task in tasks:
        subject = task["subject"]
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

    upcoming_limit = today + timedelta(days=7)
    upcoming = 0
    overdue = 0

    for task in tasks:
        if task["status"] == "Completed":
            continue

        due = parse_date(task["due_date"], "Due date")
        if today <= due <= upcoming_limit:
            upcoming += 1
        elif due < today:
            overdue += 1

    average_minutes = (
        sum(task["estimated_minutes"] for task in tasks) / total
        if total else 0
    )

    completion_rate = (
        status_counts["Completed"] / total * 100
        if total else 0
    )

    return {
        "total": total,
        "status_counts": status_counts,
        "subject_counts": subject_counts,
        "upcoming": upcoming,
        "overdue": overdue,
        "average_minutes": average_minutes,
        "completion_rate": completion_rate,
    }


def prompt_nonempty(label):
    """Ask until the user enters text."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def prompt_date(label):
    """Ask for a valid date in YYYY-MM-DD format."""
    while True:
        value = input(label).strip()
        try:
            date.fromisoformat(value)
            return value
        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format (example: 2026-11-25).")


def prompt_choice(label, allowed_values):
    """Ask until the user chooses one of the listed options."""
    options = ", ".join(allowed_values)
    while True:
        value = input(f"{label} ({options}): ").strip().title()
        if value in allowed_values:
            return value
        print(f"Please choose one of these values: {options}.")


def prompt_positive_integer(label):
    """Ask for a positive whole number."""
    while True:
        value = input(label).strip()
        try:
            number = int(value)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def prompt_task_details():
    """Collect and validate all information needed for a new task."""
    while True:
        title = prompt_nonempty("Task title: ")
        subject = prompt_nonempty("Subject: ")
        date_assigned = prompt_date("Date assigned (YYYY-MM-DD): ")
        due_date = prompt_date("Due date (YYYY-MM-DD): ")

        try:
            if date.fromisoformat(due_date) < date.fromisoformat(date_assigned):
                raise ValueError("Due date cannot be earlier than date assigned.")
        except ValueError as error:
            print(error)
            print("Please enter the dates again.\n")
            continue

        priority = prompt_choice("Priority", VALID_PRIORITIES)
        status = prompt_choice("Status", VALID_STATUSES)
        estimated_minutes = prompt_positive_integer("Estimated minutes: ")

        return {
            "title": title,
            "subject": subject,
            "date_assigned": date_assigned,
            "due_date": due_date,
            "priority": priority,
            "status": status,
            "estimated_minutes": estimated_minutes,
        }


def display_tasks(tasks):
    """Print tasks in a readable table-like format."""
    if not tasks:
        print("\nNo tasks have been saved yet. Choose 'Add a task' to begin.")
        return

    print("\n" + "-" * 100)
    print(f"{'ID':<5} {'TITLE':<27} {'SUBJECT':<17} {'DUE DATE':<13} {'PRIORITY':<10} {'STATUS'}")
    print("-" * 100)

    for task in tasks:
        print(
            f"{task['task_id']:<5} "
            f"{task['title'][:26]:<27} "
            f"{task['subject'][:16]:<17} "
            f"{task['due_date']:<13} "
            f"{task['priority']:<10} "
            f"{task['status']}"
        )

    print("-" * 100)


def add_task_action(manager):
    print("\n=== Add a Task ===")
    details = prompt_task_details()
    task = manager.add_task(details)
    print(f"Task #{task['task_id']} was saved successfully.")


def search_tasks_action(manager):
    print("\n=== Search Tasks ===")
    keyword = input("Enter a title, subject, or status keyword: ").strip().lower()

    matches = [
        task for task in manager.tasks
        if keyword in task["title"].lower()
        or keyword in task["subject"].lower()
        or keyword in task["status"].lower()
    ]
    display_tasks(matches)


def read_task_id():
    while True:
        value = input("Enter task ID: ").strip()
        try:
            task_id = int(value)
            if task_id > 0:
                return task_id
        except ValueError:
            pass
        print("Please enter a valid positive task ID.")


def update_task_action(manager):
    print("\n=== Update a Task ===")
    display_tasks(manager.tasks)
    if not manager.tasks:
        return

    task_id = read_task_id()
    task = manager.get_task(task_id)
    if task is None:
        print("No task was found with that ID.")
        return

    print("Press Enter to keep the current value.")
    changes = {}

    for field, label in (
        ("title", "Title"),
        ("subject", "Subject"),
        ("date_assigned", "Date assigned"),
        ("due_date", "Due date"),
    ):
        current = task[field]
        new_value = input(f"{label} [{current}]: ").strip()
        if new_value:
            changes[field] = new_value

    for field, label, allowed in (
        ("priority", "Priority", VALID_PRIORITIES),
        ("status", "Status", VALID_STATUSES),
    ):
        current = task[field]
        new_value = input(f"{label} [{current}] ({', '.join(allowed)}): ").strip()
        if new_value:
            normalized = new_value.title()
            if normalized not in allowed:
                print(f"{label} must be one of: {', '.join(allowed)}.")
                return
            changes[field] = normalized

    current_minutes = task["estimated_minutes"]
    new_minutes = input(f"Estimated minutes [{current_minutes}]: ").strip()
    if new_minutes:
        try:
            changes["estimated_minutes"] = int(new_minutes)
        except ValueError:
            print("Estimated minutes must be a positive whole number.")
            return

    try:
        if manager.update_task(task_id, changes):
            print("Task updated successfully.")
    except ValueError as error:
        print(f"Task was not updated: {error}")


def delete_task_action(manager):
    print("\n=== Delete a Task ===")
    display_tasks(manager.tasks)
    if not manager.tasks:
        return

    task_id = read_task_id()
    task = manager.get_task(task_id)
    if task is None:
        print("No task was found with that ID.")
        return

    confirmation = input(
        f"Delete '{task['title']}'? Type Y to confirm: "
    ).strip().lower()

    if confirmation == "y":
        manager.delete_task(task_id)
        print("Task deleted successfully.")
    else:
        print("Deletion cancelled. The task was not changed.")


def show_summary_action(manager):
    print("\n=== Task Summary ===")
    summary = calculate_summary(manager.tasks)

    print(f"Total tasks: {summary['total']}")
    for status in VALID_STATUSES:
        print(f"{status}: {summary['status_counts'][status]}")

    print(f"Completion rate: {summary['completion_rate']:.1f}%")
    print(f"Upcoming tasks (next 7 days): {summary['upcoming']}")
    print(f"Overdue tasks: {summary['overdue']}")
    print(f"Average estimated time: {summary['average_minutes']:.1f} minutes")

    print("\nTasks by subject:")
    if summary["subject_counts"]:
        for subject, count in sorted(summary["subject_counts"].items()):
            print(f"- {subject}: {count}")
    else:
        print("- No task data available yet.")


def print_menu():
    print("\n" + "=" * 48)
    print("                 STUDYTRACK")
    print("       Student Task and Deadline Tracker")
    print("=" * 48)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Search tasks")
    print("4. Update a task")
    print("5. Delete a task")
    print("6. View task summary")
    print("7. Exit")
    print("-" * 48)


def run_app(manager=None):
    """Run the main menu until the user chooses Exit."""
    try:
        manager = manager or TaskManager()
    except (ValueError, OSError) as error:
        print(f"Could not load task data: {error}")
        print("Please check the JSON file before running the program again.")
        return

    actions = {
        "1": lambda: add_task_action(manager),
        "2": lambda: display_tasks(manager.tasks),
        "3": lambda: search_tasks_action(manager),
        "4": lambda: update_task_action(manager),
        "5": lambda: delete_task_action(manager),
        "6": lambda: show_summary_action(manager),
    }

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Your tasks are saved. Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from 1 to 7.")
            continue

        try:
            action()
        except (ValueError, OSError) as error:
            print(f"Operation could not be completed: {error}")


if __name__ == "__main__":
    run_app()
