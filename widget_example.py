from tkinter import *
window=Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=50,pady=50)

label=Label(text="My label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=20,pady=20)
label.config(font='italic')
label.pack()

def buton_clic():
    print('buton click')
    print(text.get("1.0", END))

button=Button(text='Button',command=buton_clic)
button.config(pady=20,padx=20)
button.pack()


entry=Entry(width=20)
entry.focus()
entry.pack()

text=Text(height=10)

def scale_celect(value):
    print(value)

my_scale=Scale(from_=0,to=50,command=scale_celect)
my_scale.pack()



text.pack()




window.mainloop()




