import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "italic"))
my_label.pack(side="right")

window.mainloop()
