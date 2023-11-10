import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Sign-in Form")
window.geometry('340x440')
window.configure(bg = 'black')

def login():
    username = 'rafi'
    password = '12345'
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title = 'Login Success', message = 'You successfully logged in ')
    else:
        messagebox.showerror(title="Error", message="Invalid login.")




Sign_label = tk.Label(window, text="Sign In", bg='black', fg="white", font=("sans-serif", 30))
email_label = tk.Label(window, text="Email", bg='black', fg="white", font=("sans-serif", 16))
username_entry = tk.Entry(window, font=("sans-serif", 16))
password_entry = tk.Entry(window, show="*", font=("sans-serif", 16))
password_label = tk.Label(window, text="Password", bg='black', fg="white", font=("sans-serif", 16))
login_button = tk.Button(window, text="Login", bg="red", fg="white", font=("sans-serif", 16), command = login)

Sign_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
email_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=30)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=30)
login_button.grid(row=3, column=0, columnspan=2, pady=30)




window.mainloop()