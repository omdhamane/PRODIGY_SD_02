import tkinter as tk
from tkinter import messagebox
import random

# store game values
number = 0
attempts = 0
limit = 100


def new_game():
    """Start or restart the game"""
    global number, attempts, limit

    level = level_var.get()

    if level == "Easy":
        limit = 50
    elif level == "Hard":
        limit = 200
    else:
        limit = 100

    number = random.randint(1, limit)
    attempts = 0

    attempts_label.config(text="Attempts: 0")
    status_label.config(
        text=f"Guess a number between 1 and {limit}",
        fg="#cbd5f5"
    )
    entry_guess.delete(0, tk.END)


def check_number(event=None):
    """Check user's guess"""
    global attempts

    try:
        guess = int(entry_guess.get())

        if guess < 1 or guess > limit:
            raise ValueError

        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        difference = abs(number - guess)

        if guess > number:
            show_hint("Too High", difference)
        elif guess < number:
            show_hint("Too Low", difference)
        else:
            status_label.config(
                text=f"🎉 Correct! You won in {attempts} attempts",
                fg="#22c55e"
            )
            messagebox.showinfo(
                "Congratulations",
                f"You guessed the number in {attempts} attempts!"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            f"Please enter a number between 1 and {limit}"
        )


def show_hint(text, diff):
    """Show hint based on how close the guess is"""
    if diff <= 5:
        status_label.config(text=f"{text} (Very close!)", fg="#facc15")
    elif diff <= 15:
        status_label.config(text=f"{text} (Close)", fg="#fb923c")
    else:
        status_label.config(text=text, fg="#ef4444")


# ---------- Window setup ----------

window = tk.Tk()
window.title("Guessing Game")
window.geometry("520x460")
window.resizable(False, False)
window.configure(bg="#0f172a")

# main container (card style)
card = tk.Frame(window, bg="#020617", width=420, height=360)
card.place(relx=0.5, rely=0.5, anchor="center")

# title
tk.Label(
    card,
    text="🎯 Guessing Game",
    font=("Segoe UI", 20, "bold"),
    bg="#020617",
    fg="white"
).pack(pady=(20, 10))

# difficulty selection
tk.Label(
    card,
    text="Select Difficulty",
    bg="#020617",
    fg="#94a3b8",
    font=("Segoe UI", 10)
).pack()

level_var = tk.StringVar(value="Medium")
tk.OptionMenu(card, level_var, "Easy", "Medium", "Hard").pack(pady=6)

# input field
tk.Label(
    card,
    text="Enter your guess",
    bg="#020617",
    fg="#94a3b8",
    font=("Segoe UI", 10)
).pack(pady=(12, 0))

entry_guess = tk.Entry(
    card,
    font=("Segoe UI", 14),
    bg="#020617",
    fg="white",
    insertbackground="white",
    justify="center",
    relief="flat"
)
entry_guess.pack(ipady=6, pady=8)
entry_guess.bind("<Return>", check_number)

# buttons
btn_frame = tk.Frame(card, bg="#020617")
btn_frame.pack(pady=12)

tk.Button(
    btn_frame,
    text="Check Guess",
    command=check_number,
    bg="#2563eb",
    fg="white",
    width=14,
    relief="flat",
    cursor="hand2"
).grid(row=0, column=0, padx=6)

tk.Button(
    btn_frame,
    text="New Game",
    command=new_game,
    bg="#334155",
    fg="white",
    width=14,
    relief="flat",
    cursor="hand2"
).grid(row=0, column=1, padx=6)

# game info
attempts_label = tk.Label(
    card,
    text="Attempts: 0",
    bg="#020617",
    fg="#94a3b8",
    font=("Segoe UI", 10)
)
attempts_label.pack()

status_label = tk.Label(
    card,
    text="",
    bg="#020617",
    fg="white",
    font=("Segoe UI", 12)
)
status_label.pack(pady=14)

# start first game
new_game()
window.mainloop()
