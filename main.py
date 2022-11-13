import random
import string

# Generate string with all letters, numbers and symbols
random_string = string.ascii_letters + string.digits + string.punctuation

# Variable type verification
while True:
    try:
        lenght = int(
            input("Choose the lenght of the password (Only integer)\n> "))
    except ValueError:
        print("This is an unaccepted response, enter a valid value")
        continue
    else:
        break

# Creates password based on user's input
password = ''.join(random.sample(random_string, lenght))
print(password)
