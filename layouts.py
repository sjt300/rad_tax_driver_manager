from tkinter import *
from PIL import Image, ImageTk
import time

release_version = "1.0"


class Screen(object):

    def __init__(self, master, layout):
        self.master = master

    def common_layout(self, geometry, sq_func):
        for child in self.master.winfo_children():  # destroys all children and redraws from scratch
            child.destroy()
        self.master.overrideredirect(True)  # disables windows standard title frame
        self.master.geometry(geometry)  # geometry set by mini or maxi

        title_frame = Frame(self.master, bg='#ff1100')
        title_frame.pack(expand=True, fill=X, anchor=N)
        img = Image.open("RT_icon.jpg")  # RadioTaxis logo; for open-source, this will need changing to escape
        # copyright infringement
        img.thumbnail([20, 20])
        photo = ImageTk.PhotoImage(img)
        img_lbl = Label(title_frame, image=photo)
        img_lbl.image = photo
        img_lbl.pack(side=LEFT)
        title_txt = "Radio Taxis Shift manager: Version " + release_version  # displays current version in title
        title_lbl = Label(title_frame, text=title_txt, bg='#ff1100')
        title_lbl.pack(side=LEFT)
        close_btn = Button(title_frame, text="X", command=self.master.destroy)  # top-right button commands, manually
        # coded
        close_btn.pack(side=RIGHT)
        square = chr(9633)
        sq_btn = Button(title_frame, text=square, command=sq_func)
        sq_btn.pack(side=RIGHT)
        min_btn = Button(title_frame, text="_", command=self.minimise)
        min_btn.pack(side=RIGHT)
        main_frame = Frame(self.master)  # todo put main gui in here
        main_frame.pack()
        status_bar = Frame(self.master, bg='gray')  # status bar at the bottom
        status_bar.pack(expand=True, fill=X, anchor=S)
        clock_lbl = Label(status_bar, text="")
        clock_lbl.pack(anchor=SW)

        def update_clock():
            now = time.strftime('%H:%M:%S %d-%m-%Y')
            if clock_lbl.winfo_exists():  # this prevents error when changing window size and therefore clock label name
                clock_lbl.configure(text=now)
                self.master.after(1000, update_clock)
        update_clock()

        def move_window(event):  # allows single click on title bar to move the window
            self.master.geometry("+{0}+{1}".format(event.x_root, event.y_root))

        title_frame.bind("<B1-Motion>", move_window)

        def mapped(event):
            self.master.update_idletasks()
            self.master.overrideredirect(True)
            self.master.state('normal')

        title_frame.bind("<Map>", mapped)

    def mini(self):
        """
        Windows the program
        :return:
        """
        def sq_maximise():
            self.maxi()
        self.common_layout('500x300+0+0', sq_maximise)

    def maxi(self):
        """
        Fullscreens the program
        :return:
        """
        def sq_minimise():
            self.mini()
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        geom = str(width) + "x" + str(height)
        self.common_layout(geom, sq_minimise)

    def minimise(self):
        self.master.update_idletasks()
        self.master.overrideredirect(False)
        self.master.state('iconic')


class Layout:
    def __init__(self, master):
        self.master = master

    def install(self, master):
        self.master = master

