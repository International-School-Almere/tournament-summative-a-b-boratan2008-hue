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
rankings = []

# points for each place
points = {1: 10, 2: 7, 3: 5, 4: 3, 5: 1}

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
#add team screen
def add_team_screen():

    #replace previous screen
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
        clear_screen()

    def return_button():
        print("return")

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
    
    tk.label (root, text="Add Event", font=("Arial", 14, "bold")).pack(pady=10)

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

    def return_button():
        print("return")

    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack()

    back = tk.Button(root, text="return", anchor='center', command=return_button)
    back.pack() 

    #enter result screen
    def enter_result_screen():
        clear_screen()
        if len(events) == 0: 
            messagebox.showerror ("Error", "No events added yet!")
        return 
    
    tk.Label(root, text="Enter Results", font=("Arial", 14, "bold")).pack(pady=10)
    tk.label (root, text="Select Event:") .pack()
    event_names = [e[0] for e in events]
    event_var = tk.StringVar(root)
    event_var.set(event_names[0])
    tk.OptionMenu(root, event_var, *event_names).pack()

    tk.Label(root, text="select event:").pack()
    event_names=[e[0] for e in events]
    event_var=tk.StringVar(root)
    event_var.set(event_names[0])
    tk.OptionMenu(root, event_var, *event_names).pack()

    tk.Label(root, text="Rankings (1st to 5th):").pack(pady=5) 
    tk.Label(root, text="1st=10pts  2nd=7pts  3rd=5pts  4th=3pts  5th=1pt", font=("Arial", 8)).pack()

    Rank1=tk.Entry(root,width=25)
    Rank1.pack()
    tk.Label(root, text="^ 1st place").pack()

    Rank2=tk.entr(root,width=25)
    Rank2.pack()
    tk.Label(root, text="^ 2nd place").pack() 

    Rank3=tk.entr(root,width=25)
    Rank3.pack()
    tk.Label(root, text="^ 3nd place").pack() 

    Rank4=tk.entr(root,width=25)
    Rank4.pack()
    tk.Label(root, text="^ 4nd place").pack() 

    Rank5=tk.entr(root,width=25)
    Rank5.pack()
    tk.Label(root, text="^ 5nd place").pack() 

    def save_button():
        global rankings
        chosen = event_var.get()
        #find the event type 
        etype="Individual"
        for e in events:
            if e[0] == chosen:
                etype = e[1]


                rankings=[Rank1.get(), Rank2.get(), Rank3.get(),Rank4.get(),Rank5.get()]
        
                alreadey_ranked_one=[]
        

for rank, name  in enumerate(rankings, 1):
    name = name.strip()
    if name == "":
                continue
    
    if name in alreadey_ranked_one:
        messagebox.showwarning("Warning", name + " already_ranked_one!")
        continue
    if etype == "Individual":
        if name not in individuals:
         messagebox.showwarning("Warning", name + " not found!")

         continue
        individuals[name]=individuals[name] + points[rank]
    else:
        if name not in team_scores:
           messagebox.showwarning ("Warning",name+ "not found!")

        continue
    team_scores[name]= team_scores[name]+points[rank]
    alreadey_ranked_one.append(name)

    messageboxs.howinfo("Success", "Results saved!")
    main_menu()
    def return_button():
        print("return")
        
 
    save = tk.Button(root, text="save", anchor='center', command=save_button)
    save.pack() 
    back=tk.Button(root, text="return", anchor='center', command=return_button) 
    back.pack()

#Leader board screen 
def leaderboard_screen():
    clear_screen()
    tk.Label(root)


    

    
 

    






#start 
root = tk.Tk()
root.title("Tournament Scoring System")
root.geometry("600x500")
add_team_screen()
root.mainloop()