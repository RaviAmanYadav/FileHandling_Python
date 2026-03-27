import json
import os

FILE = "FileHandling_Python/students.json"


def addStudent():
    # Load existing data
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
        except:
            data = {}  # if the file is empty
    else:
        data = {}

    # Auto generated roll number
    if data:
        last_roll = max(map(int, data.keys()))
        new_roll = last_roll + 1
    else:
        new_roll = 1

    # Input
    studentName = input("Enter student name => ")
    fatherName = input("Enter Father's name => ")
    motherName = input("Enter mother's name => ")

    # Store data
    data[str(new_roll)] = {
        "name": studentName,
        "father": fatherName,
        "mother": motherName,
    }

    # Save
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Student added with roll number : {new_roll} Successfully.\n")


def showStudent():
    if not os.path.exists(FILE):
        print("Data not found")
        return
    else:
        with open(FILE, "r") as f:
            data = json.load(f)

        for roll, details in data.items():
            print(f"Roll number => {roll}")
            print(f"Name => {details["name"]}")
            print(f"Father's Name => {details["father"]}")
            print(f"Mother's Name => {details["mother"]}")
            print("-" * 20)


def searchStudent():
    if not os.path.exists(FILE):
        print("Data file not found")
        return
    print("Searching student")
    roll = input("Enter the roll number => ")
    with open(FILE, "r") as f:
        data = json.load(f)

    if roll in data:
        print("Student Data")
        print(f"Roll number => {roll}")
        print(f"Student's Name => {data[roll]['name']}")
        print(f"Father's Name => {data[roll]['father']}")
        print(f"Mother's Name => {data[roll]['mother']}")
    else:
        print("Roll number not found.")


while True:
    print("1. Add student")
    print("2. Show student")
    print("3. Search Student")
    print("4. Exit.")
    choice = int(input("Enter your choice => "))
    match choice:
        case 1:
            addStudent()
        case 2:
            showStudent()
        case 3:
            searchStudent()
        case 4:
            exit()
        case _:
            print("Invalid operations")
