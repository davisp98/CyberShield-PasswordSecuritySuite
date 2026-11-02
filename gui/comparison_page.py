import tkinter as tk
from tkinter import messagebox
from core.password_analyzer import analyze_password

BG = "#EDF2F7"
NAVY = "#20354A"
TEAL = "#168C8C"


class ComparisonPage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG)

        tk.Label(self, text="Password Comparison",
                 font=("Arial", 24, "bold"),
                 bg=BG, fg=NAVY).pack(pady=30)

        self.pass1 = tk.Entry(self, width=35, show="*",
                              font=("Arial", 12))
        self.pass1.pack(pady=12)

        self.pass2 = tk.Entry(self, width=35, show="*",
                              font=("Arial", 12))
        self.pass2.pack(pady=12)

        self.visible = tk.BooleanVar()

        tk.Checkbutton(
            self, text="Show Passwords",
            variable=self.visible,
            command=self.toggle,
            bg=BG, fg=NAVY
        ).pack()

        tk.Button(
            self, text="Compare Passwords",
            command=self.compare,
            bg=TEAL, fg="white",
            relief="flat", padx=15, pady=7
        ).pack(pady=20)

        self.result = tk.Label(
            self, text="", font=("Arial", 13),
            bg=BG, fg=NAVY, justify="left"
        )
        self.result.pack(pady=20)

    def toggle(self):
        mode = "" if self.visible.get() else "*"
        self.pass1.config(show=mode)
        self.pass2.config(show=mode)

    def compare(self):
        p1 = self.pass1.get()
        p2 = self.pass2.get()

        if not p1 or not p2:
            messagebox.showwarning("Warning", "Enter both passwords")
            return

        a = analyze_password(p1)
        b = analyze_password(p2)

        if a["score"] > b["score"]:
            winner = "Password 1 is stronger"
        elif b["score"] > a["score"]:
            winner = "Password 2 is stronger"
        else:
            winner = "Both passwords have equal scores"

        self.result.config(
            text=f"PASSWORD 1: {a['score']}/100 ({a['strength']})\n\n"
                 f"PASSWORD 2: {b['score']}/100 ({b['strength']})\n\n"
                 f"RESULT: {winner}"
        )