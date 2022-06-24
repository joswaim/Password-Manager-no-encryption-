from tkinter import *
from tkinter import messagebox
import random


EMAIL = "test@testmail.test"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Missing required information")

    else:

        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}",
                                       message=f"These are the details entered:\nEmail: {email_entry.get()}"
                                               f"\nPassword: {password_entry.get()}\n Is this ok to save?")

        if is_ok:
            pass_data = open("data.txt", "a")
            pass_data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            pass_data.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        else:
            pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
mypass_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_png)
canvas.grid(column=1, row=0, padx=(40, 0))

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=(5, 0))

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, pady=(5, 0))
email_entry.insert(index=0, string=EMAIL)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=(5, 0))

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3, pady=(5, 0))

pass_gen_button = Button(text="Generate Password", width=15, command=generate_password)
pass_gen_button.grid(column=2, row=3, padx=(0, 41), pady=(5, 0))

add_pass_button = Button(text="Add", width=44, command=save)
add_pass_button.grid(column=1, row=4, columnspan=2, pady=(5, 0))

window.mainloop()
