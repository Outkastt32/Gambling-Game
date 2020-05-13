from tkinter import *
import random

num = random.randint(0, 10)
if num >= 0 and num <= 5:
    mes = "Player 1 Wins!"
elif num >= 6 and num <= 10:
    mes = "Player 2 Wins!"

def main():
    root = Tk()
    root.geometry("300x250")
    root.title("Gambling Game")
    #Remember to add this next line ALWAYS


    Label(root, text = mes, bg = "grey", font = ("Courier", 13, "normal")).pack()

    root.mainloop()

main()