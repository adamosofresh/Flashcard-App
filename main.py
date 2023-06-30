from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(view, image=front_card_image)
    flip_timer = window.after(3000, func=flip)

def flip():
    canvas.itemconfig(view, image=back_card_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
view = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

new_card()





window.mainloop()