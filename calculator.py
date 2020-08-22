from tkinter import *
root = Tk()
def click():
    label = Label(root,text="how are you "+e,fg="pink",bg="yellow")
    label.pack()
    
entry = Entry(root)
entry.pack()
e = entry.get()
button = Button(root,width=10,height=10,command=click,text="CLick me",fg="red",bg="yellow")
button.pack()
root.mainloop()
