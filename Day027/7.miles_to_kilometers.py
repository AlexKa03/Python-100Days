import tkinter

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=round(km, 2))

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
input = tkinter.Entry(width=7)
input.grid(column=1, row=0)

# Labels
miles = tkinter.Label(text="Miles", font=("Arial", 24, "italic"))
miles.grid(column=2, row=0)

equal = tkinter.Label(text="is equal to", font=("Arial", 24, "italic"))
equal.grid(column=0, row=1)

result = tkinter.Label(text="0", font=("Arial", 24, "italic"))
result.grid(column=1, row=1)

kilometers = tkinter.Label(text="Km", font=("Arial", 24, "italic"))
kilometers.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()