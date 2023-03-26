import random
import string
from logo import logo

print(logo)

# Generate string with all letters, numbers and symbols

def generate_password(n_letters, n_numbers, n_symbols):
    letters = "".join(random.sample(string.ascii_letters, n_letters))
    numbers = "".join(random.sample(string.digits, n_numbers))
    symbols = "".join(random.sample(string.punctuation, n_symbols))
    password = letters + numbers + symbols
    return "".join(random.sample(password, len(password)))


# Variable type verification
while True:
    try:
        length = int(input("[-] Choose the length of the password (Only integer): "))
        while length <= 0:
            length = int(input("[!] Please insert a positive integer: "))
        letters = int(input("[-] How many letters: "))
        while letters >= length:
            letters = int(input(f"[!] Amount of letters cannot be bigger than the password lenght, please insert a number lesser than {length}: "))
        numbers = int(input("[-] How many numbers: "))
        while numbers + letters > length:
            numbers = int(input(f"[!] Amount of numbers plus letter cannot be bigger than the password lenght, please insert a number lesser than {length - letters}: "))
        symbols = int(input("[-] How many symbols: "))
        while numbers + letters + symbols > length:
            symbols = int(input(f"[!] Amount of symbols plus letters and numbers cannot be bigger than the password lenght, please insert a number lesser than {length - letters - numbers}: "))
    except ValueError:
        print("[!] Invalid input, please enter an integer number")
        continue
    else:
        break
        
# Creates password based on user's input
password = generate_password(letters, numbers, symbols)
print(f"[+] Your password: {password}")
