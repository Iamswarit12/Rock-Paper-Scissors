from tkinter import *
import random 

window = Tk()
window.geometry("500x275")
window.title("Rock, Paper and Scissers")
window.configure(bg="blue")

frame = Frame(master=window, width=450, height=200, bg="#8FBFFF")
var = ('Rock', 'Paper', 'Scissers')

computer1 = random.choice(var)
computer2 = random.choice(var)
computer3 = random.choice(var)

text_box = Text(master=frame, width=53, height = 3)

def rock():
    if computer1 == 'Rock':
        info = 'Computer chose rock! It was a tie!\n'
    if computer1 == 'Paper':
        info = 'Computer chose Paper! You lost!\n'
    if computer1 =='Scissers':
        info = 'Computer chose Scissors! You win\n'

    text_box.insert(END, info)

def paper():
    if computer2 == 'Rock':
        info = 'Computer chose Rock! You Won!\n'
    if computer2 == 'Paper':
        info = 'Computer chose Paper! It was a tie!\n'
    if computer2 == 'Scissers':
        info = 'Computer chose Scissors! You lose\n'

    text_box.insert(END, info)

def scissers():
    if computer3 == 'Rock':
        info = 'Computer chose rock! You lost!\n'
    elif computer3 == 'Paper':
        info = 'Computer chose Paper! You Win!\n'
    if computer3 == 'Scissers':
        info = 'Computer chose Scissors! It was a tie!\n'

    text_box.insert(END, info)

btn_rock = Button(command=rock, height=2, width=15, text="Rock", bg="forest green")
btn_paper = Button(command=paper, height=2, width=15, text="Paper", bg="forest green")
btn_scissers = Button(command=scissers , height=2, width=15, text="Scissers", bg="forest green")

btn_rock.place(x=42, y=20)
btn_paper.place(x=192, y=20)
btn_scissers.place(x=342, y=20)
frame.place(x=25, y=10)
text_box.place(x=10, y=135)

window.mainloop()