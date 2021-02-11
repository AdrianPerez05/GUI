from tkinter import *

master = Tk()

master.geometry("900x400")
master.title("Adrian's GUI")
master.configure(background="salmon")

canvas = Canvas(master, width='200', height='200')


# add = Button(master,text= '+', bg="lime green", fg="gray20", highlightbackground="lime green")
# add.grid(column=3, row=2)
global counter
counter = 0
def lines():
    global counter
    canvas_height = 20
    canvas_width = 200
    y = int(canvas_height / 2)
    canvas.create_line(0, y, canvas_width, y)

    x1 = 0
    y1 = canvas_width
    x2 = 0
    y2 = 0

    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x1, y1+counter, x2, y2+counter)
    for x in range(0, 200, 20):
        canvas.create_line(x1, y1, x2, y2)
        canvas.create_line(x1, y1 + x, x2, y2 + x)
    counter =+ 50

draw_button1 = Button(master,text= 'Draw Lines', command=lines, bg="red", fg="gray20", highlightbackground="royal blue")
draw_button1.grid(column=3, row=2)

canvas.grid(column = 4, row = 4)

#First and Last Name
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Pop-Up Menu
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#Male or Female Radio Button

var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)

#Scale

w1 = Scale(master, from_=0, to=400)
w1.pack()
w = Scale(master, from_=0, to=700, orient=HORIZONTAL)
w.pack()

#Scroll Bar
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, 'Adrians GUI line number ' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

#GUI TEXT
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'ADRIANS GUI\nBEST GUI\n')

#ListBox
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Lambo')
Lb.insert(2, 'Ferrari')
Lb.insert(3, 'Mercedes')
Lb.insert(4, 'Bugatti')
Lb.pack()

#Spin Box

w = Spinbox(master, from_ = 0, to = 10)
w.pack()

#RadioButtons
root = Tk()
v = IntVar()
Radiobutton(root, text='Red Lambo', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Green Lambo', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='Blue Lambo', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Black Lambo', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='White Lambo', variable=v, value=1).pack(anchor=W)
mainloop()





mainloop()

