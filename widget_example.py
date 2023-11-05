from tkinter import *
window=Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)

label=Label(text="My label")
label.config(bg="black")
label.config(fg="white")
label.pack()

window.mainloop()




