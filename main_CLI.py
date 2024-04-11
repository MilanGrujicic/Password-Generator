import random
import string
from logo import logo

print(logo)

MAX_LENGTH = 30
MIN_LENGTH = 8
remaining = MAX_LENGTH - 2  # at least 1 lettter, number and special character

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


# User inputs amount of special characters, numbers and letters
special = get_input(
    f"[-] How many special characters (1-{remaining}): ", (1, remaining)
)
remaining -= special + 1

if remaining > 2:
    numbers = get_input(f"[-] How many numbers (1-{remaining}): ", (1, remaining))
else:
    numbers = 1

remaining -= numbers + 1
if remaining > 1:
    min_letters = max(1, MIN_LENGTH - (special + numbers))
    letters = get_input(
        f"[-] How many letters ({min_letters}-{remaining}): ", (min_letters, remaining)
    )
else:
    letters = 1

# Creates password based on user's input
password = generate_password(letters, numbers, special)
print(f"[+] Your password: {password}")
