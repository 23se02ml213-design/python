from datetime import datetime
import os

class Journal:

    def add(self):
        try:
            f = open("journal.txt", "a")
            f.write("[" + str(datetime.now()) + "]\n")
            f.write(input("Enter Entry: ") + "\n\n")
            f.close()
            print("Entry Added")
        except:
            print("Error!")

    def view(self):
        try:
            f = open("journal.txt", "r")
            print(f.read())
            f.close()
        except:
            print("No File Found")

    def search(self):
        try:
            word = input("Enter Keyword: ")
            f = open("journal.txt", "r")
            data = f.read()
            if word in data:
                print("Entry Found")
                print(data)
            else:
                print("No Entry Found")
            f.close()
        except:
            print("No File Found")

    def delete(self):
        if os.path.exists("journal.txt"):
            ch = input("Delete All? (y/n): ")
            if ch == "y":
                os.remove("journal.txt")
                print("Deleted")
        else:
            print("No File Found")

obj = Journal()

while True:
    print("\n1.Add")
    print("2.View")
    print("3.Search")
    print("4.Delete")
    print("5.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        obj.add()
    elif ch == "2":
        obj.view()
    elif ch == "3":
        obj.search()
    elif ch == "4":
        obj.delete()
    elif ch == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")