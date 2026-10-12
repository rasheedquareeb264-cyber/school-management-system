# School Management System — Project Instructions

## Project Overview
Build a command-line application for managing students, teachers, classes, and subjects. Store data in JSON and organize the program into clear functions.

## Learning Objectives
Practice variables, input/output, conditions, loops, lists, dictionaries, functions, file handling, JSON, and `try` / `except`.

## Main Menu
Create a repeating menu:
1. Manage students
2. Manage teachers
3. Manage classes
4. Manage subjects
5. View school statistics
6. Exit

Each management section should have its own submenu.

## Required Features

### Students
Fields: student ID, full name, age, gender, class. Support add, view, search, update, and delete.

### Teachers
Fields: teacher ID, full name, subject taught, phone number. Support add, view, search, update, and delete.

### Classes
Fields: class name, arm (if applicable), assigned teacher. Support add, view, search, delete, and assigning students to classes.

### Subjects
Fields: subject name and assigned teacher. Support add, view, search, and delete.

### Statistics
Display total students, teachers, classes, and subjects. Optional: show student counts by class or gender.

## Data Persistence
Use separate files: `students.json`, `teachers.json`, `classes.json`, and `subjects.json`. Load data at startup and save changes after modifications. If a file is missing, initialize that collection as empty.

## Error Handling
Handle invalid menu choices, invalid numeric input, empty required fields, duplicate IDs where uniqueness is required, missing records, and missing or invalid JSON files.

## Code Organization
Use separate functions for each operation and data type. Helper functions for loading, saving, finding records, validating input, and displaying menus are encouraged.

## Suggested Development Order
1. Build the main menu and student management.
2. Add JSON loading and saving.
3. Add teacher management.
4. Add class management and student assignment.
5. Add subject management.
6. Add statistics.
7. Test and improve validation.

## Optional Challenges
- Add grades and pass/fail results.
- Search students by class or gender.
- Sort records by name.
- Add basic login or generate a school summary report.

## Suggested Assessment Rubric

| Area | Marks |
|---|---:|
| Menu flow and navigation | 10 |
| Functions and organization | 15 |
| CRUD operations | 20 |
| JSON and file handling | 15 |
| Error handling and validation | 10 |
| Lists and dictionaries | 10 |
| Statistics and extra features | 10 |
| Readability and naming | 5 |
| Testing and presentation | 5 |
| **Total** | **100** |

## Submission Checklist
- [ ] Main menu and submenus work.
- [ ] All four data types can be managed.
- [ ] JSON data loads and saves correctly.
- [ ] Invalid input and missing records are handled.
- [ ] Statistics are correct.
- [ ] Code is readable, organized, and tested.
