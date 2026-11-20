# Project Proposal (First Draft)

## Project Title

**StudyTrack: Student Task and Deadline Tracker**

**Prepared by:** Markellus Jhames D. Chu  
**Section:** Grade 8 – Anthurium  
**Course:** Computer Science 2  
**Status:** For teacher review and approval

---

## Brief Description

StudyTrack is a proposed Python-based task management application designed to help students keep track of school assignments, projects, quizzes, and other academic responsibilities. Users will be able to add tasks, view saved tasks, update task details or completion status, delete records, and search or filter tasks. The application will store its records in a JSON file so that the information remains saved between program sessions.

The program will also analyze the saved tasks and display useful information, including the number of tasks in each status, tasks grouped by subject, the completion percentage, and the number of upcoming or overdue tasks.

## Problem Statement

Students may have several assignments and deadlines from different subjects at the same time. When these responsibilities are written in different notebooks, messages, or notes, it can be difficult to see all unfinished work in one place. A missed deadline or forgotten assignment can result from not having an organized record of tasks.

StudyTrack aims to address this problem by providing one organized place to record and manage academic tasks. By saving information in a JSON file, the application can preserve task records between sessions. Its summaries can help users understand their workload and identify which tasks still need attention.

## Project Objectives

1. To develop a simple application that allows users to record, view, edit, and delete school task entries.
2. To store task information persistently using a JSON file.
3. To organize tasks by subject, due date, priority, and completion status.
4. To calculate and present descriptive summaries, such as total tasks and completion percentage.
5. To apply functions, loops, lists, file handling, input validation, and testing in a practical Python project.

## Planned Features

The proposed application will include at least the following features:

1. **Add a task (Create):** The user enters a task title, subject, date assigned, due date, priority, status, and estimated time.
2. **View all tasks (Read):** The program displays all saved tasks in an organized list.
3. **Search and filter tasks:** The user can search by title or filter by subject, due date, priority, or status.
4. **Update a task (Update):** The user can edit task details or change its status to Pending, In Progress, or Completed.
5. **Delete a task (Delete):** The user can select a task to remove, with a confirmation step before deletion.
6. **Show task summaries:** The program calculates the total number of tasks, counts by status, and completion percentage.
7. **Show deadline information:** The program identifies upcoming and overdue tasks using the current date.
8. **Compare workload by subject and priority:** The program displays how many tasks belong to each subject and priority level.

## Data to Be Collected and Stored

The application will use the file `data/tasks.json` to store a list of task records. Each record will contain:

| Field | Description | Example |
|---|---|---|
| task_id | Unique identifier for the task | 1 |
| title | Name or short description of the task | Science worksheet |
| subject | Subject connected to the task | Science |
| date_assigned | Date the task was recorded | 2026-11-20 |
| due_date | Deadline of the task | 2026-11-24 |
| priority | Importance level | High |
| status | Current progress | In Progress |
| estimated_minutes | Estimated time needed | 45 |

The JSON file will act as persistent storage. When the program starts, it will load the saved records. After a user adds, edits, or deletes a task, the program will save the updated list to the JSON file.

The sample data included in this repository is fictional and is only for testing the proposed structure.

## Planned Inputs and Outputs

### Inputs

- Task title and subject
- Date assigned and due date
- Priority: Low, Medium, or High
- Status: Pending, In Progress, or Completed
- Estimated time in minutes
- Menu choice and search/filter terms

### Outputs

- A list of saved tasks
- Details of a selected task
- Confirmation after adding, updating, or deleting a task
- A summary of total, pending, in-progress, and completed tasks
- Completion percentage
- A list of upcoming and overdue tasks
- Counts of tasks grouped by subject and priority

## CRUD and Persistent Data Plan

- **Create:** Add a new task record to the in-memory list and save it to JSON.
- **Read:** Load and display records from the JSON file.
- **Update:** Find a record by its task ID, change its selected fields, and save the revised list.
- **Delete:** Find a record by its task ID, ask for confirmation, remove it, and save the revised list.

The application will use Python's built-in `json` library to read and write the data file.

## Data Analysis and Descriptive Statistics

The application is planned to calculate:

- Total number of saved tasks.
- Number and percentage of tasks that are Pending, In Progress, and Completed.
- Number of tasks per subject.
- Number of tasks per priority level.
- Number of upcoming and overdue tasks.
- Average estimated time for all saved tasks.

For the completion percentage, the planned formula is:

`Completion percentage = (number of completed tasks / total number of tasks) × 100`

The program will handle the case where there are no saved tasks so that it does not divide by zero.

## Logic Plan

### Pseudocode

1. Start the program.
2. Open the JSON data file.
3. If the file exists and contains valid data, load the task list. Otherwise, start with an empty list and show an appropriate message.
4. Display the main menu.
5. Ask the user to choose an operation.
6. If the user chooses Add, collect task details, validate them, add the task, and save the JSON file.
7. If the user chooses View, display the saved tasks.
8. If the user chooses Search/Filter, ask for a keyword or filter and display matching tasks.
9. If the user chooses Update, find the selected task, validate the new information, update it, and save.
10. If the user chooses Delete, ask for confirmation, remove the selected task, and save.
11. If the user chooses Summary, calculate and display task statistics.
12. If the user chooses Exit, close the program.
13. For an invalid menu choice or invalid input, display an error message and return to the menu.
14. Repeat the menu until the user chooses Exit.

## Sample Wireframe

See [wireframe.md](wireframe.md) for the proposed menu layout, example task display, summary output, and program flow.

## Testing and Input Validation

The application will check that required text fields are not empty, dates use the expected format, the due date is not earlier than the assigned date, priority and status use allowed values, and estimated minutes are positive whole numbers. It will also handle missing or invalid JSON data without silently treating incorrect data as valid. Proposed test cases are listed in [testing_plan.md](testing_plan.md).

## Initial Task Schedule and Team Members

See [task_schedule.md](task_schedule.md). The known preparer is Markellus Jhames D. Chu. Other team-member names and final task assignments must be completed after the teacher confirms the official group.

## Expected Outcome

The expected outcome is a beginner-friendly Python application that stores school task records in JSON, supports CRUD operations, and presents meaningful summaries to help users understand their academic workload.

---

**Teacher approval:** Pending  
**Note:** This proposal is an initial draft and may be revised based on teacher and group feedback.
