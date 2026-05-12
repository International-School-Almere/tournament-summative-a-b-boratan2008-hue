# Progress Journal

> Use this journal to track progress, decisions, problems, and next steps.
> Update it after each work session.
> 
---

# 1. Project Overview 

## Project Title
[scorinsystem.py]

## Project Description
[Its a tournament scoring sytem built in phyton visual stuiido code also using Tkinter the program will 
also allow organisers to add team and also individual participant like for example create events, enter results and view a leaderboard points are decided based on the ranking positions like 1st=10, 2nd=7, 3rd=5, 4th=3, 5th=1]

## Start Date
[ 30 march 2026]

## Target End Date
[ add later]

## File list.
scoring system.py
## (Dependencies) API / library / module list.
tkinter (built into Python, used for GUI)
tkinter.messagebox (used for error and success popups)
tkinter.ttk (imported but available for future use) 
---


# 2. Progress Log

> Add a new session at the top each time you work.

---
## Session [10]
**Date:** [ 7 May 2026]  
**Time spent:** [45 min]  
**Focus:** [i fixed remaining errors and writing progress journal]

### Problems / Challenges
- i still had some left errors from the previous sesion
-  My Progress journal needed to be updated with all sessions

### Solutions / Actions Taken
- fixed old errors in the code 
- Updated progress journal with all session dates and details


### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?: my program right now is so much more cleaner and more complete 
- What needs improvement?: I need to finish leaderboard and test the full program again
- What did I learn?: i learned that keeping a journal makes it easier to track what went wrong and why 

---

## Session [09]
**Date:** [6 may 2026]  
**Time spent:** [1 hour]  
**Focus:** [I focus on fixing all erros across all screens]

### Problems / Challenges
- Multiple screens had tk.label with lowercase l causing AttributeError 
- tk.entr typo on Rank2 to Rank5 entries
- enter result screen was defined inside 
- add_event_screen instead of outside
- messageboxs.howinfo typo causing results not to save


### Solutions / Actions Taken
- Fixed all tk.label to tk.Label with capital L my teacher help me a lot 

- Fixed all tk.entr to tk.Entry
_ Moved enter_result_screen outside of add event screen againmy teacher help with it 
_Fixed messageboxs.howinfo to messagebox showinfo it was a little spelling mistake
_Fixed all indentation errors throughout the file


### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well? After fixing the errors the program ran without crashing 
- What needs improvement? Need to finish the leaderboard screen
- What did I learn? Even the small typos like lowercase letters can break the whole program 

---
## Session [08]
**Date:** [22 april 2026]  
**Time spent:** [1 hour]  
**Focus:** [i focus on continue code and fixing bugs]

### Problems / Challenges
- rankings list had missing commas between .get() calls
- already_ranked variable was outside the function so indentation was wrong

### Solutions / Actions Taken
- i added missing commas to the list
- I fixed indentation of already_ranked and the for loop

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?  Points calculation logic started working after fixing indentation 
- What needs improvement?  Still some errors left to fix
- What did I learn?  Missing commas in lists cause SyntaxErrors that are hard to spot 
---
## Session [07]
**Date:** [21 April 2026]  
**Time spent:** [1 hour]  
**Focus:** [Writing the enter results screen]

### Problems / Challenges
-  I needed to find the event type before assigning points
-  Had to prevent the same name from being ranked twice


### Solutions / Actions Taken
-  I used a for loop to find the event type from the events list

- Used an already_ranked list to track who has already been given points

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well? The logic for finding event type worked correctly 
- What needs improvement? I need to test with the actual data 
- What did I learn? i learned how mostly things work in this stage


## Session [06]
**Date:** [20 April 2026]  
**Time spent:** [30 min]  
**Focus:** [Adding the event type dropdown and fixing event screen errors]

### Problems / Challenges
-  Wrote tk.label with lowercase l which caused an AttributeError
-  Duplicate event names were not being checked properly


