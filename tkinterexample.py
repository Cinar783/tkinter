import tkinter


window=tkinter.Tk()
window.title("Python Tkinter")


my_label=tkinter.Label(text='This is label',foreground='Black',font=("Arial",30,"normal"))
window.minsize(width=500,height=500)
my_label.pack()


my_button=tkinter.Button(text="My button",background="Black",foreground="White",font=("Arial",20,"italic"))
my_button.pack()


tkinter.mainloop()