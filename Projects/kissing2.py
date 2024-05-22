from os import system, name
from time import sleep
import keyboard as kb
from tkinter import *

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
def nameCheck(name):
    if not all(letter.isalpha() for letter in name) or len(name) == 0:
        print('not a valid input.')
        return True

# window
root = Tk()
root.title("Rizz Lord")
root.geometry("400x320")  
root.maxsize(400, 320)
root.config()

# title label
title = Label(root, text="Rizz Lord", bg="#2176C1", fg='white', relief=RAISED)
title.pack(ipady=5, fill='x')
title.config(font=("Font", 30))

# p1 name Entry
person1_frame = Frame(root, bg="#6FAFE7")
person1_frame.pack()
Label(person1_frame, text="Person 1", bg="#6FAFE7").pack(side='left', padx=5)
person1_entry = Entry(person1_frame, bd=3)
person1_entry.pack(side='right')

# p2 name entry
person2_frame = Frame(root)
person2_frame.pack()
Label(person2_frame, text="Person 2", bg="#6FAFE7").pack(side='left', padx=7)
person2_entry = Entry(person2_frame, bd=3)
person2_entry.pack(side='right')

def checkInput():

    entered_person_1_name = person1_entry.get()  # get username from Entry widget
    entered_person_2_name = person2_entry.get()  # get password from Entry widget

    if not nameCheck(entered_person_1_name) and not nameCheck(entered_person_2_name):
        print("Hello!")
    else:
        print("Login failed: Invalid username or password.")
    
# Create Go! Button
go_button = Button(root, text="GO!", command=checkInput, bg="#6FAFE7", width=15)
go_button.pack(pady=5)

var = IntVar()

root.mainloop()