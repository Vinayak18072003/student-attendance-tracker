# app.py - Milestone 3: Persistent storage

import os
from datetime import date

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"

students = []
attendance_record = {}

# Load data from files
def load_data():
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                name, sid = line.strip().split(",")
                students.append({"name": name, "id": sid})

    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    date_str, ids = line.split(":")
                    attendance_record[date_str] = ids.split(",")

# Save student list to file
def save_students():
    with open(STUDENT_FILE, "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['id']}\n")

# Save attendance record to file
def save_attendance():
    with open(ATTENDANCE_FILE, "w") as f:
        for d, ids in attendance_record.items():
            f.write(f"{d}:{','.join(ids)}\n")

def add_student():
    name = input("Enter student name: ")
    sid = input("Enter student ID: ")
    students.append({"name": name, "id": sid})
    save_students()
    print(f"Student {name} added.\n")

def view_students():
    if not students:
        print("No students.\n")
        return
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. {s['name']} (ID: {s['id']})")
    print()

def mark_attendance():
    if not students:
        print("No students found.\n")
        return
    today = str(date.today())
    present_ids = []

    print(f"Marking attendance for {today}:")
    for s in students:
        status = input(f"{s['name']} (ID: {s['id']}) present? (y/n): ").strip().lower()
        if status == 'y':
            present_ids.append(s['id'])

    attendance_record[today] = present_ids
    save_attendance()
    print("Attendance saved.\n")

def view_attendance():
    if not attendance_record:
        print("No attendance records.\n")
        return
    for d, ids in attendance_record.items():
        print(f"{d}: {len(ids)} students present")
    print()

def main():
    load_data()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            view_attendance()
        elif choice == '5':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
