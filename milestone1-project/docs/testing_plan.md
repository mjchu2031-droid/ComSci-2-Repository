# Proposed Testing and Input Validation Plan

**Project:** StudyTrack — Student Task and Deadline Tracker

This file lists tests that should be carried out when the application is implemented. These are planned tests, not results from a completed program.

| Test | Input or action | Expected result |
|---|---|---|
| Add valid task | All fields contain valid values | Task is added and saved to JSON |
| Empty title | Leave task title blank | Program rejects the entry and asks for a title |
| Invalid date | Enter a date that does not follow YYYY-MM-DD | Program displays a validation message |
| Due date before assigned date | Due date is earlier than date assigned | Program rejects the date range |
| Invalid priority | Enter a value outside Low, Medium, High | Program asks for an allowed priority |
| Invalid status | Enter a value outside Pending, In Progress, Completed | Program asks for an allowed status |
| Non-positive estimated time | Enter 0 or a negative number | Program rejects the value |
| Read saved tasks | Choose View after saving tasks | Saved tasks are displayed |
| Update existing task | Enter a valid task ID and new details | Correct task is updated and saved |
| Unknown task ID | Enter an ID that does not exist | Program reports that no matching task was found |
| Delete task | Confirm deletion of an existing task | Selected task is removed and JSON is updated |
| Cancel deletion | Decline the deletion confirmation | Task remains in the JSON file |
| Empty dataset summary | Run summary when there are no tasks | Program shows zero counts and does not divide by zero |
| Corrupted JSON file | Load invalid JSON content | Program gives a clear error and avoids silently overwriting the data |
| Reopen program | Save a task, exit, and start again | Previously saved task is still available |

## Input Validation Rules

1. Required text fields must not be empty.
2. Dates must use the `YYYY-MM-DD` format and represent valid calendar dates.
3. The due date must be the same as or later than the date assigned.
4. Priority must be Low, Medium, or High.
5. Status must be Pending, In Progress, or Completed.
6. Estimated minutes must be a positive whole number.
7. Task IDs must be unique.
8. Deletion must require user confirmation.

## Output Verification

The total number of tasks shown in the summary should match the number of records in the JSON list. Status counts should add up to the total. The completion percentage should be checked against the formula in the proposal. When the task list is empty, the program should display a suitable message instead of attempting division by zero.
