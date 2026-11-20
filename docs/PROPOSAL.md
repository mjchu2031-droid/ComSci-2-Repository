# StudyTrack – Project Proposal

**Project title:** StudyTrack: Student Task and Deadline Tracker  
**Prepared by:** Markellus Jhames D. Chu and group  
**Section:** Grade 8 – Anthurium  
**Subject:** Computer Science 2

## 1. Brief Description

StudyTrack is a program that will help students remember their school tasks and deadlines. Users can add assignments, see their saved tasks, search for a task, edit it, or delete it. The program will save the information in a JSON file so it will not disappear when the program closes.

## 2. Problem

Students sometimes have many assignments and deadlines from different subjects. It can be hard to remember all of them, especially when they are written in different places. We chose this idea because having one place for school tasks can make them easier to organize.

## 3. Objectives

- Make a program where students can add and manage their school tasks.
- Save task information in a JSON file.
- Let users view, search, update, and delete tasks.
- Show a summary of completed and unfinished tasks.
- Practice using Python functions, loops, lists, and files.

## 4. Features

1. **Add a task** – The user can enter the task name, subject, assigned date, due date, priority, status, and estimated time.
2. **View tasks** – The user can see all the tasks that have been saved.
3. **Search tasks** – The user can search using a task name, subject, or status.
4. **Update a task** – The user can change the information or status of a saved task.
5. **Delete a task** – The user can remove a task after confirming.
6. **Task summary** – The program can count the total tasks and show how many are pending, in progress, or completed.
7. **Deadline check** – The program can show tasks that are due soon or already overdue.
8. **Subject summary** – The program can count how many tasks there are for each subject.

## 5. Data We Will Save

We will use a file called `tasks.json`. Each task will have these details:

| Information | What it means | Example |
|---|---|---|
| task_id | Number of the task | 1 |
| title | Name of the task | Science worksheet |
| subject | School subject | Science |
| date_assigned | Date the task was added | 2026-11-20 |
| due_date | Deadline | 2026-11-24 |
| priority | How important it is | High |
| status | Progress of the task | In Progress |
| estimated_minutes | Estimated time to finish | 45 |

The program will read the JSON file when it starts. When a task is added, edited, or deleted, the file will be updated.

## 6. Inputs and Outputs

**Inputs:**
- The user's menu choice
- Task name and subject
- Assigned date and due date
- Priority and status
- Estimated minutes
- Task ID or search word

**Outputs:**
- List of saved tasks
- Search results
- Messages when a task is added, changed, or deleted
- Number of tasks in each status
- Completion percentage
- Tasks due soon or overdue
- Number of tasks for each subject

## 7. How the Program Will Work

1. The program opens and reads the saved tasks from the JSON file.
2. It shows a menu.
3. The user chooses what to do.
4. The program performs the selected action.
5. If the user changes the task list, the program saves the new information in the JSON file.
6. The menu appears again until the user chooses Exit.

## 8. Data Analysis

The program will count all the tasks and group them by status and subject. It will also calculate the percentage of completed tasks.

**Formula:**

`Completion percentage = (Completed tasks ÷ Total tasks) × 100`

It will also count tasks that are due within the next seven days and tasks that are already overdue. If there are no tasks, the program will show 0% instead of dividing by zero.

## 9. Programming Concepts

- **Functions:** We will use functions for adding, viewing, updating, deleting, and counting tasks.
- **Loops:** The menu will repeat until the user chooses Exit. Loops will also be used to go through the task list.
- **Lists:** The tasks will be kept in a Python list while the program is running.
- **JSON:** The `json` library will be used to save and load tasks.
- **Date handling:** The `datetime` tools will help check due dates.

## 10. Wireframe

See [WIREFRAME.md](WIREFRAME.md) for our simple sample layout and program flow.

## 11. Testing

We will test adding, viewing, searching, updating, and deleting tasks. We will also check what happens when the user enters an invalid date, leaves a required field blank, or opens an empty task list.

## 12. Group Schedule

See [TASK_SCHEDULE.md](TASK_SCHEDULE.md). We still need to add all group members' names and agree on who will do each task.

---

**Project idea:** Approved by our teacher, as reported by the group.  
**Project status:** Initial working version; we will continue testing and improving it.
