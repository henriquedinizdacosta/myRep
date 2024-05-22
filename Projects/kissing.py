from os import system, name
from time import sleep
import keyboard as kb
from tkinter import *

class tkinter_window:

    root = Tk()
    root.title("Rizzing lord")
    root.minsize(500, 350)  # width, height
    root.geometry("300x300+50+50")  # width x height + x + y
    # label
    text = Label(root, text="Nothing will work unless you do.")
    text.pack()
    text2 = Label(root, text="- Maya Angelou")
    text2.pack()
    # buttons

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def nameCheck(name):
    if not all(letter.isalpha() for letter in name) or len(name) == 0:
        clear()
        print('not a valid input.')
        return True

# names
while True:
    person1 = input('person 1, what\'s your name?\n')
    if not nameCheck(person1):
        break
clear()
while True:
    person2 = input('person 2, what\'s your name?\n')
    if not nameCheck(person2):
        break
clear()

if person1 == person2:
    print('you can\'t kiss yourself.')
else:
    # asking
    while True:
        print(f'{person1}, do you wanna kiss {person2}? (y/n)')
        if kb.read_key() == 'y':
            kiss1 = True
            clear()
            break
        elif kb.read_key() == 'n':
            kiss1 = False
            clear()
            break
        elif kb.read_key():
            clear()
            print('no such option') 
    sleep(0.1)
    while True:
        print(f'{person2}, do you wanna kiss {person1}? (y/n)')
        if kb.read_key() == 'y':
            kiss2 = True
            clear()
            break
        elif kb.read_key() == 'n':
            kiss2 = False
            clear()
            break
        elif kb.read_key():
            clear()
            print('no such option')
    clear()

    # computing
    if kiss1 and kiss2:
        print('both are kissing! :)')
    elif kiss1:
        print(f'no kisses... {person2} don\'t want kisses. :(')
    elif kiss2:
        print(f'no kisses... {person1} don\'t want kisses. :(')
    else: 
        print('no one wanna kiss... ;(')

while True:
    print('\npress any key to finnish.')
    if kb.read_key():
        break
                    