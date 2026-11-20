"""Unit tests for StudyTrack. Run: python -m unittest discover -s tests -v"""

import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from main import TaskManager, calculate_summary, validate_task


def make_task(task_id=1, status="Pending", due_date="2026-11-24"):
    return {
        "task_id": task_id,
        "title": "Science worksheet",
        "subject": "Science",
        "date_assigned": "2026-11-20",
        "due_date": due_date,
        "priority": "High",
        "status": status,
        "estimated_minutes": 45,
    }


class TaskValidationTests(unittest.TestCase):
    def test_valid_task(self):
        validate_task(make_task())

    def test_empty_title_is_rejected(self):
        task = make_task()
        task["title"] = " "
        with self.assertRaises(ValueError):
            validate_task(task)

    def test_invalid_date_is_rejected(self):
        task = make_task()
        task["due_date"] = "not-a-date"
        with self.assertRaises(ValueError):
            validate_task(task)

    def test_due_date_before_assigned_date_is_rejected(self):
        task = make_task(due_date="2026-11-19")
        with self.assertRaises(ValueError):
            validate_task(task)

    def test_invalid_priority_is_rejected(self):
        task = make_task()
        task["priority"] = "Urgent"
        with self.assertRaises(ValueError):
            validate_task(task)

    def test_minutes_must_be_positive_integer(self):
        task = make_task()
        task["estimated_minutes"] = 0
        with self.assertRaises(ValueError):
            validate_task(task)


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task_and_persist(self):
        task = self.manager.add_task({key: value for key, value in make_task().items()
                                      if key != "task_id"})
        self.assertEqual(task["task_id"], 1)
        with self.data_file.open(encoding="utf-8") as file:
            saved = json.load(file)
        self.assertEqual(len(saved), 1)

    def test_update_task(self):
        self.manager.add_task({key: value for key, value in make_task().items()
                               if key != "task_id"})
        changed = self.manager.update_task(1, {"status": "Completed"})
        self.assertTrue(changed)
        self.assertEqual(self.manager.get_task(1)["status"], "Completed")

    def test_delete_task(self):
        self.manager.add_task({key: value for key, value in make_task().items()
                               if key != "task_id"})
        self.assertTrue(self.manager.delete_task(1))
        self.assertEqual(self.manager.tasks, [])

    def test_missing_task_returns_false(self):
        self.assertFalse(self.manager.delete_task(99))

    def test_corrupt_json_is_not_overwritten(self):
        self.data_file.write_text("{invalid json", encoding="utf-8")
        with self.assertRaises(ValueError):
            TaskManager(self.data_file)
        self.assertEqual(self.data_file.read_text(encoding="utf-8"), "{invalid json")


class SummaryTests(unittest.TestCase):
    def test_summary_counts(self):
        tasks = [
            make_task(1, "Completed", "2026-11-20"),
            make_task(2, "Pending", "2026-11-22"),
            make_task(3, "In Progress", "2026-11-10"),
        ]
        summary = calculate_summary(tasks, today=date(2026, 11, 20))
        self.assertEqual(summary["total"], 3)
        self.assertEqual(summary["status_counts"]["Completed"], 1)
        self.assertAlmostEqual(summary["completion_rate"], 100 / 3)
        self.assertEqual(summary["upcoming"], 1)
        self.assertEqual(summary["overdue"], 1)

    def test_empty_summary_does_not_divide_by_zero(self):
        summary = calculate_summary([], today=date(2026, 11, 20))
        self.assertEqual(summary["total"], 0)
        self.assertEqual(summary["completion_rate"], 0)
        self.assertEqual(summary["average_minutes"], 0)


if __name__ == "__main__":
    unittest.main()
