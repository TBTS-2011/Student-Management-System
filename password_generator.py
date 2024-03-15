
from tkinter import *

import random

root = Tk()

root.geometry("400x175")

# Declaring a variable of string type and this variable will be used to store the password generated
passstr = StringVar()

# Declaring a variable of integer type which will be used to store the length of the password entered by the user
passlen = IntVar()

passlen.set(8)

def generate():
    # Storing the keys in a Matrix which will be used to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    password = ""

    # Loop to generate the random password of the length entered by the user
    for x in range(passlen.get()):
        password += random.choice(pass1)  # Using the shorthand notation for string concatenation

    # Declaring the password to the entry widget
    passstr.set(password)


Label(root, text="Password Generating Application", font="arial 15").pack()

Label(root, text="Enter password length").pack(pady=4)

# Creating a entry widget to take password length entered by the user
Entry(root, textvariable=passlen).pack(pady=4)

# Button to call the generate function
Button(root, text="Generate your Password", command=generate).pack(pady=8)

# Entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=4)

# This part is for developer's preview only, and can only be viewd in their consoles
print("NOTE: This Password Generating Application cannot support clipboard copying, but this feature will soon arrive in the next upcoming version.")

root.mainloop()
