# StudyTrack

**Computer Science 2 Project**  
**Made by:** Markellus Jhames D. Chu, Sebastian Meil C. Valdez, Sofia Kyle Nicole M. Palad

**Section:** Grade 8 – Anthurium

## What is StudyTrack?

StudyTrack is a simple program that can help students keep track of their schoolwork. It lets the user save assignments and their due dates so they can check what they still need to do.

The program uses Python and saves the tasks in a JSON file. This means the tasks will still be there when the program is opened again.

## What can it do?

- Add a task
- Show all saved tasks
- Search for a task
- Change the details or status of a task
- Delete a task
- Show a summary of the tasks

## Files in this project

- `main.py` – the main Python program
- `data/tasks.json` – where the tasks are saved
- `data/sample_tasks.json` – example tasks for testing
- `docs/PROPOSAL.md` – our project proposal draft
- `docs/WIREFRAME.md` – our simple plan for the screens and program flow
- `docs/TASK_SCHEDULE.md` – group tasks and schedule
- `tests/test_main.py` – some tests for the program

## How to run it

You need Python installed on your computer.

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Type:

```bash
python main.py
```

On some Windows computers, you may need to type `py main.py`.

## How to run the tests

Type this in the terminal:

```bash
python -m unittest discover -s tests -v
```
