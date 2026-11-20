# StudyTrack — Student Task and Deadline Tracker

**Computer Science 2 project**  
**Prepared by:** Markellus Jhames D. Chu  
**Section:** Grade 8 – Anthurium  
**Project idea:** Approved by the teacher (as reported by the student)

StudyTrack is a beginner-friendly Python command-line application for organizing school assignments, projects, and deadlines. It stores task records in a JSON file so that data remains available after the program closes.

## Features

- Add tasks with a title, subject, assigned date, due date, priority, status, and estimated time.
- View all saved tasks.
- Search tasks by title, subject, or status.
- Update saved task information.
- Delete tasks after confirmation.
- View statistics: total tasks, status counts, completion percentage, upcoming and overdue tasks, subject breakdown, and average estimated time.
- Validate user input and handle missing or invalid JSON data.

## Project structure

```text
ComSci-2-Repository/
├── main.py
├── data/
│   ├── tasks.json
│   └── sample_tasks.json
├── docs/
│   ├── PROPOSAL.md
│   ├── WIREFRAME.md
│   └── TASK_SCHEDULE.md
├── tests/
│   └── test_main.py
├── archive/
│   ├── 2d-distance-calculator-README.md
│   └── 2d_distance_calculator.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- No third-party packages are required. The project uses Python's built-in `json`, `datetime`, and `unittest` modules.

## How to run the application

1. Download or clone this repository.
2. Open a terminal in the repository folder.
3. Run:

```bash
python main.py
```

On some Windows setups, use:

```bash
py main.py
```

## How to run the tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

## Data storage

The application reads and writes `data/tasks.json`. It starts with an empty task list. A separate `data/sample_tasks.json` file contains example records that can be copied into `tasks.json` for demonstration. Do not put private or sensitive information in the sample dataset.

## Main menu

1. Add a task
2. View all tasks
3. Search tasks
4. Update a task
5. Delete a task
6. View task summary
7. Exit

## School project documentation

- [Project proposal](docs/PROPOSAL.md)
- [Wireframe and program flow](docs/WIREFRAME.md)
- [Task schedule](docs/TASK_SCHEDULE.md)

## Project status

The StudyTrack idea has been approved by the teacher, according to the student. This repository contains the initial working version. The group should review the code, test it, and improve it during development. Add the official names of all teammates and update task assignments in `docs/TASK_SCHEDULE.md`.

## Original class template

The teacher's starter template is available at:
https://github.com/MDeluteAgrazamendez/Project_Template_ComputerScience2
