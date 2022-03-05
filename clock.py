# import required modules
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Setup main window
root = Tk()
root.title("Clock")
root.geometry("640x200")
root.configure(bg="black")

# Setup font
font = "Ubuntu"

# Setup time
def time():

    string = strftime("%H:%M:%S %p")
    label_time.config(text=string)
    label_time.after(1000, time)


# Setup date
def date():

    date = strftime("%d")

    if date[0] == "1":
        ltr = "th"
    elif date[1] == "1":
        ltr = "st"
    elif date[1] == "2":
        ltr = "nd"
    elif date[1] == "3":
        ltr = "rd"
    else:
        ltr = "th"

    string = strftime(f"%d{ltr} of %B %Y")
    label_date.config(text=string)
    label_date.after(1000, time)


label_time = Label(root, font=(font, 80), background="#000", foreground="#00ff00")
label_time.pack(anchor="center")

label_date = Label(root, font=(font, 40), background="#000", foreground="#00ff00")
label_date.pack(anchor="center")

# Display date and time
time()
date()

# Run main window
mainloop()
