import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("student_form.db")
cursor = connection.cursor()

TABLE_NAME = "students"
STUDENT_NAME = "name"
STUDENT_GENDER = "gender"
STUDENT_AGE = "age"
STUDENT_COLLEGE = "college"
STUDENT_COURSE = "course"
STUDENT_ADDRESS = "address"
STUDENT_PHONE = "phone"

cursor.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_NAME + " TEXT, " +
                STUDENT_GENDER + " TEXT , " + STUDENT_AGE + " INTEGER , " + STUDENT_COLLEGE + " TEXT ," +
                STUDENT_COURSE + " TEXT , " + STUDENT_ADDRESS + " TEXT , " + STUDENT_PHONE + " INTEGER );")

root = tk.Tk()
root.title("Student Management System")

titleLabel = tk.Label(root,text="Student Application Form",fg="blue",font=("TimesNewRoman",30))
titleLabel.place(x=450,y=5)

nameLabel = tk.Label(root, text="Name",font=("Times New Roman",25))
nameLabel.place(x=450,y=100)

genderLabel = tk.Label(root, text="Gender",font=("Times New Roman",25))
genderLabel.place(x=450,y=160)

ageLabel = tk.Label(root, text="Age",font=("Times New Roman",25))
ageLabel.place(x=450,y=220)

collegeLabel = tk.Label(root, text="College",font=("Times New Roman",25))
collegeLabel.place(x=450,y=280)

courseLabel = tk.Label(root, text="Course",font=("Times New Roman",25))
courseLabel.place(x=450,y=340)

addressLabel = tk.Label(root, text="Address",font=("Times New Roman",25))
addressLabel.place(x=450,y=400)

phoneLabel = tk.Label(root, text="Phone",font=("Times New Roman",25))
phoneLabel.place(x=450,y=460)

nameEntry = tk.Entry(root,font=("Times New Roman",16))
nameEntry.place(x=650,y=110)

genderEntry = tk.Entry(root,font=("Times New Roman",16))
genderEntry.place(x=650,y=165)

ageEntry = tk.Entry(root,font=("Times New Roman",16))
ageEntry.place(x=650,y=225)

collegeEntry = tk.Entry(root,font=("Times New Roman",16))
collegeEntry.place(x=650,y=285)

courseEntry = tk.Entry(root,font=("Times New Roman",16))
courseEntry.place(x=650,y=345)

addressEntry = tk.Entry(root,font=("Times New Roman",16))
addressEntry.place(x=650,y=405)

phoneEntry = tk.Entry(root,font=("Times New Roman",16))
phoneEntry.place(x=650,y=465)

def take_input():
    name = nameEntry.get()
    gender = genderEntry.get()
    age = ageEntry.get()
    college = collegeEntry.get()
    course = courseEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()

    cursor.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_GENDER + " , " +
                   STUDENT_AGE + " , " + STUDENT_COLLEGE + " , " + STUDENT_COURSE + " , " +
                   STUDENT_ADDRESS + " , " + STUDENT_PHONE + ")  VALUES (?,?,?,?,?,?,?)",
                   (name,gender,age,college,course,address,phone))
    
    connection.commit()

    nameEntry.delete(0, 'end')
    genderEntry.delete(0, 'end')
    ageEntry.delete(0, 'end')
    collegeEntry.delete(0, 'end')
    courseEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    
    messagebox.showinfo("Success", "Data Saved Successfully.")

def display_data():
    display_window = tk.Toplevel(root)
    display_window.title("Student Data")

    titleLabel = tk.Label(display_window, text="Student Management System", fg="#06a099", width=40)
    titleLabel.config(font=("Sylfaen",30))
    titleLabel.pack()

    columns = (STUDENT_NAME, STUDENT_GENDER, STUDENT_AGE, STUDENT_COLLEGE, STUDENT_COURSE, STUDENT_ADDRESS, STUDENT_PHONE)
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)

    cursor.execute("SELECT * FROM " + TABLE_NAME)
    results = cursor.fetchall()

    for row in results:
        tree.insert('', 'end', values=row)

    tree.pack()

button = tk.Button(root, text="Add Student", font=("Times New Roman",16), command=lambda: take_input())
button.place(x=450,y=600)

displayButton = tk.Button(root, text="Display Data", font=("Times New Roman",16), command=lambda: display_data())
displayButton.place(x=700,y=600)

root.mainloop()
