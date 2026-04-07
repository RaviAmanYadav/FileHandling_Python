# 📘 Student Management System (Python CLI)

A simple **Command Line Interface (CLI)** based Student Management System built using Python.  
This project allows you to **Add, View, Search, Update, and Delete student records** using JSON file storage.

---

## 🚀 Features

- ➕ **Add new student**
- 📋 **View all students**
- 🔍 **Search student by roll number**
- ✏️ **Update student details**
- ❌ **Delete student**
- 💾 **Persistent storage using JSON file**

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON** (for data storage)
- **OS module** (for file handling)

---

## 📂 Project Structure

```
FileHandling_Python/
│
└── student2/
    └── student.json   # Stores student data
```

---

## 🧠 How It Works

Think of this project like a **school register**:

- Each student gets a **unique roll number**
- Data is stored in a **JSON file (like a digital notebook)**
- Every operation (**add/update/delete**) updates that file

---

## ▶️ How to Run

### 1. Clone or Download the Project

```bash
git clone <your-repo-link>
cd <your-project-folder>
```

### 2. Run the Python File

```bash
python your_file_name.py
```

---

## 🧾 Menu Options

```
1. Add student
2. View Student
3. Search Student
4. Delete Student
5. Update Student
6. Exit
```

---

## 📌 Sample Data Format (`student.json`)

```json
{
    "1": {
        "name": "Aman",
        "parent": {
            "father_name": "Rajesh",
            "mother_name": "Sunita"
        }
    }
}
```

---

## ⚠️ Important Notes

- Make sure the folder **`FileHandling_Python/student2/`** exists before running
- If `student.json` is empty or corrupted, the system will handle it automatically
- Roll numbers are **auto-generated**

---

## 💡 Future Improvements

- Add input validation (no empty fields)
- Use database (**SQLite / MySQL**)
- Convert CLI → **GUI (Tkinter) or Web App**
- Add logging system
- Add authentication (Admin login)

---

## 🎯 Why This Project Matters

This project helps you understand:

- **File Handling in Python**
- **Object-Oriented Programming (OOP)**
- **CRUD Operations**
- **Real-world backend logic**

---

## 👨‍💻 Author

**Aman**  
Aspiring Python Developer 🚀

---

## ⭐ Pro Tip

This is not just a project — this is your **first step toward backend development**.

👉 Next step: Convert this into a **Flask / Django web app**  
👉 Then connect it to a **database**
