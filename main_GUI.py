from logo import logo
from utils import *
from tkinter import *

class input():
    def __init__(self, type, value):
        self.type = type
        self.value = value

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("GUI")
        self.window.config(bg="#004AAD")
        self.window.geometry("500x500")

        # LOGO
        self.logo = PhotoImage(file="logo.png")  # Load the image

        # Create a canvas with the size of the logo or larger
        canvas_width = self.logo.width()
        canvas_height = self.logo.height()
        canvas = Canvas(self.window, width=canvas_width, height=canvas_height, bg="#004AAD", highlightthickness=0)
        canvas.grid(row=0, column=0)

        # Centering the image in the canvas
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.logo)
        
        self.window.mainloop()


if __name__ == "__main__":
    app = GUI()
