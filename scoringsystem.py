# Tournament Scoring Sytem
# BTEC Unit 4 Programming
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# storing data
teams = {}
individuals = {}
team_scores = {}
events = []

# points for each place
points = {1: 10, 2: 7, 3: 5, 4: 3, 5: 1}


# ── ADD TEAM WINDOW ──────────────────────────────────────
def open_add_team():
    if len(teams) >= 4:
        messagebox.showerror("Error", "Max 4 teams allowed!")
        return
 
    win = tk.Toplevel(root)
    win.title("Add Team")
    win.geometry("300x350")
    win.config(bg="#f0f0f0")
 
    tk.Label(win, text="Team Name:", bg="#f0f0f0").pack(pady=5)
    team_entry = tk.Entry(win, width=25)
    team_entry.pack()

