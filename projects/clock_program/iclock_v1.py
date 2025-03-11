from tkinter import *
import time


def update():
    # get the day
    day_string = time.strftime('%A')
    day_label.configure(text=day_string)

    # get the date
    date_string = time.strftime('%B %d, %Y')
    date_label.configure(text=date_string)

    # get the time
    time_string = time.strftime('%I:%M:%S  %p')
    time_label.configure(text=time_string)

    # update the window with its new content every 1 sec or 1000ms
    window.after(1000, update)


window = Tk()
window.geometry('255x140')
window.resizable(width=False, height=False)
window.title('iClock v1')

# create a day label
day_label = Label(window, font=('Ink Free', 25), bg='#00ff00', width=225)
day_label.pack()

# create a date label
date_label = Label(window, font=('Ink Free', 20), bg='#00ff00', width=225)
date_label.pack()

# create a time label
time_label = Label(window, font=('Ink Free', 30), fg='#00ff00', bg='black', width=225)
time_label.pack()

# display the time for the first time
update()

window.mainloop()