# Student Management System (Python + SQL)

# aa program python ane SQLite database use kari student records manage kare che

import sqlite3

# database connection create karvu 
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Student table create karvu (jo already na hoy toh)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER               
)
""")
conn.commit()


# student add karva mate function

def add_student():
    try:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = int(input("Enter your Marks: "))
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (sid, name, marks))
        conn.commit()
        print("Student Record Added Successfully")
    except sqlite3.IntegrityError:
        print("This ID already exist")
    except ValueError:
        print("ID and Marks should be in Numbers only")



# badha students display karva mate

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if records:
        print("\n--- Student Records ---")
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Marks: {row[2]}")
    else:
        print("There is no Record of Student")


# student search karva mate

def search_student():
    sid = int(input("Enter the Student ID for Search: "))
    cursor.execute("SELECT * FROM students where id = ?", (sid,))
    record = cursor.fetchone()

    if record:
        print(f"ID: {record[0]} | Name: {record[1]} | Marks: {record[2]}")
    else:
        print("Student not Found")



# student marks update karva mate

def update_marks():
    sid = int(input("Enter Student ID: "))
    new_marks = int(input("Enter New Marks: "))
    cursor.execute("UPDATE students SET marks = ? where id = ?", (new_marks, sid))
    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found")
    else:
        print("Marks updated Successfully")


# student delete karva mate

def delete_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("DELETE FROM students where id = ?", (sid,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found")
    else:
        print("Student Record deleted Successfully")


# Main Menu

def menu():
    while True:
        print("\n==== Student Managment System =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Program is Closed.")
            break
        else:
            print("Invalid Choice")


# program start
menu()

# database connection pn close karvu
conn.close()