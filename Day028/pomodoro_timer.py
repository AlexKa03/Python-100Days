import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 2
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    status_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 != 0 and reps % 2 != 0:
        countdown(work_sec)
        status_label.config(text="Work", fg=GREEN)
    elif reps % 8 != 0 and reps % 2 != 1:
        countdown(short_break_sec)
        status_label.config(text="Break", fg=PINK)
    else:
        countdown(long_break_sec)
        status_label.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60

    if count_secs == 0:
        count_secs = "00"
    elif count_secs <= 9:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

status_label = tk.Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
status_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = tk.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=2, column=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()