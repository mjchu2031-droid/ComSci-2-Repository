# StudyTrack — Project Proposal

**Project title:** StudyTrack: Student Task and Deadline Tracker  
**Prepared by:** Markellus Jhames D. Chu  
**Section:** Grade 8 – Anthurium  
**Course:** Computer Science 2  
**Project idea approval:** Approved by the teacher (as reported by the student)

## 1. Brief Description

StudyTrack is a Python command-line application that helps students record and organize assignments, projects, quizzes, and other academic tasks. It stores task records persistently in a JSON file. Users can add, view, search, update, and delete tasks, then review summaries of their workload.

## 2. Problem Statement

Students may have several school tasks and deadlines across different subjects. When these are recorded in separate notebooks or messages, it can be difficult to keep track of unfinished work and upcoming due dates. StudyTrack provides one organized place to manage task records and view useful summaries. Saving the records in JSON means the information remains available after the program closes.

## 3. Objectives

1. Create an application that can manage school task records.
2. Use a JSON file to save and retrieve task information.
3. Implement Create, Read, Update, and Delete (CRUD) operations.
4. Organize tasks by subject, deadline, priority, and status.
5. Calculate descriptive summaries such as status counts, completion percentage, and average estimated time.
6. Apply input validation and test the program for common errors.

## 4. Planned and Implemented Features

1. Add a task with title, subject, assigned date, due date, priority, status, and estimated minutes.
2. View all saved tasks in a table-like list.
3. Search by task title, subject, or status.
4. Update task information by task ID.
5. Delete a task after confirmation.
6. Display totals for Pending, In Progress, and Completed tasks.
7. Calculate completion percentage.
8. Identify upcoming tasks due within seven days and overdue tasks that are not completed.
9. Display task counts by subject and average estimated time.

## 5. Data to Be Collected and Stored

The application uses `data/tasks.json`. Each task record contains:

| Field | Description | Example |
|---|---|---|
| task_id | Unique task number | 1 |
| title | Task name | Science worksheet |
| subject | Subject name | Science |
| date_assigned | Date recorded | 2026-11-20 |
| due_date | Task deadline | 2026-11-24 |
| priority | Importance level | High |
| status | Current progress | In Progress |
| estimated_minutes | Estimated time | 45 |

The application loads the JSON list at startup and saves the list after each successful add, update, or delete operation. The main dataset starts empty; a separate sample dataset is provided for demonstration.

## 6. Inputs and Outputs

**Inputs:** menu choice, task title, subject, assigned date, due date, priority, status, estimated minutes, task ID, and search keyword.

**Outputs:** saved task list, search results, success or error messages, total task count, status counts, completion percentage, upcoming and overdue task counts, subject breakdown, and average estimated time.

## 7. CRUD Operations

- **Create:** add a task record and save it to JSON.
- **Read:** load and display saved task records.
- **Update:** edit a record selected by task ID and save the changes.
- **Delete:** remove a selected record after confirmation and save the changes.

## 8. Data Analysis

The program calculates the number of tasks in each status, completion percentage, tasks per subject, upcoming task count, overdue task count, and average estimated time.

Completion percentage is:

`(Completed tasks / Total tasks) × 100`

The program returns 0% when there are no tasks, preventing division by zero.

## 9. Programming Concepts

- **Functions and arguments:** separate functions manage input, validation, CRUD operations, and summaries.
- **Iteration:** loops display the menu, process lists of tasks, and repeat input prompts when necessary.
- **Arrays/lists:** Python lists hold multiple task records.
- **Programming libraries:** `json` handles persistent storage and `datetime` handles dates. `unittest` is used for testing.

## 10. Wireframe

See [WIREFRAME.md](WIREFRAME.md) for the main menu, sample task display, summary screen, and program flow.

## 11. Testing

Planned automated tests and manual checks are in the `tests/` folder and the repository README. These include valid and invalid dates, empty task data, CRUD persistence, and summary calculations.

## 12. Team Schedule

See [TASK_SCHEDULE.md](TASK_SCHEDULE.md). The official group member names and final task assignments should be added by the group.

**Project status:** The project idea has been approved by the teacher, as reported by the student. The application is an initial working version and will continue to be developed and tested.
