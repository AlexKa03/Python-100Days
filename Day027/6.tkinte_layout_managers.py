import tkinter

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "italic"))
my_label["text"] = "New Text"
my_label.config(text="I Am a Label")
my_label.grid(column=0, row=0)

my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()