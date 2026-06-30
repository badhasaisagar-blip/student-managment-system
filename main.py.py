import sqlite3

DATABASE = "students.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students(name, roll, department) VALUES (?, ?, ?)",
            (name, roll, department)
        )
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Roll number already exists.")

    conn.close()


def view_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n----- Student Records -----")

    if not students:
        print("No students found.")

    for student in students:
        print(student)

    conn.close()


def search_student():
    roll = input("Enter Roll Number: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student not found.")

    conn.close()


def update_student():
    roll = input("Enter Roll Number: ")

    name = input("New Name: ")
    department = input("New Department: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, department=? WHERE roll=?",
        (name, department, roll)
    )

    conn.commit()

    if cursor.rowcount:
        print("Student updated.")
    else:
        print("Student not found.")

    conn.close()


def delete_student():
    roll = input("Enter Roll Number: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()

    if cursor.rowcount:
        print("Student deleted.")
    else:
        print("Student not found.")

    conn.close()


def menu():
    create_table()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()