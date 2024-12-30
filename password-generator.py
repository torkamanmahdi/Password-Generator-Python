import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables
        self.password_length = tk.IntVar(value=12)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_letters = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.easy_to_read = tk.BooleanVar(value=False)
        self.password_strength = tk.StringVar(value="Weak")

        # GUI Elements
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = ttk.Entry(root, textvariable=self.password_length)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(root, text="Include Letters", variable=self.include_letters).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(root, text="Easy to Read", variable=self.easy_to_read).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        ttk.Button(root, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.password_display = ttk.Label(root, text="", font=("Arial", 12))
        self.password_display.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(root, text="Password Strength:").grid(row=7, column=0, padx=10, pady=10)
        self.strength_meter = ttk.Label(root, textvariable=self.password_strength, font=("Arial", 12))
        self.strength_meter.grid(row=7, column=1, padx=10, pady=10)

    def generate_password(self):
        length = self.password_length.get()
        include_numbers = self.include_numbers.get()
        include_letters = self.include_letters.get()
        include_symbols = self.include_symbols.get()
        easy_to_read = self.easy_to_read.get()

        characters = ""
        if include_numbers:
            characters += string.digits
        if include_letters:
            characters += string.ascii_letters
        if include_symbols:
            characters += string.punctuation

        if easy_to_read:
            characters = characters.replace("l", "").replace("I", "").replace("1", "").replace("O", "").replace("0", "")

        if not characters:
            self.password_display.config(text="Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.config(text=password)
        self.update_password_strength(password)

    def update_password_strength(self, password):
        strength = 0
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c.isalpha() for c in password):
            strength += 1
        if any(c in string.punctuation for c in password):
            strength += 1
        if len(password) >= 12:
            strength += 1

        if strength == 4:
            self.password_strength.set("Strong")
            self.strength_meter.config(foreground="green")
        elif strength >= 2:
            self.password_strength.set("Medium")
            self.strength_meter.config(foreground="orange")
        else:
            self.password_strength.set("Weak")
            self.strength_meter.config(foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
