# Interactive Perspronal Data Collector

print("Welcome to the Interactive Personal Data Collector!\n")


# Collect Information
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in cm: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Display Variable Details
print("Name:", name, "Type:", type(name), " Memory Address:", id(name))
print("Age:", age, "Type:", type(age), " Memory Address:", id(age))
print("Height:", height, "cm", "Type:", type(height), " Memory Address:", id(height))
print("Favourite Number:", fav_number, "Type:", type(fav_number), " Memory Address:", id(fav_number))

# Data Processing
current_year = 2025
birth_year = current_year - age

print("\nYour birth year is approximately:", birth_year)


# User-Friendly Summary
print("\n========== USER SUMMARY ==========")
print("Hello", name)
print("You are", age, "years old.")
print("Your height is", height, "cm.")
print("Your favourite number is", fav_number)
print("Your estimated birth year is", birth_year)
print("==================================")

# Exit Message
print("\nThank you for using the Personal Data Collector!")

