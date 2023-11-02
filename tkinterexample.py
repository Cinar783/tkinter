import tkinter


window=tkinter.Tk()
window.title("Python Tkinter")
def button_funcion():
    user_input=my_entry.get()
    print(user_input)

#label
my_label=tkinter.Label(text='This is label',foreground='Black',font=("Arial",30,"normal"))
window.minsize(width=500,height=500)
#my_label.pack(side='top')
my_label.place(x=40,y=20)


#button
my_button=tkinter.Button(text="My button",command=button_funcion)
#my_button.pack(side="top")


#entry
my_entry=tkinter.Entry(width=50,)
#my_entry.pack(side="left")



tkinter.mainloop()