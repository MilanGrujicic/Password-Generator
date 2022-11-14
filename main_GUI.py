from tkinter import *
import random
import string

random_string = string.ascii_letters + string.digits + string.punctuation

root = Tk()

root.title(
    'Password Generator - Generate password with lenght from 1 to 94 characters')

window_width = 400
window_height = 200

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width / 10)
center_y = int(screen_height/2 - window_height / 10)

# Set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


def generatePasswordButtonClicked():
    try:
        lenght = int(userInput.get())
    except ValueError:
        resultLabel.configure(text="Wrong input")
    else:
        password = ''.join(random.sample(random_string, lenght))
        resultLabel.configure(text="Password: " + password)


def cancelButtonClicked():
    root.destroy()


generateButton = Button(root, text='Create Password',
                        command=generatePasswordButtonClicked)

generateButton.pack()

closeButton = Button(root, text='Close', command=cancelButtonClicked)

closeButton.config(bg='#9FD996')

closeButton.pack()

userInput = Entry(root, width=10)

userInput.pack()

resultLabel = Label(root, text="Password: ")

resultLabel.pack()

root.mainloop()
