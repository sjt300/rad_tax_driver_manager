"""
Application developed by Stephen Turley for Radio Taxis, Southampton
This application is open-source apart from specific items clearly stated in comments.Change these to avoid copyright
"""

from tkinter import *
from PIL import Image, ImageTk
import time
import layouts
import os
import db_manager
import functions
release_version = "1.0"
root = Tk()
# disable standard title frame
root.overrideredirect(True)
# default to fullscreen
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
full_geom = str(s_width) + "x" + str(s_height) + "+0+0"
root.geometry(full_geom)
# custom title frame
title_frame = Frame(root, bg='#ff1100')
title_frame.place(relwidth=1, relx=0.5, anchor=N)
# icon image top left
# RadioTaxis logo; for open-source, this will need changing to escape copyright infringement
icon_logo = Image.open("./images/RT_icon.jpg")
icon_logo.thumbnail([20, 20])
photo_logo = ImageTk.PhotoImage(icon_logo)
icon_logo_lbl = Label(title_frame, image=photo_logo)
icon_logo_lbl.image = photo_logo
icon_logo_lbl.pack(side=LEFT)  # todo add bind for double click for admin
# main title
title_lbl = Label(title_frame, text="Radio Taxis Shift Manager", bg='#ff1100')
title_lbl.pack(side=LEFT)
# close button img
icon_close = Image.open("./images/close_icon.jpg")
icon_close.thumbnail([20, 20])
photo_close = ImageTk.PhotoImage(icon_close)
close_lbl = Label(title_frame, image=photo_close)
close_lbl.image = photo_close
close_lbl.pack(side=RIGHT)


def close(event):
    root.destroy()


close_lbl.bind("<Button-1>", close)
title_frame.update()
bar_relheight = title_frame.winfo_height() / s_height  # used to duplicate size of status bar
# minimize img
min_lbl = Label(title_frame)
min_lbl.pack(side=RIGHT)
icon_min = Image.open("./images/min_icon.jpg")
icon_min.thumbnail([20, 20])
photo_min = ImageTk.PhotoImage(icon_min)
min_lbl.configure(image=photo_min)
min_lbl.image = photo_min


def minimize(event):  # minimise without this doesn't put idle window in taskbar
    root.update_idletasks()
    root.overrideredirect(False)
    root.state('iconic')


min_lbl.bind("<Button-1>", minimize)


# sets back to overrider direct (disable title frame again)
def mapped(event):
    root.update_idletasks()
    root.overrideredirect(True)
    root.state('normal')


min_lbl.bind("<Map>", mapped)
# main canvas
title_frame.update()  # without this, height returns 1
title_bar_height = title_frame.winfo_height()
main_canvas_relheight = (s_height - (2 * title_bar_height)) / s_height  # assumes status frame same as title frame
main_canvas = Canvas(root)
main_canvas.place(relwidth=1, relheight=main_canvas_relheight, relx=0, rely=title_bar_height / s_height)
# background gradient  # could possibly use an image instead of coding it in
main_canvas.update()
h = main_canvas.winfo_height()
for i in range(0, h + 1):
    r, g, b = 255, 255 - int(10 + ((i / h) * 245)), 255 - int((i / h) * 255)
    color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    main_canvas.create_line(0, i, s_width, i, fill=color)
# status bar
status_frame = Frame(root, bg='#ff1100')
status_frame.place(relwidth=1, relheight=bar_relheight, relx=0, rely=1 - bar_relheight)
# clock
clock_lbl = Label(status_frame, bg='#ff1100', borderwidth=3, relief='sunken')
clock_lbl.pack(side=LEFT)


def clock_time():
    time_string = time.strftime('%A %d %B %H%M %S')  # Full DayName/day/month/h/m/s in 24hr format
    clock_lbl.config(text=time_string)
    root.after(1000, clock_time)


clock_time()
clock_lbl.update()

# status label  # todo can have more functionality in status bar
status_lbl = Label(status_frame, bg='#ff1100', borderwidth=2, relief='sunken', anchor=W, text="test")
status_lbl.pack(side=LEFT, expand=True, fill=X)

# initiate startup
# test
layouts.first(root, main_canvas, status_frame)

root.mainloop()
