import tkinter as tk
from tkinter import messagebox
from core.password_analyzer import analyze_password
from core.vulnerability_checker import check_vulnerabilities

BG = "#EDF2F7"
NAVY = "#20354A"
TEAL = "#168C8C"


class AnalyzerPage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG)

        tk.Label(self, text="Password Analyzer",
                 font=("Arial", 24, "bold"),
                 bg=BG, fg=NAVY).pack(pady=25)

        self.password = tk.StringVar()
        self.visible = tk.BooleanVar()

        self.entry = tk.Entry(
            self, textvariable=self.password,
            show="*", width=38, font=("Arial", 13)
        )
        self.entry.pack(pady=10)

        tk.Checkbutton(
            self, text="Show Password",
            variable=self.visible,
            command=lambda: self.entry.config(
                show="" if self.visible.get() else "*"
            ),
            bg=BG, fg=NAVY
        ).pack()

        tk.Button(
            self, text="Analyze Password",
            command=self.analyze,
            bg=TEAL, fg="white",
            font=("Arial", 11, "bold"),
            relief="flat", padx=15, pady=7
        ).pack(pady=15)

        self.result = tk.Label(
            self, text="Enter a password to analyze",
            font=("Arial", 15, "bold"),
            bg=BG, fg=NAVY
        )
        self.result.pack(pady=10)

        self.details = tk.Label(
            self, text="", font=("Arial", 12),
            bg=BG, fg=NAVY
        )
        self.details.pack(pady=10)

        tk.Label(
            self, text="Security Report",
            font=("Arial", 14, "bold"),
            bg=BG, fg=NAVY
        ).pack(pady=5)

        self.report = tk.Text(
            self, height=15, width=65,
            font=("Arial", 10),
            bg="white", fg=NAVY,
            wrap="word"
        )
        self.report.pack(pady=5)

    def analyze(self):

        password = self.password.get()

        if not password:
            messagebox.showwarning("Warning", "Enter a password")
            return

        data = analyze_password(password)
        vulnerabilities = check_vulnerabilities(password)

        self.result.config(
            text=f"Strength: {data['strength']} ({data['score']}/100)"
        )

        self.details.config(
            text=f"Password Length: {data['length']}"
        )

        self.report.delete("1.0", tk.END)

        self.report.insert(tk.END, "SECURITY CHECKS\n\n")

        checks = [
            ("Minimum 8 characters", len(password) >= 8),
            ("Uppercase letters", any(c.isupper() for c in password)),
            ("Lowercase letters", any(c.islower() for c in password)),
            ("Numbers", any(c.isdigit() for c in password)),
            ("Special characters", any(not c.isalnum() for c in password))
        ]

        for name, passed in checks:
            status = "PASS" if passed else "FAIL"
            self.report.insert(tk.END, f"[{status}] {name}\n")

        self.report.insert(tk.END, "\nVULNERABILITIES DETECTED\n\n")

        if vulnerabilities:
            for issue in vulnerabilities:
                self.report.insert(tk.END, f"[WARNING] {issue}\n")
        else:
            self.report.insert(
                tk.END, "No vulnerabilities detected by basic checks.\n"
            )

        self.report.insert(tk.END, "\nRECOMMENDATIONS\n\n")

        recommendations = []

        if len(password) < 12:
            recommendations.append("Use at least 12 characters.")

        if not any(c.isupper() for c in password):
            recommendations.append("Include uppercase letters.")

        if not any(c.islower() for c in password):
            recommendations.append("Include lowercase letters.")

        if not any(c.isdigit() for c in password):
            recommendations.append("Include numbers.")

        if not any(not c.isalnum() for c in password):
            recommendations.append("Include special characters.")

        if vulnerabilities:
            recommendations.append(
                "Avoid common passwords and predictable patterns."
            )

        if recommendations:
            for item in recommendations:
                self.report.insert(tk.END, f"- {item}\n")
        else:
            self.report.insert(
                tk.END, "Continue using unique passwords for each account.\n"
            )