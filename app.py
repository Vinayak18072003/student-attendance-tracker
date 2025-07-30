# app.py - Milestone 1: Add/View Students

students = []

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

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
