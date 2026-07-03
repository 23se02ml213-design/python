# Functional Treat - Simple Program

data = []
summary = {}

# 1. Input Data
def input_data():
    """Input 1D List"""
    global data
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Data Stored Successfully!")

# 2. Built-in Functions
def display_summary():
    """Display Summary"""
    print("Length =", len(data))
    print("Minimum =", min(data))
    print("Maximum =", max(data))
    print("Sum =", sum(data))
    print("Average =", sum(data) / len(data))

# 3. User Defined Function
def average():
    """Find Average"""
    return sum(data) / len(data)

# 4. *args
def show_values(*args):
    """Display Values"""
    print("Values are:", args)

# 5. **kwargs
def show_info(**kwargs):
    """Dataset Information"""
    for k, v in kwargs.items():
        print(k, ":", v)

# 6. Recursion
def factorial(n):
    """Factorial using Recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 7. Lambda
def filter_data():
    """Filter Values"""
    value = int(input("Enter Threshold: "))
    result = list(filter(lambda x: x >= value, data))
    print("Filtered Data:", result)

# 8. Global Variable
def save_summary():
    """Save Summary"""
    global summary
    summary = {
        "Total": len(data),
        "Average": average()
    }
    print(summary)

# 9. Return Multiple Values
def statistics():
    """Return Statistics"""
    return min(data), max(data), sum(data), average()

# 10. Sorting
def sort_data():
    """Sort Data"""
    ch = int(input("1.Ascending 2.Descending: "))
    if ch == 1:
        data.sort()
    else:
        data.sort(reverse=True)
    print("Sorted Data:", data)

# Main Menu
while True:
    print("\n----- MENU -----")
    print("1. Input Data")
    print("2. Display Summary")
    print("3. Average")
    print("4. Factorial")
    print("5. Filter Data")
    print("6. Sort Data")
    print("7. Statistics")
    print("8. Show *args")
    print("9. Show **kwargs")
    print("10. Show Function Description")
    print("11. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        display_summary()

    elif choice == 3:
        print("Average =", average())

    elif choice == 4:
        n = int(input("Enter Number: "))
        print("Factorial =", factorial(n))

    elif choice == 5:
        filter_data()

    elif choice == 6:
        sort_data()

    elif choice == 7:
        a, b, c, d = statistics()
        print("Minimum =", a)
        print("Maximum =", b)
        print("Sum =", c)
        print("Average =", d)

    elif choice == 8:
        show_values(*data)

    elif choice == 9:
        save_summary()
        show_info(**summary)

    elif choice == 10:
        print(input_data.__doc__)
        print(display_summary.__doc__)
        print(average.__doc__)
        print(factorial.__doc__)

    elif choice == 11:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
