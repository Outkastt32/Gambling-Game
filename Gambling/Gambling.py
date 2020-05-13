from tkinter import *
import random

bal = input("How many chips: ")
print("You have %s chips." % bal )


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

Label( text = "How Many Chips") 

e1 = Entry()

Label( text = mes, bg = "grey", font = ("Courier", 13, "normal")).pack()

mainloop()

main()