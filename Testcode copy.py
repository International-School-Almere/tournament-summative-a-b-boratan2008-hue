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


#add team screen
def add_team_screen():
    
    #replace previous screen
    if len(teams) >= 5:
        messagebox.showerror("Error", "Max 5 teams allowed!")
        return
 
    #win = tk.Toplevel(root)
    #win.title("Add Team")
   # win.geometry("300x350")
   # win.config(bg="#f0f0f0")
 
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

    save = tk.Button(root, text="save",anchor='center',command=save_button)
    save.pack()

    back = tk.Button(root, text="return",anchor='center',command=return_button)
    back.pack()

def save_button():
    print("save")
    #Save info in file.
        #read file - get data - change data - overwrite file

def return_button():
    print("return")


root = tk.Tk()
root.title("Tournament Scoring System")
root.geometry("600x500")
add_team_screen()
root.mainloop() 


def save_button():
    print("save")
    #Save info in file.
        #read file - get data - change data - overwrite file

    def return_button():
    print("return")




    team_name = team_entry.get()
    ...

    members = [
        Member1.get(),
        Member2.get(),
        Member3.get(),
        Member4.get(),
        Member5.get()
    ]

    clean_members = []
    for m in members:
        if m != "":
            clean_members.append(m)

    if team_name == "":
        messagebox.showerror("Error","Team name required!")
        return

    teams[team_name] = clean_members
    team_scores[team_name] = 0

    messagebox.showinfo("Success", "Team added!") 
    team_name=team_entry.get()

        #get the members
    members = []
    members.append(Member1.get())
    members.append(Member2.get())
    members.append(Member3.get())
    members.append(Member4.get())
    members.append(Member5.get())

        #remove the empty ones
clean_members = [ ]
for m in members:
            if m != "":
                clean_members.append(m)

        #control
if team_name == " ":
            messagebox.showerror("Error","Team name required!")
return
        
        #save in dictinoary 
teams[team_name] = clean_members
team_scores[team_name] = 0