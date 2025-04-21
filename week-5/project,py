import tkinter as tk
import csv
from tkinter import messagebox

def load_employees():
    employees = []
    with open("GIG-logistics.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employees.append(row)
    return employees


def submit():
    name = name_entry.get().strip().lower()
    dept = dept_entry.get().strip().lower()
    found = False
    department_members = []

    for emp in employee_data:
        if emp["Name"].strip().lower() == name and emp["Department"].strip().lower() == dept:
            found = True
            for e in employee_data:
                if e["Department"].strip().lower() == dept and e["Name"].strip().lower() != name:
                    department_members.append(e["Name"])
            break

    if found:
        msg = f"Welcome {name.title()}!\n\nOther members in {dept.title()}:\n" + "\n".join(department_members)
        messagebox.showinfo("Employee Found", msg)
    else:
        messagebox.showinfo("Not Found", "Sorry, this employee does not exist.")


employee_data = load_employees()


root = tk.Tk()
root.title("Employee Checker")
root.geometry("400x250")


name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

dept_label = tk.Label(root, text="Department:")
dept_label.pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)


root.mainloop()
