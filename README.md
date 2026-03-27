# 🎓 Student Management System (Python)

A simple **Student Management System** built using Python and file handling (JSON).
This project allows you to **add, view, search, update, and delete student records** using a command-line interface.

---

## 🚀 Features

* ➕ Add new student
* 📋 View all students
* 🔍 Search student by roll number
* ✏️ Update student details *(optional / if implemented)*
* ❌ Delete student record *(optional / if implemented)*
* 💾 Data stored in JSON file

---

## 🛠️ Technologies Used

* Python 3
* File Handling
* JSON

---

## 📁 Project Structure

```
student_management_system/
│
├── student.py        # Main program
├── students.json     # Data file
└── README.md         # Project documentation
```

---

## ▶️ How to Run

1. Clone the repository or download the code
2. Open terminal in project folder
3. Run the program:

```
python3 student.py
```

---

## 🧑‍💻 How It Works

The system uses a **menu-driven program**:

```
1. Add Student
2. Show Students
3. Search Student
4. Exit
```

* Data is stored in `students.json`
* Each student has a unique **roll number**
* Data is stored using Python **dictionary (hash map)**

---

## 📌 Example Data Format

```
{
    "1": {
        "name": "Aman Yadav",
        "fname": "Ramadhar Yadav",
        "mname": "Pushpa Yadav"
    }
}
```

---

## 🧠 Concepts Learned

* File handling in Python
* JSON data storage
* CRUD operations (Create, Read, Update, Delete)
* Dictionary (HashMap) usage
* Basic DSA (searching)

---

## 🔥 Future Improvements

* Search by name
* GUI version (Tkinter / Web)
* Database integration (SQLite / POSTGRESQL)
* User authentication system

---

## 🤝 Contributing

Feel free to fork this project and improve it.

---

## 📜 License

This project is open-source and free to use.

---

## ⭐ Author

**Aman Yadav**
