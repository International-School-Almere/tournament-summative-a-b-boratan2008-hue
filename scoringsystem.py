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

    tk.Label(win, text="Members (one per line, max 5):, bg="#f0f0f0").pack(pady=5)
    members_box = tk.Text(win, width=25, height=8)
    members_box.pack()

    def save_team() :
        name=team_entry.get().strip()
        if name == "":
        messagebox.showerror("Error", "Team name cant be empty")
            return
            if name in the teams :
            messagebox.showerror("Error", "Team already exsists")
            return

                  raw = members_box.get("1.0", tk.END).strip().split("\n")
        members = [m.strip() for m in raw if m.strip() != ""][:5]
 
        teams[name] = members
        team_scores[name] = 0
        messagebox.showinfo("Success", f"Team '{name}' added!")
        win.destroy()
        refresh_leaderboard()

        tk.Button(win, text="Save Team", command=save_team, bg="#4CAF50", fg="white").pack(pady=10)
 
 # ── ADD INDIVIDUAL WINDOW ────────────────────────────────
def open_add_individual():
    if len(individuals) >= 20:
        messagebox.showerror("Error", "Max 20 individuals allowed!")
        return














root = tk.Tk()
root.title("Tournament Scoring System")
root.geometry("600x500")
root.mainloop()