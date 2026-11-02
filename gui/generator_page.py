import tkinter as tk
from tkinter import messagebox
from core.password_generator import generate_password

BG = "#EDF2F7"
NAVY = "#20354A"
TEAL = "#168C8C"


class GeneratorPage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG)

        tk.Label(self, text="Password Generator",
                 font=("Arial", 24, "bold"),
                 bg=BG, fg=NAVY).pack(pady=25)

        tk.Label(self, text="Password Length",
                 bg=BG, fg=NAVY).pack()

        self.length = tk.IntVar(value=12)

        tk.Scale(
            self, from_=8, to=64,
            orient="horizontal",
            variable=self.length,
            length=300, bg=BG
        ).pack(pady=10)

        self.upper = tk.BooleanVar(value=True)
        self.lower = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar(value=True)

        for name, var in [
            ("Uppercase", self.upper),
            ("Lowercase", self.lower),
            ("Numbers", self.numbers),
            ("Symbols", self.symbols)
        ]:
            tk.Checkbutton(
                self, text=name, variable=var,
                bg=BG, fg=NAVY
            ).pack()

        tk.Button(
            self, text="Generate Password",
            command=self.generate,
            bg=TEAL, fg="white",
            relief="flat", padx=15, pady=7
        ).pack(pady=20)

        self.output = tk.Entry(
            self, width=35, font=("Arial", 13),
            justify="center", show="*"
        )
        self.output.pack(pady=10)

        self.visible = tk.BooleanVar()

        tk.Checkbutton(
            self, text="Show Password",
            variable=self.visible,
            command=lambda: self.output.config(
                show="" if self.visible.get() else "*"
            ), bg=BG, fg=NAVY
        ).pack()

        tk.Button(
            self, text="Copy Password",
            command=self.copy,
            bg=TEAL, fg="white",
            relief="flat"
        ).pack(pady=12)

    def generate(self):
        password = generate_password(
            self.length.get(),
            self.upper.get(),
            self.lower.get(),
            self.numbers.get(),
            self.symbols.get()
        )

        if not password:
            messagebox.showwarning(
                "Warning", "Select valid password options"
            )
            return

        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def copy(self):
        if self.output.get():
            self.clipboard_clear()
            self.clipboard_append(self.output.get())
            messagebox.showinfo("Copied", "Password copied successfully")