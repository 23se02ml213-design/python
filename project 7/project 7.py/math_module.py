import math

def menu():
    while True:
        print("\nMathematical Operations")
        print("1. Calculate Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Circle")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            n = int(input("Enter Number: "))
            print("Factorial =", math.factorial(n))

        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            t = float(input("Time: "))

            amount = p * (1 + r/100) ** t
            print("Compound Interest =", round(amount - p, 2))
            print("Total Amount =", round(amount, 2))

        elif ch == "3":
            angle = float(input("Enter Angle: "))
            print("sin =", round(math.sin(math.radians(angle)), 2))
            print("cos =", round(math.cos(math.radians(angle)), 2))
            print("tan =", round(math.tan(math.radians(angle)), 2))

        elif ch == "4":
            r = float(input("Enter Radius: "))
            print("Area =", round(math.pi * r * r, 2))

        elif ch == "5":
            break

        else:
            print("Invalid Choice")
