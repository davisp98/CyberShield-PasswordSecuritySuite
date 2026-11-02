import tkinter as tk
from gui.analyzer_page import AnalyzerPage
from gui.generator_page import GeneratorPage
from gui.comparison_page import ComparisonPage

BG = "#EDF2F7"
NAVY = "#20354A"
TEAL = "#168C8C"


class Dashboard(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("CyberShield")
        self.geometry("1100x700")
        self.configure(bg=BG)

        self.sidebar = tk.Frame(self, bg=NAVY, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="CYBERSHIELD",
                 font=("Arial", 19, "bold"),
                 bg=NAVY, fg="white").pack(pady=35)

        self.content = tk.Frame(self, bg=BG)
        self.content.pack(fill="both", expand=True)

        pages = [
            ("Dashboard", self.home),
            ("Password Analyzer", AnalyzerPage),
            ("Password Generator", GeneratorPage),
            ("Password Comparison", ComparisonPage)
        ]

        for name, page in pages:
            tk.Button(
                self.sidebar, text=name,
                command=lambda p=page: self.show(p),
                bg=NAVY, fg="white",
                activebackground=TEAL,
                activeforeground="white",
                relief="flat", font=("Arial", 11),
                width=22, pady=12
            ).pack(pady=5)

        self.home()

    def show(self, page):
        for widget in self.content.winfo_children():
            widget.destroy()

        if page == self.home:
            self.home()
        else:
            page(self.content).pack(fill="both", expand=True)

    def home(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(
            self.content, text="Welcome to CyberShield",
            font=("Arial", 26, "bold"),
            bg=BG, fg=NAVY
        ).pack(pady=(150, 15))

        tk.Label(
            self.content,
            text="Advanced Password Security Suite",
            font=("Arial", 15), bg=BG, fg=TEAL
        ).pack()


if __name__ == "__main__":
    Dashboard().mainloop()