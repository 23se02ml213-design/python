<div align="center">

# 🎓 Student Data Organizer

### *Console-Based Python App for Managing Student Records*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Interface](https://img.shields.io/badge/Interface-Console%20Based-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DataStructure](https://img.shields.io/badge/Data%20Structure-List%20of%20Dicts-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CRUD](https://img.shields.io/badge/Operations-CRUD-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Good record-keeping starts with good structure — learn to store it, and you control the data."*

</div>

---

## 📑 Table of Contents

- [📘 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [📂 Project Structure](#-project-structure)
- [🔄 Menu Workflow](#-menu-workflow)
- [🧩 Code Explanation](#-code-explanation)
- [🖥️ Sample Output](#️-sample-output)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚠️ Known Issues](#️-known-issues)
- [🚀 Possible Improvements](#-possible-improvements)
- [📜 License](#-license)
- [👤 Author](#-author)

---

## 📘 Overview

The **Student Data Organizer** is a beginner-friendly Python console application that manages student records using a **list of dictionaries**. It demonstrates core programming concepts such as **menu-driven CLI design**, **loops (`while`)**, **structural pattern matching (`match`/`case`)**, and basic **CRUD (Create, Read, Update, Delete)** operations on in-memory data.

The program lets a user:
- Add a new student record
- View all stored records
- Update an existing student's details
- Delete a student record
- View the subjects offered across all students
- Exit the program gracefully

This project is designed to:
- Practice working with **lists and dictionaries** as a simple in-memory database
- Use Python's `match`/`case` statement for menu routing
- Build nested menus (a sub-menu for updating individual fields)
- Reinforce loop control (`while True`, `break`) for a persistent CLI session

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console tool that stores multiple student records and lets a user add, view, update, delete, and summarize that data without needing a database or external file storage.

| 📋 Section | 🏷️ Type | 📝 Description |
|------------|----------|----------------|
| Add Student | Create | Collects ID, name, age, grade, DOB, and subjects |
| Display All Students | Read | Prints every stored student record in a formatted line |
| Update Student Information | Update | Lets the user edit one field at a time via a sub-menu |
| Delete Student | Delete | Removes a student record by ID |
| Display Subjects Offered | Read/Aggregate | Intended to show all unique subjects across students |

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📋 **Menu-Driven Interface** | A `while True` loop repeatedly shows a 6-option menu |
| 🗂️ **In-Memory Storage** | Students are stored as dictionaries inside a `students` list |
| 🆕 **Add Student** | Captures ID, name, age, grade, DOB, and subjects |
| 👀 **Display All Students** | Loops through `students` and prints a formatted summary line per record |
| ✏️ **Update Student Information** | Opens a nested sub-menu to update name, age, grade, DOB, or subjects |
| 🗑️ **Delete Student** | Searches by ID and removes the matching record |
| 📚 **Display Subjects Offered** | Meant to aggregate unique subjects using a `set` |
| 🚪 **Graceful Exit** | Prints a thank-you message and breaks out of the main loop |

---

## 📂 Project Structure

```
student-data-organizer/
│
├── project_3.py        → Main Python script (entry point)
└── README.md            → Project documentation
```

---

## 🔄 Menu Workflow

```
Program Start
      │
      ▼
┌───────────────────────────┐
│   Print Main Menu (1-6)   │
└───────────────────────────┘
      │
      ▼
┌───────────────────────────┐
│   Read user choice (int)  │
└───────────────────────────┘
      │
      ▼
match choice:
 ├── 1 → Add Student        (collect fields → append dict to students)
 ├── 2 → Display All        (loop students → print each record)
 ├── 3 → Update Student     (find by ID → nested sub-menu → edit field)
 ├── 4 → Delete Student     (find by ID → remove from list)
 ├── 5 → Display Subjects   (aggregate subjects into a set)
 ├── 6 → Exit               (print goodbye → break)
 └── _ → Invalid Choice
      │
      ▼
 Loop back to Main Menu (until Exit)
```

---

## 🧩 Code Explanation

### 1. Data Storage
```python
students = []
```
Each student is stored as a dictionary with keys: `identity`, `name`, `age`, `grade`, `dob`, and `subjects`.

### 2. Add Student (`case 1`)
Collects six fields from the user and appends a new dictionary to `students`. The `subjects` field is stored as a **raw comma-separated string** (e.g. `"science,math"`), not as a list.

### 3. Display All Students (`case 2`)
Iterates through `students` and prints a single formatted line per record using an f-string.

### 4. Update Student Information (`case 3`)
Asks for a student ID, then opens a **nested menu** (using a second `match`/`case` inside a `while True` loop) where the user can update one field at a time before choosing "6. back" to return to the main menu.

### 5. Delete Student (`case 4`)
Asks for a student ID and removes the matching dictionary from `students` using `list.remove()`.

### 6. Display Subjects Offered (`case 5`)
Intended to build a `set` of all unique subjects across every student using `set.update()`.

### 7. Exit (`case 6`)
Prints a goodbye message and `break`s out of the main loop, ending the program.

---

## 🖥️ Sample Output

```
====== RESTART: project_3.py ======
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 101
Enter Name: priya
Enter Age: 20
Enter Grade: A+
Enter Date of Birth (YYYY-MM-DD): 2005-09-07
Subjects (comma-separated): science

Student added successfully!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2

--- Display All Students ---
Student ID: 101 | Name: priya | Age: 20 | Grade: A+ | DOB: 2005-09-07 | Subjects: science

Select an option:
...
Enter your choice: 3

Enter Student ID to update: 101
1. Update name
2. Update Age
3. Update grade
4. Update dob
5. Update subject_input
6. back
Enter your choice: 1
enter update name: PRIYA
1. Update name
2. Update Age
3. Update grade
4. Update dob
5. Update subject_input
6. back
Enter your choice: 6
Update Record Success.......

Select an option:
...
Enter your choice: 4

Enter Delete Student ID: 101
No Record Found....

Select an option:
...
Enter your choice: 5

--- Unique Subjects Offered ---

Select an option:
...
Enter your choice: 6

Thank you for using the Student Data Organizer! Goodbye.
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (requires `match`/`case`, added in 3.10) |
| 🖨️ **print() / input()** | Built-in | Console I/O |
| 📦 **list / dict** | Built-in | In-memory data storage for student records |
| 🔁 **while loop** | Built-in | Keeps the menu running until Exit |
| 🧮 **match / case** | Built-in | Routes user choices to the correct action |
| 🧩 **set()** | Built-in | Intended for aggregating unique subjects |

---

## ⚠️ Known Issues

This script has a few logic bugs worth being aware of (and good practice exercises to fix):

| # | Location | Issue |
|---|----------|-------|
| 1 | `case 3` (Update) | The user is asked for `search_id`, but the lookup loop still checks against the **previous** `student_id` variable from Add Student, not `search_id`. |
| 2 | `case 3` (Update) | `search_id` is read as a `str` via `input()`, but `identity` is stored as an `int` — even if compared correctly, the types would mismatch. |
| 3 | `case 4` (Delete) | Same type mismatch: `student_id` is a `str` from `input()`, compared against an `int` `identity`, so deletion always reports "No Record Found." |
| 4 | `case 1` (Add) | `subjects` is stored as a single string (e.g. `"science,math"`) instead of a list (e.g. `["science", "math"]`). |
| 5 | `case 5` (Display Subjects) | `all_subjects.update(stu["subjects"])` iterates over **individual characters** of the subjects string (since it's a string, not a list), and the unique subjects are never actually printed even when `all_subjects` is non-empty. |
| 6 | `case 4` (Delete) | Mutating a list with `.remove()` while iterating over it in a `for` loop can skip elements if multiple matches exist. |

---

## 🚀 Possible Improvements

- Split `subjects_input` into a list with `.split(",")` and `.strip()` before storing.
- Fix variable names in `case 3` and `case 4` to use the freshly entered `search_id`, converted to `int` for comparison.
- Validate `input()` calls (e.g. wrap `int()` conversions in `try`/`except`) to avoid crashes on bad input.
- Use a dictionary keyed by `identity` instead of a list, for faster lookups and safer deletion.
- Print the contents of `all_subjects` in `case 5` after building the set.

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Priya Vadsak

*"Every program starts with a single input — learn to handle it right, and the rest follows."*

**🎓 Role:** Python Learner
**📍 Location:** India
**🛠️ Skills:** Python

</div>

---

<div align="center">

*Last updated: June 2026*

</div>
