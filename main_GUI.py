from logo import logo
from utils import *
from tkinter import *

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("GUI")
        self.window.config(bg="#FF3131")
        self.window.geometry("500x600")

        # LOGO
        self.logo = PhotoImage(file="logo.png")  # Load the image

        # Create a canvas with the size of the logo or larger
        canvas_width = self.logo.width()
        canvas_height = self.logo.height()
        canvas = Canvas(self.window, width=canvas_width, height=canvas_height, bg="#004AAD", highlightthickness=0)
        canvas.grid(row=0, column=0)

        # Centering the image in the canvas
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.logo)

        # BUTTONS
        self.close_button = Button(text="Exit", width=10, bg="#fff500", highlightbackground = "black", border="2", command=self.window.destroy)
        self.close_button.grid(row=1, column=0)

        self.window.mainloop()

if __name__ == "__main__":
    app = GUI()
