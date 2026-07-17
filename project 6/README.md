<div align="center">

# 📔 Personal Journal — Console-Based Journaling App

### *A Simple Python CLI App for Writing, Viewing, and Searching Daily Journal Entries*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![File Handling](https://img.shields.io/badge/File%20Handling-Read%2FWrite%2FAppend-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Datetime](https://img.shields.io/badge/Datetime-Timestamped%20Entries-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Menu](https://img.shields.io/badge/Menu-Driven%20Program-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"A journal is a place to keep your thoughts — this one keeps them timestamped and searchable."*

</div>

---

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🗂️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧠 Code Explanation](#-code-explanation)
- [🖥️ Sample Output](#-sample-output)
- [🛠️ Tech Stack](#-tech-stack)
- [📊 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📜 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Personal Journal** program is a beginner-friendly, menu-driven Python console application that lets users maintain a simple text-based journal. Every entry is automatically timestamped and appended to a local file (`journal.txt`), so nothing is ever overwritten.

The program offers a 5-option menu: add a new entry, view all saved entries, search entries by keyword, delete the entire journal, or exit. The menu keeps repeating until the user chooses to exit.

This project is designed to:
- Practice **file handling** in Python (`open`, `read`, `write`, `append` modes)
- Use the **`datetime`** module to timestamp every journal entry
- Use the **`os`** module to check for and remove files safely
- Apply **object-oriented programming** by wrapping journal operations inside a `Journal` class
- Handle runtime errors gracefully using **`try/except`** blocks
- Implement **keyword search** using Python's `in` operator on file contents
- Build a **persistent, menu-driven CLI loop** using `while True` and `break`

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console tool that lets the user record daily journal entries with automatic timestamps, view all past entries, search for entries containing a specific keyword, and delete the journal entirely — all through a simple repeating menu.

| 📂 Section | 📁 Type | 📝 Description |
|------------|---------|-----------------|
| Menu System | User Input | Displays 5 options and loops until "Exit" is chosen |
| Add Entry | File Write (Append) | Appends a timestamped entry to `journal.txt` |
| View Entries | File Read | Prints the full contents of `journal.txt` |
| Search Entries | File Read + String Search | Searches file contents for a keyword and prints matches |
| Delete Journal | File Removal | Deletes `journal.txt` after user confirmation |
| Error Handling | Exception Handling | Catches missing-file and I/O errors gracefully |

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📝 **Add Journal Entry** | Records a new entry with the current date and time automatically |
| 📖 **View All Entries** | Displays every saved entry in chronological (append) order |
| 🔍 **Keyword Search** | Searches the journal for a word/phrase and reports if it's found |
| 🗑️ **Delete Journal** | Permanently deletes the journal file after a y/n confirmation prompt |
| ⏱️ **Automatic Timestamps** | Uses `datetime.now()` to stamp every entry the moment it's saved |
| 🔁 **Persistent Menu Loop** | Menu keeps showing until the user explicitly chooses to exit |
| 🛡️ **Error Handling** | Gracefully handles a missing `journal.txt` instead of crashing |

---

## 🗂️ Project Structure

```
📁 personal-journal/
│
├── project6.py       # Main application script
├── journal.txt        # Auto-created file that stores journal entries (generated at runtime)
└── README.md          # Project documentation
```

---

## 🔄 Project Workflow

1. Program starts and displays the main menu (Add / View / Search / Delete / Exit)
2. User enters a numeric choice
3. Based on the choice, the corresponding `Journal` class method is called:
   - **Add** → prompts for entry text, timestamps it, and appends it to `journal.txt`
   - **View** → opens `journal.txt` and prints its full contents
   - **Search** → prompts for a keyword and checks if it exists in the file
   - **Delete** → asks for confirmation, then removes `journal.txt` if confirmed
4. Menu reappears after every action
5. Loop continues until the user selects **Exit**, which prints a farewell message and ends the program

---

## 🧠 Code Explanation

| Component | Explanation |
|-----------|-------------|
| `class Journal` | Groups all journal operations (add, view, search, delete) into a single object |
| `add()` | Opens `journal.txt` in append mode (`"a"`), writes a timestamp and the user's entry, then confirms success |
| `view()` | Opens `journal.txt` in read mode (`"r"`) and prints its entire contents; catches the error if the file doesn't exist |
| `search()` | Reads the full file content and uses the `in` operator to check if the keyword appears anywhere in it |
| `delete()` | Uses `os.path.exists()` to check if the file exists, asks for confirmation, then calls `os.remove()` to delete it |
| `try/except` blocks | Prevent the program from crashing if `journal.txt` hasn't been created yet |
| `while True` loop | Keeps the menu running repeatedly until the user chooses option `5` to exit |

---

## 🖥️ Sample Output

```
1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 1
Enter Entry: Today I learned Python.
Entry Added

1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 2
[2026-07-17 10:47:42.711363]
Today I Learned python.

[2026-07-17 10:54:18.939898]
Today I learned Python.

[2026-07-17 10:55:21.866689]
Today I learned Python.


1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 3
Enter Keyword: Python
Entry Found
[2026-07-17 10:47:42.711363]
Today I Learned python.

[2026-07-17 10:54:18.939898]
Today I learned Python.

[2026-07-17 10:55:21.866689]
Today I learned Python.


1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 4
Delete All? (y/n): y
Deleted

1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 6
Invalid Choice

1.Add
2.View
3.Search
4.Delete
5.Exit
Enter Choice: 5
Thank You
```

---

## 🛠️ Tech Stack

| Tool / Module | Purpose |
|----------------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 📅 **datetime** | Generates timestamps for each journal entry |
| 📁 **os** | Checks for and deletes the journal file |
| 💻 **Console I/O** | `input()` and `print()` for all user interaction |

---

## 📊 Results & Insights

After running the program, the following outcomes are verified:

- ✅ **Menu Loop Verified** — Program repeats the menu until choice `5` (Exit) is selected
- ✅ **Entries Timestamped** — Every entry is saved with an accurate `datetime.now()` stamp
- ✅ **Append Mode Working** — New entries are added without overwriting previous ones
- 🔍 **Keyword Search Working** — Correctly reports whether a keyword exists in the journal
- 🗑️ **Deletion Confirmed** — Journal file is removed only after explicit `y` confirmation
- ⚠️ **Invalid Input Handled** — Out-of-range menu choices show an "Invalid Choice" message instead of crashing
- 🛡️ **Missing File Handled** — Viewing or searching before any entry exists shows "No File Found" instead of an error

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Demonstrates file handling, OOP, and exception handling in one small project |
| 📦 **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🔁 **Reusable Menu Loop** | The `while True` + `break` structure is a reusable pattern for future CLI projects |
| 🧩 **Extensible** | Easy to add features like edit entry, entry count, or date-range filtering |
| 🧾 **Readable Code** | Clear, simple class-based structure makes the logic easy to follow |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Priya Vadsak

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/23se02ml213-design)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priya-vadsak-434729400/)

> *"A few lines of code, and every thought finds a place to stay."*

**🎓 Role:** Python Learner \
**📍 Location:** India \
**💻 Skills:** Python

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📘 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 📗 [Real Python — File Handling](https://realpython.com/read-write-files-python/) — In-depth file I/O tutorials
- 🌐 [GeeksForGeeks — File Handling in Python](https://www.geeksforgeeks.org/file-handling-python/) — File operations explained
- 📙 [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

🎥 **Video Demo:** [https://drive.google.com/drive/folders/1Y2Z0_LuanysAWJzNsX7qJ-WyTTZeIRLJ](https://drive.google.com/drive/folders/1Y2Z0_LuanysAWJzNsX7qJ-WyTTZeIRLJ)

</div>

</div>
