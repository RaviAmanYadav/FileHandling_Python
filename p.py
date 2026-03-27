# class Student:
#     def __init__(self, name, father_name, mother_name, roll_no, grades):
#         self.name = name
#         self.father_name = father_name
#         self.mother_name = mother_name
#         self.roll_no = roll_no
#         self.grades = grades  # Dictionary format: {"Subject": "Grade"}

#     def display_info(self):
#         print(f"\n--- Student Report: {self.name} ---")
#         print(f"Roll No: {self.roll_no}")
#         print(f"Father's Name: {self.father_name}")
#         print(f"Mother's Name: {self.mother_name}")
#         print("Grades:")
#         for subject, grade in self.grades.items():
#             print(f"  - {subject}: {grade}")

# def manage_school():
#     students = {}

#     while True:
#         print("\n--- School Management System ---")
#         print("1. Add New Student")
#         print("2. Search Student by Roll No")
#         print("3. Exit")

#         choice = input("Select an option (1-3): ")

#         if choice == '1':
#             name = input("Enter Student Name: ")
#             f_name = input("Enter Father's Name: ")
#             m_name = input("Enter Mother's Name: ")
#             roll = input("Enter Roll Number: ")

#             # Entering grades
#             grades = {}
#             try:
#                 num_subs = int(input("How many subjects to add? "))
#                 for _ in range(num_subs):
#                     sub = input("Enter Subject Name: ")
#                     grd = input(f"Enter Grade for {sub}: ")
#                     grades[sub] = grd

#                 students[roll] = Student(name, f_name, m_name, roll, grades)
#                 print(f"\n[Success] Student {name} added successfully!")
#             except ValueError:
#                 print("[Error] Please enter a valid number for subjects.")

#         elif choice == '2':
#             roll = input("Enter Roll Number to search: ")
#             if roll in students:
#                 students[roll].display_info()
#             else:
#                 print("\n[Error] Student record not found.")

#         elif choice == '3':
#             print("Exiting system. Goodbye!")
#             break
#         else:
#             print("[Error] Invalid choice. Please try again.")

# # Run the program
# if __name__ == "__main__":
#     manage_school()


# This is simplest Student data management program in python


# Create class "Student"
# class Student:

#     # Constructor
#     def __init__(self, name, rollno, m1, m2):
#         self.name = name
#         self.rollno = rollno
#         self.m1 = m1
#         self.m2 = m2

#     # Function to create and append new student
#     def accept(self, Name, Rollno, marks1, marks2):

#         # use ' int(input()) ' method to take input from user
#         ob = Student(Name, Rollno, marks1, marks2)
#         ls.append(ob)

#     # Function to display student details
#     def display(self, ob):
#         print("Name : ", ob.name)
#         print("RollNo : ", ob.rollno)
#         print("Marks1 : ", ob.m1)
#         print("Marks2 : ", ob.m2)
#         print("\n")

#     # Search Function
#     def search(self, rn):
#         for i in range(ls.__len__()):
#             if ls[i].rollno == rn:
#                 return i

#     # Delete Function
#     def delete(self, rn):
#         i = obj.search(rn)
#         del ls[i]

#     # Update Function
#     def update(self, rn, No):
#         i = obj.search(rn)
#         roll = No
#         ls[i].rollno = roll


# # Create a list to add Students
# ls = []
# # an object of Student class
# obj = Student("", 0, 0, 0)

# print("\nOperations used, ")
# print(
#     "\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit"
# )

# # ch = int(input("Enter choice:"))
# # if(ch == 1):
# obj.accept("A", 1, 100, 100)
# obj.accept("B", 2, 90, 90)
# obj.accept("C", 3, 80, 80)

# # elif(ch == 2):
# print("\n")
# print("\nList of Students\n")
# for i in range(ls.__len__()):
#     obj.display(ls[i])

# # elif(ch == 3):
# print("\n Student Found, ")
# s = obj.search(2)
# obj.display(ls[s])

# # elif(ch == 4):
# obj.delete(2)
# print(ls.__len__())
# print("List after deletion")
# for i in range(ls.__len__()):
#     obj.display(ls[i])

# # elif(ch == 5):
# obj.update(3, 2)
# print(ls.__len__())
# print("List after updation")
# for i in range(ls.__len__()):
#     obj.display(ls[i])

# # else:
# print("Thank You !")



class Student:
	def __init__(self):
		self.student_details = {}
 
	@property
	def input_student_details(self):	# input student details
		roll_number = input("Enter Roll Number : ")
		name = input("Enter Student Name : ")
		marks = float(input("Enter Marks : "))
		self.student_details[roll_number] = {'name': name, 'marks': marks}
		print("Marks Added successfully")
 
	def update_student_marks(self):	  # update student marks
		roll_number = input("Enter Roll Number of the Student to Update Marks : ")
		if roll_number in self.student_details:
			new_marks = float(input("Enter New Marks : "))
			self.student_details[roll_number]['marks'] = new_marks
			print("Marks updated successfully")
		else:
			print("Student not found")
 
	def print_student_details(self):	# print student details
		roll_number = input("Enter Roll Number of the student to view details : ")
		if roll_number in self.student_details:
			student = self.student_details[roll_number]
			print("Roll Number :", roll_number)
			print("Student Name :", student['name'])
			print("Marks :", student['marks'])
		else:
			print("Student not found")
 
obj = Student()
 
while True:
    print("\n ********* Student Management System *********  ")
    print("\n1. Input Student Details")
    print("2. Update Student Marks")
    print("3. Print Student Details")
    print("4. Exit")
 
    choice = input("\nEnter your Choice (1 to 4): ")
 
    if choice == '1':
        obj.input_student_details
    elif choice == '2':
        obj.update_student_marks()
    elif choice == '3':
        obj.print_student_details()
    elif choice == '4':
        print("Exiting the program")
        break
    else:
        print("Invalid Choice. Please Try Again !!!")

