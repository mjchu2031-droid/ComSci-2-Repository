# StudyTrack – Simple Wireframe

This is our first idea of how the program will look. The final version may change as we work on it.

## 1. Main Menu

```text
------------------------------------
             STUDYTRACK
      Student Task and Deadline Tracker
------------------------------------
1. Add a task
2. View all tasks
3. Search tasks
4. Update a task
5. Delete a task
6. View task summary
7. Exit
------------------------------------
Enter your choice: __
```

## 2. Add a Task

```text
----------- ADD A TASK -------------
Task name:       __________________
Subject:         __________________
Date assigned:  YYYY-MM-DD
Due date:        YYYY-MM-DD
Priority:        Low / Medium / High
Status:          Pending / In Progress / Completed
Estimated time:  ______ minutes
------------------------------------
Task saved!
```

## 3. View Tasks

```text
------------------- MY TASKS -------------------
ID   Task name             Subject       Due date
1    Science worksheet    Science       2026-11-24
2    Math exercises       Mathematics   2026-11-25
------------------------------------------------
```

## 4. Task Summary

```text
--------------- TASK SUMMARY ----------------
Total tasks:             6
Pending:                 2
In Progress:             2
Completed:               2
Completion:              33.3%
Due in the next 7 days:  3
Overdue:                 1
-----------------------------------------------
```

The numbers above are only examples. The actual numbers will depend on the tasks saved by the user.

## 5. Program Flow

```text
          START
            |
     Read tasks.json
            |
       Show menu
            |
      User chooses
            |
   +--------+---------+--------+
   |        |         |        |
  Add      View     Search   Summary
   |        |         |        |
   +--------+---------+--------+
            |
    Update or Delete?
            |
    Save changes to JSON
            |
       Show menu again
            |
        Choose Exit
            |
           END
```
