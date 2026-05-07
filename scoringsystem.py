
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
 
 
# clear the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
 
 
# ── ADD TEAM SCREEN ──────────────────────────────────────
def add_team_screen():
 
    #replace previous screen
    clear_screen()
 
    if len(teams) >= 5:
        messagebox.showerror("Error", "Max 5 teams allowed!")
        return
 
    tk.Label(root, text="Team Name:", bg="#f0f0f0").pack(pady=5)
    team_entry = tk.Entry(root, width=25)
    team_entry.pack()
 
    Members_label = tk.Label(root, text="Members (one per line, max 5):", bg="#f0f0f0")
    Members_label.pack(pady=5)
 
    Member1 = tk.Entry(root, width=25)
    Member1.pack()
 
    Member2 = tk.Entry(root, width=25)
    Member2.pack()
 
    Member3 = tk.Entry(root, width=25)
    Member3.pack()
 
    Member4 = tk.Entry(root, width=25)
    Member4.pack()
 
    Member5 = tk.Entry(root, width=25)
    Member5.pack()
 
    def save_button():
        team_name = team_entry.get()
 
        # get the members
        members = []
        members.append(Member1.get())
        members.append(Member2.get())
        members.append(Member3.get())
        members.append(Member4.get())
        members.append(Member5.get())
 
        # remove the empty ones
        clean_members = []
        for m in members:
            if m != "":
                clean_members.append(m)
 
        # control
        if team_name == "":
            messagebox.showerror("Error","Team name required!")
            return
 
        # save in dictionary
        teams[team_name] = clean_members
        team_scores[team_name] = 0
 
        messagebox.showinfo("Success", "Team added!")
        main_menu()
 
    def return_button():
        main_menu()
 
    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack()
 
    back = tk.Button(root, text="return", anchor='center', command=return_button)
    back.pack()
 
 
# ── ADD INDIVIDUAL SCREEN ────────────────────────────────
def add_individual_screen():
    clear_screen()
 
    if len(individuals) >= 20:
        messagebox.showerror("Error", "Max 20 individuals allowed!")
        return
 
    tk.Label(root, text="Participant Name:").pack(pady=5)
    name_entry = tk.Entry(root, width=25)
    name_entry.pack()
 
    def save_button():
        name = name_entry.get()
 
        # check if empty
        if name == "":
            messagebox.showerror("Error", "Name cant be empty!")
            return
 
        # check if already exsists
        if name in individuals:
            messagebox.showerror("Error", "Already added!")
            return
 
        # save in dictionary
        individuals[name] = 0
 
        messagebox.showinfo("Success", name + " added!")
        main_menu()
 
    def return_button():
        main_menu()
 
    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack()
 
    back = tk.Button(root, text="return", anchor='center', command=return_button)
    back.pack()
 
 
# ── ADD EVENT SCREEN ─────────────────────────────────────
def add_event_screen():
    clear_screen()
 
    if len(events) >= 5:
        messagebox.showerror("Error", "Max 5 events allowed!")
        return
 
    tk.Label(root, text="Add Event", font=("Arial", 14, "bold")).pack(pady=10)
 
    tk.Label(root, text="Event Name:").pack()
    event_entry = tk.Entry(root, width=25)
    event_entry.pack()
 
    tk.Label(root, text="Event Type:").pack(pady=5)
    type_var = tk.StringVar(root)
    type_var.set("Individual")
    tk.OptionMenu(root, type_var, "Individual", "Team").pack()
 
    def save_button():
        ename = event_entry.get()
        etype = type_var.get()
 
        if ename == "":
            messagebox.showerror("Error", "Event name cant be empty!")
            return
 
        for e in events:
            if e[0] == ename:
                messagebox.showerror("Error", "Event already exsists!")
                return
 
        # saving event as tuple (name, type)
        events.append((ename, etype))
 
        messagebox.showinfo("Success", "Event added!")
        main_menu()
 
    def return_button():
        main_menu()
 
    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack()
 
    back = tk.Button(root, text="return", anchor='center', command=return_button)
    back.pack()
 
 
# ── ENTER RESULTS SCREEN ─────────────────────────────────
def enter_result_screen():
    clear_screen()
 
    if len(events) == 0:
        messagebox.showerror("Error", "No events added yet!")
        return
 
    tk.Label(root, text="Enter Results", font=("Arial", 14, "bold")).pack(pady=10)
 
    tk.Label(root, text="Select Event:").pack()
    event_names = [e[0] for e in events]
    event_var = tk.StringVar(root)
    event_var.set(event_names[0])
    tk.OptionMenu(root, event_var, *event_names).pack()
 
    tk.Label(root, text="Rankings (1st to 5th):").pack(pady=5)
    tk.Label(root, text="1st=10pts  2nd=7pts  3rd=5pts  4th=3pts  5th=1pt", font=("Arial", 8)).pack()
 
    Rank1 = tk.Entry(root, width=25)
    Rank1.pack()
    tk.Label(root, text="^ 1st place").pack()
 
    Rank2 = tk.Entry(root, width=25)
    Rank2.pack()
    tk.Label(root, text="^ 2nd place").pack()
 
    Rank3 = tk.Entry(root, width=25)
    Rank3.pack()
    tk.Label(root, text="^ 3rd place").pack()
 
    Rank4 = tk.Entry(root, width=25)
    Rank4.pack()
    tk.Label(root, text="^ 4th place").pack()
 
    Rank5 = tk.Entry(root, width=25)
    Rank5.pack()
    tk.Label(root, text="^ 5th place").pack()
 
    def save_button():
        chosen = event_var.get()
 
        # find the event type
        etype = "Individual"
        for e in events:
            if e[0] == chosen:
                etype = e[1]
 
        rankings = [Rank1.get(), Rank2.get(), Rank3.get(), Rank4.get(), Rank5.get()]
 
        alreadey_ranked_one = []
 
        for rank, name in enumerate(rankings, 1):
            name = name.strip()
            if name == "":
                continue
 
            if name in alreadey_ranked_one:
                messagebox.showwarning("Warning", name + " already ranked!")
                continue
 
            if etype == "Individual":
                if name not in individuals:
                    messagebox.showwarning("Warning", name + " not found!")
                    continue
                individuals[name] = individuals[name] + points[rank]
 
            else:
                if name not in team_scores:
                    messagebox.showwarning("Warning", name + " not found!")
                    continue
                team_scores[name] = team_scores[name] + points[rank]
 
            alreadey_ranked_one.append(name)
 
        messagebox.showinfo("Success", "Results saved!")
        main_menu()
 
    def return_button():
        main_menu()
 
    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack()
 
    back = tk.Button(root, text="return", anchor='center', command=return_button)
    back.pack()
 
 
# ── LEADERBOARD SCREEN ───────────────────────────────────
def leaderboard_screen():
    clear_screen()
 
    tk.Label(root, text="Leaderboard", font=("Arial", 14, "bold")).pack(pady=10)

    

    
 

    






#start 
root = tk.Tk()
root.title("Tournament Scoring System")
root.geometry("600x500")
add_team_screen()
root.mainloop()