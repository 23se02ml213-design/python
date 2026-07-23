def write_file():
    text = input("Enter text: ")
    f = open("data.txt", "w")
    f.write(text)
    f.close()
    print("Data Written Successfully")

def read_file():
    try:
        f = open("data.txt", "r")
        print(f.read())
        f.close()
    except:
        print("File Not Found")

def append_file():
    text = input("Enter text: ")
    f = open("data.txt", "a")
    f.write("\n"+text)
    f.close()
    print("Data Added Successfully")