### Solutions / Actions Taken
-  Fixed tk.label to tk.Label
-  i save events as tuples (name, type) so both stay together
- Added a for loop to check if event name already exists before saving

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well? The dropdown menu for event type worked correctly
- What needs improvement? Return button still just prints, needs to go to main menu 
- What did I learn?  I learned how to use tk.OptionMenu and tk.StringVar for dropdowns


## Session [05]
**Date:** [15 April 2026]  
**Time spent:** [39 min]  
**Focus:** [Writing the add event screen]

### Problems / Challenges
-  Needed a dropdown menu for event type which I had not used before
-  enter_result_screen was accidentally written inside add_event_screen

### Solutions / Actions Taken
-  I used tk.StringVar and tk.OptionMenu for the dropdown
-  Moved enter_result_screen outside to be its own function


### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?  Dropdown worked after learning how StringVar and OptionMenu work together
- What needs improvement? Need to add the enter results screen
- What did I learn? OptionMenu needs a StringVar to store the selected value
## Session [04]
**Date:** [10 April 2026]  
**Time spent:** [1 hour]  
**Focus:** [Adding the individual screen and fixing navigation]

### Problems / Challenges
-  Return button was just printing return instead of going back to main menu
-  Screen was not clearing properly between screens


### Solutions / Actions Taken
-  i changed return_button to call main_menu() instead of print
-  i really make sure clear_screen() is called at the start of every screen function

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well? The navigation between screens started working properly
- What needs improvement? i need to add more screens
- What did I learn? I learned every screen function needs clear_screen() at the start otherwise widgets stack up


## Session [03]
**Date:** [7 April 2026]  
**Time spent:** [50 min]  
**Focus:** [Fixing errors from previous session and adding main menu]

### Problems / Challenges
- save_button and return_button were defined after the buttons that called them
- Indentation errors inside the save function


### Solutions / Actions Taken
-  I moved function definitions above the button calls
-  Fixed all indentation errors using consistent 4 spaces
-  Add main_menu function with buttons for each screen
### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?  Main menu loaded correctly after fixes
- What needs improvement?  Individual and event screens still need to be written
- What did I learn? I learned that functions must be defined before they are called in Tkinter button commands

## Session [02]
**Date:** [31 march 2026]  
**Time spent:** [1 hour]  
**Focus:** [Building the add team screen]

### Problems / Challenges
- Missing quotation mark on a Label line stopped the whole program from running
- Wrote from tkinter import ttv instead of ttk which caused an ImportError
- After i pressed save nothing happened visually because clear_screen was missing


### Solutions / Actions Taken
-  Fixed the missing quotation mark by reading the error message carefully
-  Corrected ttv to ttk
-  Added clear_screen() function and called it inside save_button 
### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?  Once errors were fixed the team data saved correctly to the dictionary
- What needs improvement? Return button needs to go back to main menu
- What did I learn? Small typos like ttv instead of ttk cause ImportErrors that stop the whole program
## Session [01]
**Date:** [30 March 2026]  
**Time spent:** [50 min]  
**Focus:** [Initial setup and data structures]

### Problems / Challenges
- Needed to decide how to store teams, individuals, events and scores
- Needed to choose a points system for the tournament

### Solutions / Actions Taken
- Used dictionaries for teams, individuals and team_scores
Used a list for events
-  Defined a points dictionary mapping rank to points (1st=10, 2nd=7, 3rd=5, 4th=3, 5th=1)
-  I decided to use Tkinter for the GUI since it comes built into Python with no extra install needed
### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well? Data structures were straightforward to plan and set up
- What needs improvement? Need to start building the actual screens
- What did I learn? Planning the data structures first made it easier to build the rest of the program
# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |

---

# 11. Final Reflection

> Complete this section at the end of the project.

## What I achieved
- 
- 
- 

## What worked well
- 
- 
- 

## What did not work well
- 
- 
- 

## What I would improve next time
- 
- 
- 

## Final outcome
[Describe the final result]

## Did I meet the success criteria (designspecifications)?
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Final evaluation
[Write a short final judgment of the project]

---
- .

