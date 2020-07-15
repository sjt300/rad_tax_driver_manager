from tkinter import *
import os
import functions


def first(main, canvas, bar):
    canvas.grid_columnconfigure(0, weight=1)
    canvas.grid_columnconfigure(1, weight=1)
    canvas.grid_columnconfigure(2, weight=0)
    cwd = os.getcwd()
    install_instructions_title_text = "First Time Setup"
    install_instructions_title_lbl = Label(canvas, text=install_instructions_title_text)
    install_instructions_title_lbl.grid(row=0, column=0, columnspan=2)
    install_instructions_body = f"""    
    - Please run this program from the folder you intend it to be installed in

    - If {cwd} is not where you want this program to run from:
        ~ Click "Cancel"
        ~ Relocate the program to where you want it permanently
        ~ Re-run the program from that location (shortcuts can be created where necessary)

    - If you are happy with the current location, please click "Continue" to setup admin access
        
    """
    install_instructions_body_lbl = Label(canvas, text=install_instructions_body, justify=LEFT, borderwidth=2,
                                          relief='sunken')
    install_instructions_body_lbl.grid(row=1, column=0, columnspan=2)
    cancel_btn = Button(canvas, text="Cancel", command=main.destroy)
    cancel_btn.grid(row=2, column=0, sticky=E)

    def launch_admin_setup():
        admin_setup(main, canvas)

    continue_btn = Button(canvas, text="Continue", command=launch_admin_setup)
    continue_btn.grid(row=2, column=1, sticky=W)


