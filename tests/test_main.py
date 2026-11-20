import json
import tempfile
import unittest
from pathlib import Path

from main import check_task, find_task, load_tasks, save_tasks


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

    def test_save_and_load_tasks(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "tasks.json"
            tasks = [example_task()]

            save_tasks(tasks, file_path)
            result = load_tasks(file_path)

            self.assertEqual(result, tasks)

    def test_load_empty_file_that_does_not_exist_yet(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "tasks.json"

            result = load_tasks(file_path)

            self.assertEqual(result, [])

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

    def test_invalid_json_file(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "tasks.json"
            file_path.write_text("{wrong json", encoding="utf-8")

            with self.assertRaises(ValueError):
                load_tasks(file_path)


if __name__ == "__main__":
    unittest.main()
