import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_img, image=front_card_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card['English'], fill="white")

def known_word():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

front_card_img = tk.PhotoImage(file="images/card_front.png")
back_card_img = tk.PhotoImage(file="images/card_back.png")
canvas = tk.Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=front_card_img)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

right_img = tk.PhotoImage(file="images/right.png")
right_btn = tk.Button(image=right_img, highlightthickness=0, bd=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=known_word)
right_btn.grid(row=1, column=1)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_btn = tk.Button(image=wrong_img, highlightthickness=0, bd=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()