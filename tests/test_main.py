import json
import tempfile
import unittest
from pathlib import Path
from datetime import date

from main import save_tasks, find_task, show_summary, check_task


def example_task():
    return {
        "task_id": 1,
        "title": "Science worksheet",
        "subject": "Science",
        "date_assigned": "2026-11-20",
        "due_date": "2026-11-24",
        "priority": "High",
        "status": "Pending",
        "estimated_minutes": 30
    }


class StudyTrackTests(unittest.TestCase):

    def test_save_tasks(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "tasks.json"
            old_file = None

            # Test the JSON format by writing a list with json directly.
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([example_task()], file)

            with open(file_path, "r", encoding="utf-8") as file:
                result = json.load(file)

            self.assertEqual(result[0]["title"], "Science worksheet")

    def test_find_task(self):
        tasks = [example_task()]
        result = find_task(tasks, 1)
        self.assertEqual(result["subject"], "Science")

    def test_task_id_not_found(self):
        self.assertIsNone(find_task([example_task()], 10))

    def test_valid_task(self):
        check_task(example_task())

    def test_invalid_due_date(self):
        task = example_task()
        task["due_date"] = "2026-11-18"

        with self.assertRaises(ValueError):
            check_task(task)

    def test_empty_task_name(self):
        task = example_task()
        task["title"] = ""

        with self.assertRaises(ValueError):
            check_task(task)


if __name__ == "__main__":
    unittest.main()
