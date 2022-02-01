from tkinter import *
root = Tk()
root.command(padx=20,pady=20)
root.title("Password Manager")
canvas = Canvas(root, width = 400, height = 480)
img = PhotoImage(file="lock.png")
canvas.create_image(20,20, anchor=NW, image=img)
canvas.grid(row=0,column=1)
#Label




canvas.pack()
mainloop()
