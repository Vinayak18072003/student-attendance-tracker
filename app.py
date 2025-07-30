# app.py - Milestone 2: Add/View Students + Attendance

from datetime import date

students = []
attendance_record = {}  # Key: date, Value: list of present student IDs

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    students.append({"name": name, "id": student_id})
    print(f"Student {name} added successfully.\n")

def view_students():
    if not students:
        print("No students added yet.\n")
        return
    print("\nList of Students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student['name']} (ID: {student['id']})")
    print()

def mark_attendance():
    if not students:
        print("No students to mark attendance.\n")
        return

    today = str(date.today())
    present_ids = []

    print(f"\nMarking attendance for {today}")
    for student in students:
        status = input(f"Is {student['name']} (ID: {student['id']}) present? (y/n): ").strip().lower()
        if status == 'y':
            present_ids.append(student['id'])

    attendance_record[today] = present_ids
    print("\nAttendance recorded.\n")

def view_attendance():
    if not attendance_record:
        print("No attendance records found.\n")
        return

    print("\nAttendance Records:")
    for record_date, present_ids in attendance_record.items():
        print(f"{record_date}: {len(present_ids)} present")
    print()

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance Records")
        print("5. Exit")
        choice = input("Choose an option: ")

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
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
