from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Frank' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please enter the correct credentials')


window = Tk()

window.geometry('1280x700+0+0')
window.title('Login System')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg2.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='#EDEDED')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT, font=('poppins', 16, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('poppins', 16, 'bold'))
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

passwordImage = PhotoImage(file='padlock.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT, font=('poppins', 16, 'bold'))
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('poppins', 16, 'bold'))
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('poppins', 16, 'bold'), width=15, cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()
