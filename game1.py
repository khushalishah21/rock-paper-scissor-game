from random import randint
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Rock  Scissor  Paper")
root.configure(background="green")

rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\com_stone.jpeg"))
sci_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\com_sci.jpeg"))
paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\com_paper.jpeg"))
rocku = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\user_stone.jpeg"))
sciu = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\user_sci.jpeg"))
paperu = ImageTk.PhotoImage(Image.open("C:\\Users\\Khushali\\Downloads\\user_paper.jpeg"))


com_label = Label(root, image=sci_img,bg="green")
user_label = Label(root, image=sciu,bg="green")

com_label.grid(row=1, column=0)
user_label.grid(row=1, column=12)

#scores..
playerscore = Label(root, text=0, font=100, bg="green", fg="white")
computerscoe= Label(root, text=0, font=100, bg="green", fg="white")
computerscoe.grid(row=1 ,column=1)
playerscore.grid(row=1 ,column=3)

#indicator
user_indicator = Label(root, font=50, text="USER", bg="green", fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER", bg="green", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

#messages
msg = Label(root, font=50, bg="green", fg="white",text="You Loose")
msg.grid(row=3, column=2)

#update messages
def updatemessage(x):
    msg['text']=x

#update user score
def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

#update computer score
def updatecomscore():
    score = int(computerscoe["text"])
    score += 1
    computerscoe["text"] = str(score)

#check winner
def checkwin(player, computer):
    if player == computer:
        updatemessage("It is tie!!!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("You loose")
            updatecomscore()
        else:
            updatemessage("You win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemessage("You loose")
            updatecomscore()
        else:
            updatemessage("You win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updatemessage("You loose")
            updatecomscore()
        else:
            updatemessage("You win")
            updateuserscore()
    else:
        pass


#update choices

choices = ["rock", "paper", "scissor"]
def updatechoices(x):

    #computer int random
    compchoices = choices[randint(0, 2)]
    if compchoices == "rock":
        com_label.configure(image = rock_img)
    elif compchoices == "scissor":
        com_label.configure(image = sci_img)
    else:
        com_label.configure(image = paper_img)


#user
    if x=="rock":
        user_label.configure(image = rocku)
    elif x=="paper":
        user_label.configure(image = paperu)
    else:
        user_label.configure(image = sciu)

    checkwin(x,compchoices)

#button

rock = Button(root ,width=20, height=2 ,text="ROCK" , bg="purple", fg="white", command=lambda : updatechoices("rock")).grid(row=2, column=1)
paper = Button(root ,width=20, height=2 ,text="PAPER" , bg="blue", fg="white", command=lambda : updatechoices("paper")).grid(row=2, column=2)
scissor = Button(root ,width=20, height=2 ,text="SCISSOR" , bg="red", fg="white", command=lambda : updatechoices("scissor")).grid(row=2, column=3)

root.mainloop()