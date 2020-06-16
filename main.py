"""
Application developed by Stephen Turley for Radio Taxis, Southampton
This application is open-source apart from specific items clearly stated in comments.Change these to avoid copyright
"""

from tkinter import *
import functions
import layouts

root = Tk()
screen = layouts.Screen(root, None)  # todo initiate screen, allow functions to change the screen layout (here currently None)

if not functions.check_db():
    screen.maxi()




# screen = Screen(root)
# screen.mini()
root.mainloop()