def admin_setup(main, canvas):  # todo create 'reset admin' function - requires distribution help
    for child in canvas.winfo_children():
        child.destroy()
    admin_setup_title_lbl = Label(canvas, text="Admin Setup")
    admin_setup_title_lbl.grid(row=0, column=0, columnspan=2)
    user_lbl = Label(canvas, text="Username")
    user_lbl.grid(row=1, column=0, sticky=E)
    user_entry = Entry(canvas, width=50)
    user_entry.grid(row=1, column=1, sticky=W)
    user_entry.focus()
    pass_lbl = Label(canvas, text="Password")
    pass_lbl.grid(row=2, column=0, sticky=E)
    pass_entry = Entry(canvas, width=50, show='*')
    pass_entry.grid(row=2, column=1, sticky=W)
    pass2_entry = Entry(canvas, width=50, show='*')
    btns_frame = Frame(canvas)
    btns_frame.grid(row=4, column=0, columnspan=2)
    cancel_btn = Button(btns_frame, text="Cancel", command=main.destroy)
    cancel_btn.grid(row=0, column=0, sticky=E)

    def submit():  # todo
        if submit_btn.cget("foreground") == "black":
            user_entry.config(state="disabled")
            pass_entry.config(state='disabled')
            pass2_lbl = Label(canvas, text="Re-enter Password")
            pass2_lbl.grid(row=3, column=0, sticky=E)
            pass2_entry.grid(row=3, column=1, sticky=W)
            pass2_entry.focus_force()
            submit_btn.config(command=submit2)
        else:
            return 0

    def submit2():
        if pass_entry.get() == pass2_entry.get():
            print("match")
        else:
            pass_fail = Tk()
            pass_fail.title("Password Match Error")
            fail_txt = """The Passwords do not match
            Either retry the secondary password entry or cancel and try again
            """
            fail_lbl = Label(pass_fail, text=fail_txt)
            fail_lbl.pack()
            ok_btn = Button(pass_fail, text="Ok", command=pass_fail.destroy)
            ok_btn.pack()
            pass_fail.focus_force()

            pass_fail.mainloop()

    submit_btn = Button(btns_frame, text="Submit", fg='grey', command=submit)  # todo
    submit_btn.grid(row=0, column=1, sticky=W)

    # valid user and pass checking frame
    valid_check_frame = Frame(canvas)
    valid_check_frame.grid(row=5, column=0, columnspan=2)
    # Username Instructions
    rule_user_txt = "A valid username must adhere to following:"
    Label(valid_check_frame, text=rule_user_txt, anchor=CENTER).grid(row=0, column=0, columnspan=3)
    rule_user_len_txt = "    ~Be 4-20 characters long"
    rule_user_chars_txt = "    ~Be alphanumeric with characters only from the following: '. _ and - '"
    rule_user_len_lbl = Label(valid_check_frame, text=rule_user_len_txt, fg='red')
    rule_user_chars_lbl = Label(valid_check_frame, text=rule_user_chars_txt, fg='red')
    rule_user_len_lbl.grid(row=1, column=0, sticky=W)
    rule_user_chars_lbl.grid(row=2, column=0, sticky=W)

    # user entry bind
    def check_user(event):
        char = repr(event.char).strip("'")
        sym = repr(event.keysym).strip("'")
        entry = user_entry.get()
        curs_index = user_entry.index(INSERT)
        user = None
        # if backspace is pressed, find where, return what's left of user_entry
        if sym == "BackSpace" and len(entry) > 0 and curs_index != 0:
            user = entry[0: curs_index - 1] + entry[curs_index:]
        # if new character entered, find cursor, add in new character at cursor
        elif char.isalnum() or char in [".", "_", "-"]:
            user = entry[0: curs_index] + char + entry[curs_index:]
        elif sym == "Tab":
            return 0  # avoids breaking
        else:
            return 'break'
        user_bool = None
        if 3 < len(user) < 21:
            rule_user_len_lbl.config(fg='green')
            user_bool = True
        else:
            rule_user_len_lbl.config(fg='red')
            user_bool = False
        if len(user) > 0:  # as only valid chars can be typed after len > 0, would be valid user
            rule_user_chars_lbl.config(fg='green')
        else:
            rule_user_chars_lbl.config(fg='red')
        submittable()

    user_entry.bind("<Key>", check_user)
    # password instructions
    rule_pass_txt = "A valid password must adhere to the following"
    Label(valid_check_frame, text=rule_pass_txt, anchor=CENTER).grid(row=3, column=0, columnspan=3)
    # password rules
    rule_len_txt = "    ~ Be 8-20 characters in length"
    rule_caps_txt = "    ~ Consist of one or more capital letters"
    rule_lower_txt = "    ~ Consist of one or more lower case letters"
    rule_number_txt = "    ~ Consist of one or more numbers"
    rule_special_txt = "    ~ Contain one of the following characters '!, £, $, %, *, #, ?'"
    rule_len_lbl = Label(valid_check_frame, text=rule_len_txt, fg='red')
    rule_caps_lbl = Label(valid_check_frame, text=rule_caps_txt, fg='red')
    rule_lower_lbl = Label(valid_check_frame, text=rule_lower_txt, fg='red')
    rule_number_lbl = Label(valid_check_frame, text=rule_number_txt, fg='red')
    rule_special_lbl = Label(valid_check_frame, text=rule_special_txt, fg='red')
    rule_len_lbl.grid(row=4, column=0, sticky=W)
    rule_caps_lbl.grid(row=5, column=0, sticky=W)
    rule_lower_lbl.grid(row=6, column=0, sticky=W)
    rule_number_lbl.grid(row=7, column=0, sticky=W)
    rule_special_lbl.grid(row=8, column=0, sticky=W)
    valid_char_list = ["!", "£", "$", "%", "*", "#", "?"]

    def check_pass(event):  # todo SECURITY can this be done without storing password to memory?
        pass_char = repr(event.char).strip("'")
        pass_sym = repr(event.keysym).strip("'")
        passwd_entry = pass_entry.get()
        pass_curs_index = pass_entry.index(INSERT)
        if pass_sym == "BackSpace":
            passwd = passwd_entry[0: pass_curs_index - 1] + passwd_entry[pass_curs_index:]
        elif pass_char.isalnum() or pass_char in valid_char_list:
            passwd = passwd_entry[0: pass_curs_index] + pass_char + passwd_entry[pass_curs_index:]
        else:
            return 'break'
        # password length check
        if 7 < len(passwd) < 21:
            rule_len_lbl.config(fg='green')
        else:
            rule_len_lbl.config(fg='red')
        # password caps check
        functions.check_pass(passwd, r"[A-Z]", rule_caps_lbl)
        # password lower check
        functions.check_pass(passwd, r"[a-z]", rule_lower_lbl)
        # password number check
        functions.check_pass(passwd, r"[0-9]", rule_number_lbl)
        # password special character check
        functions.check_pass(passwd, r"[!£$%*#?]", rule_special_lbl)
        submittable()

    def submittable():
        if rule_user_len_lbl.cget("foreground") == rule_len_lbl.cget("foreground") == rule_caps_lbl.cget("foreground")\
                == rule_lower_lbl.cget("foreground") == rule_number_lbl.cget("foreground")\
                == rule_special_lbl.cget("foreground") == "green":
            submit_btn.config(fg='black')
        else:
            submit_btn.config(fg='grey')

    pass_entry.bind("<Key>", check_pass)

    def check_all():  # todo check all labels are green, if so light submit black
        pass


