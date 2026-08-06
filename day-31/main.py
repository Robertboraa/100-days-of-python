from tkinter import *
import pandas
import random

BACKGROUND = "#B1DDC6"

df = pandas.read_csv("Es.csv")
lang_dict = df.set_index("Espanol")["English"].to_dict()
words_to_learn = lang_dict.copy()
current_card = {}
flip_timer = None
def get_random_word():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = {}
    spanish = random.choice(list(words_to_learn.keys()))
    current_card["Espanol"] = spanish
    current_card["English"] = words_to_learn[spanish]
    canvas.itemconfig(card_img_item, image=front_img)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=spanish, fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_img_item, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def known():
    words_to_learn.pop(current_card["Espanol"])
    get_random_word()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND)

front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
wrong_img = PhotoImage(file="wrong.png")
right_img = PhotoImage(file="right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
card_img_item = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, bg=BACKGROUND, command=get_random_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, bd=0, bg=BACKGROUND, command=known)
right_button.grid(row=1, column=1)



get_random_word()
window.mainloop()