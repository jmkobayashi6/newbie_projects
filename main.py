import csv
import pandas
from random import choice
from tkinter import *
import json
import math
BACKGROUND_COLOR = "#B1DDC6"
ENGLISH_WORD = ""
french_data = ""
upload_df = ""
french_word = ""
dict_kiko = []
try:
  french_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
  french_data = pandas.read_csv("french_words.csv")


 ## -----------------      -------- WORDS IN CARDS ------------------------------- #
def click():
    global ENGLISH_WORD
    global french_word
    image.config(file="card_front.png")
    french_df = french_data.set_index('French')
    french_list = french_data["French"].to_list()
    french_word = choice(french_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="Black")
    ENGLISH_WORD = french_df.loc[french_word,"English"]





### make it into a dictionary where the french word is key to english word.
### randomly chose the key from a list




    # for (index, row) in french_data.iterrows():
    #     print(row.French)
    ## on click want french word
## ---------------------------- WRONG ------------------------------- #
def card_flip():
    global ENGLISH_WORD
    global french_word, dict_kiko
    canvas.itemconfig(card_image, image=back_image)
    canvas.grid(column=1, row=0, rowspan=2)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=ENGLISH_WORD, fill="White")
    dict = {"French": french_word , "English": ENGLISH_WORD}
    print(dict)
    dict_kiko.append(dict)
    print(dict_kiko)
    data = pandas.DataFrame(dict_kiko)
   # [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},
    data.to_csv("../Day31_Flash_Card/words_to_learn.csv", index=False)


    ###if flipped then also signal to global list these are the words that need to be practiced
    ### if checked this





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

#_____BACKGROUND______#
window['bg'] = 'black'
window.title("Flash Cards")
window.minsize(width=800, height=600)
window.config(padx=50,pady =5, bg=BACKGROUND_COLOR )




canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR )
image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
card_image = canvas.create_image(400, 200, image=image)
canvas.grid(column=1, row=0, rowspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))









#____BUTTONS_____#
right_image = PhotoImage(file="right.png")
right_button = Button(text="Click Me",  image=right_image, highlightthickness=0, command=click)
right_button.grid(row=2 ,column=2)
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(text="Click Me too!",  image =wrong_image, highlightthickness=0, command=card_flip)
wrong_button.grid(row=2, column=0)

#____Labels____#




window.mainloop()