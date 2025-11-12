import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"
# my_label.config(text="I Am a Label")

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
