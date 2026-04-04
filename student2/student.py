import os
import json
from typing import Dict

FILE = os.path.join("FileHandling_Python", "student2", "student.json")


class Parents:
    def __init__(self, fname: str, mname: str):
        self.fname = fname
        self.mname = mname

    def to_dict(self) -> Dict:
        return {"father_name": self.fname, "mother_name": self.mname}


class StudentManage:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        if os.path.exists(self.filePath):
            try:
                with open(self.filePath, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def _generate_roll(self) -> int:
        if not self.data:
            return 1
        return max(map(int, self.data.keys())) + 1

    def _save_data(self):
        """Saving data into student.json"""
        with open(self.filePath, "w") as f:
            json.dump(self.data, f, indent=4)

    def addStudent(self):
        name = input("Enter student name => ")
        fname = input("Enter father's name => ")
        mname = input("Enter mother's name => ")
        parent = Parents(fname, mname)
        roll = self._generate_roll()
        self.data[str(roll)] = {"name": name, "parent": parent.to_dict()}
        self._save_data()
        print(f"student roll number {roll} has been successfully admitted.")

    def viewStudent(self):
        if not self.data:
            print("No data present")
            return
        for roll, details in self.data.items():
            print("Roll number => ", roll)
            print("Name => ", details["name"])
            print("Father's Name => ", details["parent"]["father_name"])
            print("Mother's Name => ", details["parent"]["mother_name"])

    def searchStudent(self):
        if not self.data:
            print("No data present")
            return
        roll = input("Enter roll number => ")
        if roll in self.data:
            student = self.data[roll]
            print("Roll number => ", roll)
            print("Name => ", student["name"])
            print("Father's name => ", student["parent"]["father_name"])
            print("Mother's name => ", student["parent"]["mother_name"])


if __name__ == "__main__":
    manager = StudentManage(FILE)

    while True:
        print("1. Add student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Exit")
        choice = int(input("Enter your choice => "))
        match choice:
            case 1:
                manager.addStudent()
            case 2:
                manager.viewStudent()
            case 3:
                manager.searchStudent()
            case 4:
                exit()
            case _:
                print("Invalid operation")
