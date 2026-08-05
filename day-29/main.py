# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
from tkinter import *
from tkinter import messagebox


def generate_password():
    password_entry.delete(0, END)
    length = random.randint(8, 20)

    num_numbers = random.randint(1, 3)
    num_special = random.randint(1, 3)
    num_letters = length - num_numbers - num_special

    letters = random.choices(string.ascii_letters, k=num_letters)
    numbers = random.choices(string.digits, k=num_numbers)
    special = random.choices("!@#$%^&*()", k=num_special)

    password = letters + numbers + special
    random.shuffle(password)

    password_entry.insert(0, f"{''.join(password)}")


import json


def search():
    website = website_entry.get()

    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No passwords saved yet.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo("Not Found", f"No details for {website}.")

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    website_entry.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50 )


# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # Add your logo file here
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your@email.com")  # default email

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2 )

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
# Search Button
search_button = Button(text="Search", width=10, height=1,command=search)
search_button.grid(row=1, column=2, columnspan=1)
window.mainloop()
