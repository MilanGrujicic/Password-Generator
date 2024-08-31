from logo import logo
from utils import *
from tkinter import *
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.config(bg="#191919")
        self.window.geometry("500x712")

        # IMAGES
        self.logo = ImageTk.PhotoImage(file="images/logo.png")  # Load the logo.

        key_image = Image.open("images/key_icon.png")
        key_image = key_image.resize((20, 20))
        key_icon = ImageTk.PhotoImage(key_image)

        exit_image = Image.open("images/exit_icon.png")
        exit_image = exit_image.resize((20, 20))
        exit_icon = ImageTk.PhotoImage(exit_image)

        # Create a canvas with the size of the logo.
        canvas_width = self.logo.width()
        canvas_height = self.logo.height() // 2.9
        canvas = Canvas(self.window, width=canvas_width, height=canvas_height, bg="#191919", highlightthickness=0)
        canvas.grid(row=0, column=0)

        # Center the image in the canvas.
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.logo)

        # GUI components
        self.frame_scales = Frame(self.window, bg='#191919')
        self.frame_scales.grid(row=1, column=0, padx=100, sticky="nsew")
        self.frame_scales.grid_propagate(True)

        self.numbers = Label(self.frame_scales, text="Letters", bg="#191919", fg="white", font=("Helvetica", 12, "bold"))
        self.numbers.pack(pady=10, padx=10)

        self.scale_numbers = Scale(self.frame_scales, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground="black", border="2")
        self.scale_numbers.pack(pady=10, padx=10)

        self.letters = Label(self.frame_scales, text="Numbers", bg="#191919", fg="white", font=("Helvetica", 12, "bold"))
        self.letters.pack(pady=10, padx=10)

        self.scale_letters = Scale(self.frame_scales, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground="black", border="2")
        self.scale_letters.pack(pady=10, padx=10)

        self.special_characters = Label(self.frame_scales, text="Special Characters", bg="#191919", fg="white", font=("Helvetica", 12, "bold"))
        self.special_characters.pack(pady=10, padx=10)

        self.scale_special_characters = Scale(self.frame_scales, from_=0, to=10, orient=HORIZONTAL, bg="#fff500", highlightbackground="black", border="2")
        self.scale_special_characters.pack(pady=10, padx=10)

        self.output = Frame(self.window, bg="#191919")
        self.output.grid(row=2, column=0, padx=100, sticky="nsew")
        self.output.grid_propagate(True)

        self.create_password = Button(self.output, text="Generate \nPassword", width=80, bg="#fff500", highlightbackground="black", border="2", image=key_icon, compound=RIGHT, command=self.parse_scale_values_into_password)
        self.create_password.pack(pady=10, padx=10)

        self.your_password_is = Label(self.output, text="Your password is: ", bg="#191919", fg="white", font=("Helvetica", 10, "bold"))
        self.your_password_is.pack_forget()

        self.password = Text(self.output, bg="#191919", fg="white", height=1, width=15, borderwidth=0)
        self.password.pack_forget()

        self.footer = Frame(self.window, bg="#191919")
        self.footer.grid(row=3, column=0, padx=5, sticky="ew")
        self.output.grid_propagate(False)

        self.close_button = Button(self.footer, text="Exit", width=80, bg="#fff500", highlightbackground="black", border="2", image=exit_icon, compound=RIGHT, command=self.window.destroy)
        self.close_button.pack(pady=10, padx=10)

        self.made_with_love_by_milan = Label(text="Made with love by Milan Grujicic", bg="#191919", fg="white", font=("Helvetica", 10, "italic")).place(x=0,y=694)


        self.window.mainloop()

    def parse_scale_values_into_password(self):
        '''Once the button generate password is clicked, get values from scales and creates a password.'''
        numbers = self.scale_numbers.get()
        letters = self.scale_letters.get()
        special = self.scale_special_characters.get()
        password = generate_password(numbers, letters, special)
        if lambda:self.is_password_text_empty():
            self.make_output_visible(password)
        if lambda:not self.is_password_text_empty():
            self.password.configure(state="normal")
            self.password.delete('1.0', END)
            self.make_output_visible(password)

    def make_output_visible(self, password):
        '''Once the password is generated, display it to the user.'''
        self.your_password_is.pack(pady=10, padx=10)
        self.password.insert(END, password)
        self.password.configure(state="disabled")
        self.password.pack(pady=10, padx=10)

    def is_password_text_empty(self):
        '''Verify whether the field the password is displayed is empty or not.'''
        content = self.password.get("1.0", END).strip()  # Get the content of the Text widget.
        if not content:
            return False
        else:
            return True

if __name__ == "__main__":
    app = GUI()
