from tkinter import *
import random
import string

random_string = string.ascii_letters + string.digits + string.punctuation

root = Tk()

root.title('Password Generator')

root.geometry("450x300")


def generatePasswordButtonClicked():
    lenght = int(userInput.get())
    password = ''.join(random.sample(random_string, lenght))
    resultLabel.configure(text="Password: " + password)


def cancelButtonClicked():
    root.destroy()


generateButton = Button(root, text='Create Password',
                        command=generatePasswordButtonClicked)

generateButton.grid(row=0, column=0)

closeButton = Button(root, text='Close', command=cancelButtonClicked)

closeButton.config(bg='#9FD996')

closeButton.grid(row=1, column=0)

userInput = Entry(root, width=10)

userInput.grid(row=2, column=0)

resultLabel = Label(root, text="Password: ")

resultLabel.grid(row=3, column=0)

root.mainloop()
