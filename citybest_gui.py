import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import date

# --- Database Connection ---
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CityBestSchoolDB"
    )

# --- Login Function ---
def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT role FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            role = result[0]
            messagebox.showinfo("Login Success", f"Welcome {username} ({role})")
            login_frame.pack_forget()
            show_main_menu(role)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

# --- Add Student ---
def add_student():
    def save_student():
        fname = fname_entry.get()
        lname = lname_entry.get()
        dob = dob_entry.get()
        gender = gender_var.get()
        class_id = class_id_entry.get()
        guardian_name = guardian_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        enrollment_date = date.today()

        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = """
                INSERT INTO students (fname, lname, date_of_birth, gender, class_id, guardian_name, contact_number, address, enrollment_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (fname, lname, dob, gender, class_id, guardian_name, contact, address, enrollment_date)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student added successfully.")
            student_window.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    student_window = tk.Toplevel(root)
    student_window.title("Add Student")

    tk.Label(student_window, text="First Name").grid(row=0, column=0)
    fname_entry = tk.Entry(student_window)
    fname_entry.grid(row=0, column=1)

    tk.Label(student_window, text="Last Name").grid(row=1, column=0)
    lname_entry = tk.Entry(student_window)
    lname_entry.grid(row=1, column=1)

    tk.Label(student_window, text="Date of Birth (YYYY-MM-DD)").grid(row=2, column=0)
    dob_entry = tk.Entry(student_window)
    dob_entry.grid(row=2, column=1)

    tk.Label(student_window, text="Gender").grid(row=3, column=0)
    gender_var = tk.StringVar()
    tk.OptionMenu(student_window, gender_var, "Male", "Female").grid(row=3, column=1)

    tk.Label(student_window, text="Class ID").grid(row=4, column=0)
    class_id_entry = tk.Entry(student_window)
    class_id_entry.grid(row=4, column=1)

    tk.Label(student_window, text="Guardian Name").grid(row=5, column=0)
    guardian_entry = tk.Entry(student_window)
    guardian_entry.grid(row=5, column=1)

    tk.Label(student_window, text="Contact Number").grid(row=6, column=0)
    contact_entry = tk.Entry(student_window)
    contact_entry.grid(row=6, column=1)

    tk.Label(student_window, text="Address").grid(row=7, column=0)
    address_entry = tk.Entry(student_window)
    address_entry.grid(row=7, column=1)

    tk.Button(student_window, text="Save", command=save_student).grid(row=8, column=0, columnspan=2)

# --- Main Menu ---
def show_main_menu(role):
    menu_frame = tk.Frame(root)
    menu_frame.pack()

    tk.Label(menu_frame, text="--- CITYBEST SCHOOL SYSTEM ---", font=("Arial", 16)).pack()
    tk.Button(menu_frame, text="Add Student", command=add_student).pack()
    # You can add more buttons here for other features

# --- Root Window ---
root = tk.Tk()
root.title("CityBest School System")

# --- Login Frame ---
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=2, column=0, columnspan=2)

root.mainloop()
