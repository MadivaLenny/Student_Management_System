from tkinter import *
import time
import ttkthemes
from tkinter import ttk


# functionality part

def clock():
    date = time.strftime('%d/%m/%y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


# GUI part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(False, False)

datetimeLabel = Label(root, font=('poppins', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()
s = 'Student Management System'
sliderLabel = Label(root, text=s, font=('arial', 28, 'italic bold'))
sliderLabel.place(x=350, y=5)

connectButton = ttk.Button(root, text='Connect Database')
connectButton.place(x=980, y=5)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='student.png')
logo_image = Label(leftFrame, image=logo_image)
logo_image.grid(row=0, column=0)

root.mainloop()
