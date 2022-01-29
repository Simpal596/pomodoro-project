from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
REPS = 1
CHECK_SIGN = ""
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_clock():
    global CHECK_SIGN, TIMER, REPS
    window.after_cancel(TIMER)
    REPS = 1
    label_timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    label_checkbox.config(text="", fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
    canvas.itemconfig(canvas_text, text="00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global REPS, CHECK_SIGN, TIMER
    count_min = count // 60
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_second}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        print(CHECK_SIGN)
        print(REPS)
        if REPS % 2 == 0:
            CHECK_SIGN += "✔"
            label_checkbox.config(text=CHECK_SIGN)
        clock()

# ---------------------------- TIMER MECHANISM ------------------------------- #


def clock():
    global REPS, TIMER
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS > 8:
        window.after_cancel(TIMER)
    elif REPS % 8 == 0:
        label_timer.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)
        REPS += 1
    elif REPS % 2 == 0:
        label_timer.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
        REPS += 1
    elif REPS % 2 != 0:
        count_down(work_min_sec)
        label_timer.config(text="WORK", fg=GREEN)
        REPS += 1


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("POMODORO")

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 102, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# label
label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=1)
label_checkbox = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
label_checkbox.grid(row=2, column=1)

# button
button_start = Button(text="start", highlightthickness=0, command=clock)
button_start.grid(row=2, column=0)
button_reset = Button(text="reset", highlightthickness=0, command=reset_clock)
button_reset.grid(row=2, column=2)
window.mainloop()
