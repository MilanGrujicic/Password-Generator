from logo import logo
from utils import *

print(logo)

MAX_LENGTH = 30
MIN_LENGTH = 8
remaining = MAX_LENGTH - 2  # at least 1 lettter, number and special character

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

password = generate_password(letters, numbers, special)
print(f"[+] Your password: {password}")
