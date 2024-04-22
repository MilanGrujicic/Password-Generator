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
        canvas_height = self.logo.height() // 2.5
        canvas = Canvas(self.window, width=canvas_width, height=canvas_height, bg="#FF3131", highlightthickness=0)
        canvas.grid(row=0, column=0)

        # Centering the image in the canvas
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.logo)
        
        # WIDGETS

        self.numbers = Label(self.window, text="Letters", bg="#FF3131", fg="white")
        self.numbers.grid(row=1, column=0)

        self.scale_numbers = Scale(self.window, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground = "black", border="2")
        self.scale_numbers.grid(row=2, column=0, pady=5)

        self.letters = Label(self.window, text="Numbers", bg="#FF3131", fg="white")
        self.letters.grid(row=3, column=0)

        self.scale_letters = Scale(self.window, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground = "black", border="2")
        self.scale_letters.grid(row=4, column=0, pady=5)

        self.special_characters = Label(self.window, text="Special Characters", bg="#FF3131", fg="white")
        self.special_characters.grid(row=5, column=0)

        self.scale_special_characters = Scale(self.window, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground = "black", border="2")
        self.scale_special_characters.grid(row=6, column=0, pady=5)

        self.create_password = Button(text="Generate \nPassword", width=10, bg="#fff500", highlightbackground = "black", border="2", command=self.parse_scale_values_into_password)
        self.create_password.grid(row=7, column=0, pady=5)

        self.your_password_is = Label(text="Your password is: ",  bg="#FF3131", fg="white")
        self.your_password_is.grid_forget()

        self.password = Text(bg="#FF3131", fg="white", height=1, width=15, borderwidth=0)
        self.password.grid_forget()

        self.close_button = Button(text="Exit", width=10, bg="#fff500", highlightbackground = "black", border="2", command=self.window.destroy)
        self.close_button.grid(row=10, column=0)

        self.made_with_love_by_milan = Label(text="Made with love by Milan Grujicic", bg="#FF3131", fg="white", font=("Arial", 10, "italic")).place(x=0,y=580)

        self.window.mainloop()

    def parse_scale_values_into_password(self):
        numbers = self.scale_numbers.get()
        letters = self.scale_letters.get()
        special = self.scale_special_characters.get()
        password = generate_password(numbers, letters, special)
        self.make_output_visible(password)

    def make_output_visible(self, password):
        self.your_password_is.grid(row=8, column=0, pady=5)
        self.password.insert(END, password)
        self.password.configure(state="disabled")
        self.password.grid(row=9, column=0, pady=7)

if __name__ == "__main__":
    app = GUI()
