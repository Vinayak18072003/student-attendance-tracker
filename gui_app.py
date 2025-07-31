import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import date
from openpyxl import Workbook
from tkinter import filedialog
import os

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"

students = []
attendance_record = {}

def load_data():
    students.clear()
    attendance_record.clear()
    
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
        if any(s['id'] == sid for s in students):
            messagebox.showerror("Duplicate", "Student ID already exists!")
            return
        students.append({"name": name, "id": sid})
        save_students()
        messagebox.showinfo("Success", "Student added successfully!")

def delete_student():
    if not students:
        messagebox.showinfo("Delete Student", "No students to delete.")
        return
    sid = simpledialog.askstring("Delete Student", "Enter student ID to delete:")
    if not sid:
        return
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            save_students()
            messagebox.showinfo("Deleted", f"Student {s['name']} removed.")
            return
    messagebox.showwarning("Not Found", "Student ID not found.")

def view_students():
    if not students:
        messagebox.showinfo("Student List", "No students found.")
        return
    sorted_students = sorted(students, key=lambda s: s['name'])
    msg = "\n".join([f"{s['name']} (ID: {s['id']})" for s in sorted_students])
    messagebox.showinfo("Student List", msg)

def mark_attendance():
    if not students:
        messagebox.showinfo("Attendance", "No students to mark.")
        return
    today = str(date.today())
    present_ids = []
    for s in sorted(students, key=lambda s: s['name']):
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
    msg = ""
    for d, ids in attendance_record.items():
        present_names = [s['name'] for s in students if s['id'] in ids]
        msg += f"{d}: {len(present_names)} Present\n"
        msg += f"    → {', '.join(sorted(present_names))}\n"
    messagebox.showinfo("Attendance Records", msg)

def export_attendance_to_excel():
    if not attendance_record:
        messagebox.showinfo("Export", "No attendance data to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance Report"

    # Header Row
    sorted_students = sorted(students, key=lambda s: s['name'])
    ws.append(["Date"] + [s["name"] for s in sorted_students])

    # Attendance Rows
    for date_str, present_ids in attendance_record.items():
        row = [date_str]
        for s in sorted_students:
            row.append("Present" if s["id"] in present_ids else "Absent")
        ws.append(row)

    wb.save(file_path)
    messagebox.showinfo("Export Successful", f"Attendance exported to:\n{file_path}")

# GUI Window
def main_gui():
    load_data()
    win = tk.Tk()
    win.title("Student Attendance Tracker")
    win.geometry("320x350")

    tk.Button(win, text="Add Student", command=add_student, width=25).pack(pady=5)
    tk.Button(win, text="Delete Student", command=delete_student, width=25).pack(pady=5)
    tk.Button(win, text="View Students", command=view_students, width=25).pack(pady=5)
    tk.Button(win, text="Mark Attendance", command=mark_attendance, width=25).pack(pady=5)
    tk.Button(win, text="View Attendance", command=view_attendance, width=25).pack(pady=5)
    tk.Button(win, text="Export to Excel", command=export_attendance_to_excel, width=25).pack(pady=5)
    tk.Button(win, text="Exit", command=win.destroy, width=25).pack(pady=20)

    win.mainloop()

if __name__ == "__main__":
    main_gui()
