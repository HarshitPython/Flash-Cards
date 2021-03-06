from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image = card_back_img)

def is_right():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.config(padx=50, pady=50,bg = BACKGROUND_COLOR)

window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
card_background = canvas.create_image(400,263,image = card_front_img)
card_title = canvas.create_text(400,150,text = "title",font = ("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text = "Word",font = ("Arial",60,"bold"))
canvas.config(bg = BACKGROUND_COLOR)
canvas.grid(row=0, column=0,columnspan = 2)

right_img = PhotoImage(file="images/right.gif")
right_button = Button(image=right_img,highlightthickness=0,command=is_right)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
