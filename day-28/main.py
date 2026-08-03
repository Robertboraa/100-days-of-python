from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
timer_id = None
reps = 0
checks = ""
# ---------------------------- TIMER RESET ------------------------------- #
def add_check():
    global checks
    checks += "✅"
    check_marks.config(text=checks)
def reset_timer():
    global timer_id , reps,checks
    reps = 0
    if timer_id:
        window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="0:00")
    checks = ""
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        label1.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)

    elif reps % 2 == 1:
        label1.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)
        add_check()
    elif reps % 2 == 0:
        label1.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer_id
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        timer_id = window.after(1000, countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW , highlightthickness=0)
canvas.grid(row=0, column=1)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(112, 100 , image=tomato_img)
timer_text = canvas.create_text(105, 125, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.pack()


label1 = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"),fg=GREEN, bg=YELLOW)
label1.place(x=70 , y=-50)

check_marks = Label(text="" , bg=YELLOW, fg=GREEN)
check_marks.place(x=100 , y=220)

button1 = Button(text="Start", command=lambda: start_timer(), highlightbackground=YELLOW)
button2 = Button(text="Reset", command= lambda:reset_timer(),highlightbackground=YELLOW)
button1.place(x=-20,y= 200)
button2.place(x=180,y= 200)




window.mainloop()