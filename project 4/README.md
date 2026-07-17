<div align="center">

# -- ! Functional Treat — Python Functions Showcase ! --
### *Console-Based Python App Demonstrating Core Function Concepts*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Input/Output](https://img.shields.io/badge/I%2F0-Console%20Based-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Logic](https://img.shields.io/badge/Logic-Functions%20%7C%20Recursion-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Menu](https://img.shields.io/badge/Menu-Driven%20Program-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Functions turn logic into building blocks — master them, and you master reusable code."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧾 Code Explanation](#-code-explanation)
- [🖥️ Sample Output](#️-sample-output)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Functional Treat** program is a beginner-friendly, menu-driven Python console application built to demonstrate the core **function concepts** in Python — from simple user-defined functions to recursion, `*args`, `**kwargs`, lambda expressions, global variables, and multiple return values.

The program stores a 1D list of numbers entered by the user and lets them explore that data through an 11-option menu: input data, view a summary, find the average, compute a factorial, filter values, sort data, view statistics, inspect `*args`/`**kwargs` behavior, or read each function's docstring. The menu keeps repeating until the user chooses to exit.

This project is designed to:
- Practice writing and calling **user-defined functions**
- Use **built-in functions** (`len`, `min`, `max`, `sum`) for quick data summaries
- Demonstrate **`*args`** and **`**kwargs`** for variable-length arguments
- Implement **recursion** to calculate a factorial
- Apply a **lambda expression** inside `filter()` to select values above a threshold
- Use a **global variable** to persist a summary dictionary across function calls
- Return **multiple values** from a single function using tuple unpacking
- Sort a list **ascending or descending** based on user choice
- Read **docstrings** (`__doc__`) to display function descriptions dynamically

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console tool that lets the user store a list of numbers and apply a variety of function-based operations to it — input, summarize, average, factorial, filter, sort, and inspect — until the user chooses to exit.

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Menu System | User Input | Displays 11 options and loops until "Exit" is chosen |
| Data Input | User-Defined Function | Stores a list of numbers entered by the user |
| Built-in Functions | `len`, `min`, `max`, `sum` | Displays a quick summary of the stored data |
| Recursion | User-Defined Function | Calculates the factorial of a number |
| Lambda + `filter()` | Anonymous Function | Filters values greater than or equal to a threshold |
| Global Variable | Scope | Persists a summary dictionary outside function scope |
| Multiple Return Values | Tuple Unpacking | Returns min, max, sum, and average together |
| `*args` / `**kwargs` | Variable Arguments | Displays values and dataset info dynamically |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📋 **Menu-Driven Interface** | Presents 11 options repeatedly until the user exits |
| ⌨️ **Input Data** | Stores a list of numbers entered as space-separated input |
| 📊 **Display Summary** | Uses built-in functions to show length, min, max, sum, and average |
| ➗ **Average Function** | A user-defined function that calculates the mean of the data |
| 🔁 **Factorial via Recursion** | Calculates `n!` by calling itself until the base case is reached |
| 🧮 **Filter with Lambda** | Filters the dataset using a lambda expression and a user threshold |
| 🔃 **Ascending/Descending Sort** | Sorts the stored data in either direction on request |
| 📦 **Multiple Return Values** | `statistics()` returns min, max, sum, and average in one call |
| ⭐ **`*args` Demo** | `show_values(*args)` prints the dataset as a tuple of positional arguments |
| 🗂️ **`**kwargs` Demo** | `show_info(**kwargs)` prints a saved summary dictionary as keyword arguments |
| 🌍 **Global Variable** | `summary` is declared `global` so it persists across function calls |
| 📝 **Function Descriptions** | Reads each function's `__doc__` string to explain what it does |
| 🖥️ **CLI Interface** | Fully console-based — no external libraries required |

---

## 🏗️ Project Structure

```
📦 functional-treat/
│
├── 📄 project4.py            ← Main Python script (entry point)
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌──────────────────────────────┐
│   Initialize data & summary  │
└─────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐◄────────────┐
│   Display Menu (1–11)        │              │
└─────────────┬────────────────┘              │
              │                                │
              ▼                                │
┌──────────────────────────────┐               │
│   Read User Choice            │              │
└─────────────┬────────────────┘              │
              │                                │
   ┌──────────┼─────────────────────────────┐  │
   ▼          ▼             ▼               │  │
Choice 1–10  Choice 11    Invalid            │  │
Run Function  Exit         Choice             │  │
(loop back)  (break loop) (re-prompt)         │  │
   │                                          │  │
   └──────────────────────────────────────────┘──┘
                       │
                       ▼
                Exit Program ✅
```

---

## 🧾 Code Explanation

### ⌨️ 1. Input Data

```python
def input_data():
    """Input 1D List"""
    global data
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Data Stored Successfully!")
```

Reads a line of space-separated numbers, converts each to an integer with `map()`, and stores the result in the `global` list `data` so every other function can access it.

---

### 📊 2. Built-in Functions — Display Summary

```python
def display_summary():
    """Display Summary"""
    print("Length =", len(data))
    print("Minimum =", min(data))
    print("Maximum =", max(data))
    print("Sum =", sum(data))
    print("Average =", sum(data) / len(data))
```

| Built-in | Purpose |
|----------|---------|
| `len(data)` | Counts how many numbers are stored |
| `min(data)` / `max(data)` | Finds the smallest and largest values |
| `sum(data)` | Adds all values together |
| `sum(data) / len(data)` | Computes the average on the fly |

---

### ➗ 3. User-Defined Function — Average

```python
def average():
    """Find Average"""
    return sum(data) / len(data)
```

A simple **user-defined function** that returns the mean of the dataset, reused by both `display_summary()` and `save_summary()`.

---

### ⭐ 4. `*args` — Show Values

```python
def show_values(*args):
    """Display Values"""
    print("Values are:", args)
```

`*args` collects any number of positional arguments into a tuple. When called as `show_values(*data)`, each item in `data` is unpacked and passed individually, then re-collected inside the function as a tuple for display.

---

### 🗂️ 5. `**kwargs` — Show Info

```python
def show_info(**kwargs):
    """Dataset Information"""
    for k, v in kwargs.items():
        print(k, ":", v)
```

`**kwargs` collects any number of keyword arguments into a dictionary. Called as `show_info(**summary)`, it prints every key-value pair from the `summary` dictionary.

---

### 🔁 6. Recursion — Factorial

```python
def factorial(n):
    """Factorial using Recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

| Step | Purpose |
|------|---------|
| Base case (`n == 0 or n == 1`) | Stops the recursion and returns `1` |
| Recursive case | Multiplies `n` by the factorial of `n - 1`, calling itself until the base case is hit |

> Recursion breaks a problem into smaller versions of itself until it reaches a case simple enough to answer directly.

---

### 🧮 7. Lambda — Filter Data

```python
def filter_data():
    """Filter Values"""
    value = int(input("Enter Threshold: "))
    result = list(filter(lambda x: x >= value, data))
    print("Filtered Data:", result)
```

A **lambda expression** (`lambda x: x >= value`) is passed to `filter()` as a short, anonymous function that keeps only the values greater than or equal to the entered threshold.

---

### 🌍 8. Global Variable — Save Summary

```python
def save_summary():
    """Save Summary"""
    global summary
    summary = {
        "Total": len(data),
        "Average": average()
    }
    print(summary)
```

The `global` keyword lets this function modify the module-level `summary` dictionary instead of creating a local one, so the saved data is available afterward to `show_info(**summary)`.

---

### 📦 9. Multiple Return Values — Statistics

```python
def statistics():
    """Return Statistics"""
    return min(data), max(data), sum(data), average()
```

Returns four values at once as a tuple. The caller unpacks them directly:

```python
a, b, c, d = statistics()
```

---

### 🔃 10. Sorting

```python
def sort_data():
    """Sort Data"""
    ch = int(input("1.Ascending 2.Descending: "))
    if ch == 1:
        data.sort()
    else:
        data.sort(reverse=True)
    print("Sorted Data:", data)
```

Sorts the `data` list **in place** using `list.sort()`, choosing ascending order by default or descending order when `reverse=True` is passed.

---

### 📝 11. Function Descriptions & Exit

```python
elif choice == 10:
    print(input_data.__doc__)
    print(display_summary.__doc__)
    print(average.__doc__)
    print(factorial.__doc__)

elif choice == 11:
    print("Thank You!")
    break
```

Every function's docstring (`__doc__`) is printed to explain its purpose, and choice `11` breaks out of the `while True` loop to end the program.

---

## 🖥️ Sample Output

```
----- MENU -----
1. Input Data
2. Display Summary
3. Average
4. Factorial
5. Filter Data
6. Sort Data
7. Statistics
8. Show *args
9. Show **kwargs
10. Show Function Description
11. Exit
Enter Choice: 1
Enter numbers separated by space: 10 20 30
Data Stored Successfully!

----- MENU -----
Enter Choice: 2
Length = 3
Minimum = 10
Maximum = 30
Sum = 60
Average = 20.0

----- MENU -----
Enter Choice: 3
Average = 20.0

----- MENU -----
Enter Choice: 4
Enter Number: 6
Factorial = 720

----- MENU -----
Enter Choice: 5
Enter Threshold: 30
Filtered Data: [30]

----- MENU -----
Enter Choice: 5
Enter Threshold: 10
Filtered Data: [10, 20, 30]

----- MENU -----
Enter Choice: 6
1.Ascending 2.Descending: 2
Sorted Data: [30, 20, 10]

----- MENU -----
Enter Choice: 7
Minimum = 10
Maximum = 30
Sum = 60
Average = 20.0

----- MENU -----
Enter Choice: 8
Values are: (30, 20, 10)

----- MENU -----
Enter Choice: 9
{'Total': 3, 'Average': 20.0}
Total : 3
Average : 20.0

----- MENU -----
Enter Choice: 10
Input 1D List
Display Summary
Find Average
Factorial using Recursion

----- MENU -----
Enter Choice: 11
Thank You!
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🖨️ **print()** | Built-in | Console output |
| ⌨️ **input()** | Built-in | User input collection |
| 🔡 **map() / int()** | Built-in | Converting input strings to a list of integers |
| 📏 **len(), min(), max(), sum()** | Built-in | Quick statistical summaries |
| 🔁 **Recursion** | Language Feature | Factorial calculation |
| 🧮 **Lambda + filter()** | Language Feature | Threshold-based data filtering |
| ⭐ **`*args` / `**kwargs`** | Language Feature | Variable-length argument handling |
| 🌍 **global keyword** | Language Feature | Persisting the `summary` dictionary across calls |
| 🔂 **while loop** | Built-in | Persistent menu until exit |
| 🔀 **if-elif-else** | Built-in | Menu branching and input validation |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Menu Loop Verified** — Program repeats the menu until choice `11` is selected
- 📊 **Summary Computed** — Length, min, max, sum, and average correctly calculated with built-ins
- 🔁 **Factorial Calculated** — Recursion correctly computes `6! = 720`
- 🧮 **Data Filtered** — Lambda + `filter()` correctly isolates values above the threshold
- 🔃 **Data Sorted** — List sorts correctly in both ascending and descending order
- 📦 **Multiple Values Returned** — `statistics()` returns min, max, sum, and average together
- ⭐ **`*args` Verified** — `show_values(*data)` correctly displays the data as a tuple
- 🗂️ **`**kwargs` Verified** — `show_info(**summary)` correctly unpacks and prints the summary
- 📝 **Docstrings Displayed** — Function descriptions print correctly via `__doc__`
- 🚪 **Graceful Exit** — Program ends with a thank-you message

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers nearly every core function concept in one project |
| 🔍 **Educational** | Clearly demonstrates `*args`, `**kwargs`, recursion, and lambdas side by side |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🔁 **Reusable Menu Loop** | The `while True` + `break` structure is a reusable pattern for future CLI projects |
| 🧪 **Extensible** | Easy to add more menu options (e.g., median calculator, prime checker) |
| 📖 **Readable Code** | Clear, well-commented, docstring-documented functions make logic easy to follow |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Priya Vadsak

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)]( https://github.com/23se02ml213-design)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]( https://www.linkedin.com/in/priya-vadsak-434729400/)

> *"Functions turn a single idea into a reusable tool — write once, call anywhere."*

**🎓 Role:** Python Learner \
**📍 Location:** India \
**🛠️ Skills:** Python

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔍 [Real Python — Functions](https://realpython.com/defining-your-own-python-function/) — In-depth function tutorials
- 🧠 [GeeksForGeeks — Recursion in Python](https://www.geeksforgeeks.org/recursion-in-python/) — Recursion explained
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

🎥 **Video Demo:** [https://drive.google.com/drive/folders/1Y2Z0_LuanysAWJzNsX7qJ-WyTTZeIRLJ]


</div>

