import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, tk.END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if website != "" and email != "" and password != "":
        is_ok = messagebox.askokcancel(title="Password Save", message=f"These are the details entered:\n"
                                                                            f"Email: {email}\nPassword: {password}\n"
                                                                            f"Is it ok to save?")
        if is_ok:
            with open(f"data.txt", mode="a") as output_data:
                output_data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, tk.END)
                pass_entry.delete(0, tk.END)
    else:
        messagebox.showerror(title="Oops", message="Please fill in all fields!")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = tk.Label(text="Email/ Username:")
user_label.grid(row=2, column=0)
pass_label = tk.Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
user_entry = tk.Entry()
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "business@akadiyski.com")
pass_entry = tk.Entry()
pass_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_pass_btn = tk.Button(text="Generate Password", command=password_generator)
generate_pass_btn.grid(row=3, column=2, sticky="EW")
add_btn = tk.Button(text="Add", command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()

window.mainloop()