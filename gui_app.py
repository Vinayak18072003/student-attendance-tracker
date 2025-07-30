import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import date
import os

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"

students = []
attendance_record = {}

def load_data():
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                name, sid = line.strip().split(",")
                students.append({"name": name, "id": sid})

    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            for line in f:
                date_str, ids = line.strip().split(":")
                attendance_record[date_str] = ids.split(",")

def save_students():
    with open(STUDENT_FILE, "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['id']}\n")

def save_attendance():
    with open(ATTENDANCE_FILE, "w") as f:
        for d, ids in attendance_record.items():
            f.write(f"{d}:{','.join(ids)}\n")

def add_student():
    name = simpledialog.askstring("Student Name", "Enter student name:")
    sid = simpledialog.askstring("Student ID", "Enter student ID:")
    if name and sid:
        students.append({"name": name, "id": sid})
        save_students()
        messagebox.showinfo("Success", "Student added successfully!")

def view_students():
    if not students:
        messagebox.showinfo("Student List", "No students found.")
        return
    msg = "\n".join([f"{s['name']} (ID: {s['id']})" for s in students])
    messagebox.showinfo("Student List", msg)

def mark_attendance():
    if not students:
        messagebox.showinfo("Attendance", "No students to mark.")
        return
    today = str(date.today())
    present_ids = []
    for s in students:
        response = messagebox.askyesno("Mark Attendance", f"{s['name']} (ID: {s['id']}) Present?")
        if response:
            present_ids.append(s['id'])
    attendance_record[today] = present_ids
    save_attendance()
    messagebox.showinfo("Saved", f"Attendance for {today} saved!")

def view_attendance():
    if not attendance_record:
        messagebox.showinfo("Attendance", "No records found.")
        return
    msg = "\n".join([f"{d}: {len(ids)} students present" for d, ids in attendance_record.items()])
    messagebox.showinfo("Attendance Records", msg)

# GUI Window
def main_gui():
    load_data()
    win = tk.Tk()
    win.title("Student Attendance Tracker")
    win.geometry("300x300")

    tk.Button(win, text="Add Student", command=add_student, width=20).pack(pady=5)
    tk.Button(win, text="View Students", command=view_students, width=20).pack(pady=5)
    tk.Button(win, text="Mark Attendance", command=mark_attendance, width=20).pack(pady=5)
    tk.Button(win, text="View Attendance", command=view_attendance, width=20).pack(pady=5)
    tk.Button(win, text="Exit", command=win.destroy, width=20).pack(pady=20)

    win.mainloop()

if __name__ == "__main__":
    main_gui()
