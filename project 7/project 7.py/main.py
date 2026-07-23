from datetime import datetime
import time
import random
import uuid

import file_module
import math_module
from mypackage.helper import welcome


def main():

    while True:

        welcome()

        print("\nChoose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifier (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # Date Time
        if choice == "1":

            while True:
                print("\nDatetime and Time Operations")
                print("1. Display Current Date and Time")
                print("2. Format Date")
                print("3. Stopwatch")
                print("4. Countdown Timer")
                print("5. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    print("Current Date and Time:")
                    print(datetime.now())

                elif ch == "2":
                    print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

                elif ch == "3":
                    input("Press Enter to Start")
                    start = time.time()
                    input("Press Enter to Stop")
                    end = time.time()

                    print("Time:",
                          round(end-start,2),
                          "seconds")

                elif ch == "4":
                    n = int(input("Enter seconds: "))

                    while n > 0:
                        print(n)
                        time.sleep(1)
                        n -= 1

                    print("Time Over")

                elif ch == "5":
                    break


        # Math
        elif choice == "2":
            math_module.menu()


        # Random
        elif choice == "3":

            print("\nRandom Data Generation")
            print("Random Number:",
                  random.randint(1,100))

            print("Random Choice:",
                  random.choice(
                  ["Python","Java","C++"]))


        # UUID
        elif choice == "4":

            print("\nGenerated UUID:")
            print(uuid.uuid4())


        # File
        elif choice == "5":

            while True:

                print("\nFile Operations")
                print("1. Write File")
                print("2. Read File")
                print("3. Append File")
                print("4. Back")

                f = input("Enter choice: ")

                if f == "1":
                    file_module.write_file()

                elif f == "2":
                    file_module.read_file()

                elif f == "3":
                    file_module.append_file()

                elif f == "4":
                    break


        # dir()
        elif choice == "6":

            print("\nModule Attributes:")
            print(dir(random))


        # Exit
        elif choice == "7":

            print("\nThank You For Using Toolkit")
            break


        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
