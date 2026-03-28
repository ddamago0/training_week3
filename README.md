# # Daily Status Persistence System

This is a simple Python CLI program that allows users to save and manage their daily blockers using a text file.

---

## 📌 Description

The program simulates a "Team Daily Status" system where users can:

* Add a daily blocker
* Fetch (read) all saved blockers
* Overwrite the file if needed

The data is stored in a file called `database.txt`, allowing persistence between executions.

---

## 🚀 Features

* Save blockers using append mode (`a`)
* Read blockers using read mode (`r`)
* Overwrite file using write mode (`w`)
* Input validation to prevent empty values
* Error handling to avoid crashes

---

## ▶️ How to Run

1. Open terminal
2. Navigate to the project folder
3. Run:

```bash
python persistence_log.py
```

---

## 📁 Project Structure

```
week3_project/
│
├── persistence_log.py
└── database.txt
```

---

## ⚠️ Notes

* The program checks if the file exists before reading or overwriting.
* Invalid inputs are handled to prevent errors.
* The file is automatically closed using the `with open()` statement.

---

## 👨‍💻 Author

Daniel David Martinez Gonzalez - English practice project
