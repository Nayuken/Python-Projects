import sys
from tkinter import *
import sys, random
Res = "play"
Olist = ("Rock", "Paper", "Scissors")
#Gui Setup
root = Tk()
root.geometry('800x400')
root.title("RPS")
#Output
Res_text = Frame(root)
Res_text.place(width=250, height=100, x=260, y=300)
text = Label(Res_text, text=Res, fg='red', font=('Times New Roman', 40))
text.pack()

Score = 0
Score_text = Label(Score, text=Score, fg='red', font=('Times New Roman', 40))
Score_text.place(width=250, height=100, x=200, y=250)
Score_text.pack()
#functions definition
def res_text(Res):
    text.config(text=Res)
def sc_text(Score):
    Score_text.config(text=Score)


#function for rock:
def play_rock(event):
    x = random.choice(Olist)
    if x=="Rock":
        Res = "TIE"
        res_text(Res)
    elif x == "Paper":
        Res = "LOSE"
        res_text(Res)
    elif x == "Scissors":
        Res = "WIN"
        res_text(Res)
        sc_text(Score)
#function for paper:
def play_paper(event):
    x = random.choice(Olist)
    if x=="Paper":
        Res = "TIE"
        res_text(Res)
    elif x == "Scissors":
        Res = "LOSE"
        res_text(Res)
    elif x == "Rock":
        Res = "WIN"
        res_text(Res)
        sc_text(Score)
#function for scissors:
def play_scissors(event):
    x = random.choice(Olist)
    if x=="Scissors":
        Res = "TIE"
        res_text(Res)
    elif x == "Rock":
        Res = "LOSE"
        res_text(Res)
    elif x == "Paper":
        Res = "WIN"
        res_text(Res)
        sc_text(Score)

#Second Row: choice buttons
RPSLabel = Label(root, text = "Choose your Hand")
RPSLabel.pack()

rButton = Button(root, text= "Rock", width= 10)
rButton.bind("<Button-1>",play_rock)
rButton.place(x=250, y= 100)

pButton = Button(root, text= "Paper", width= 10)
pButton.bind("<Button-1>",play_paper)
pButton.place(x=350, y= 100)

sbutton = Button(root, text= "Scissors", width = 10)
sbutton.bind("<Button-1>",play_scissors)
sbutton.place(x=450, y= 100)


#Result
root.mainloop()
#End of Gui Setup