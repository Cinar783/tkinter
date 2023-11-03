import tkinter


window=tkinter.Tk()
window.title("Python Tkinter")
def button_funcion():
    user_input=my_entry.get()
    print(user_input)

#label
my_label=tkinter.Label(text='This is label',foreground='Black',font=("Arial",30,"normal"))
window.minsize(width=500,height=500)
#my_label.place(x=40,y=20)
my_label.grid(row=1,column=1)

#button
my_button=tkinter.Button(text="My button",command=button_funcion)
#my_button.place(x=100,y=100)
my_button.grid(row=2,column=1)

#entry
my_entry=tkinter.Entry(width=50,)
#my_entry.place(x=40,y=150)
my_entry.grid(row=3,column=2)



tkinter.mainloop()