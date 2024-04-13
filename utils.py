import random
import string

def generate_password(n_letters, n_numbers, n_symbols):
    """Generate random password with number of letters, numbers and symbols defined by user"""
    letters = "".join(random.sample(string.ascii_letters, n_letters))
    numbers = "".join(random.sample(string.digits, n_numbers))
    symbols = "".join(random.sample(string.punctuation, n_symbols))
    password = letters + numbers + symbols
    return "".join(random.sample(password, len(password)))

def get_input(prompt, range=None):
    """Force user to input number. If range provided, input must be in range."""
    while True:
        try:
            value = int(input(prompt))
            if not range or range[0] <= value <= range[1]:
                return value
            print("[!] Invalid input.  Try again")
        except ValueError:
            print("[!] Invalid input.  Try again")
