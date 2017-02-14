from Tkinter import *

root = Tk()
root.configure(background='gray')


leftPane = Frame(root, bg='green')

leftPaneRow = Frame(leftPane, bg='gray')

xNameL = Label(leftPaneRow, text='x variable')
xNameE = Entry(leftPaneRow,width=15,text='test')


left2 = Label(leftPane,text="I'm the 2 label!")
left3 = Label(leftPane,text="I'm the 3 label!")

leftPane.pack(side=LEFT,fill=Y,padx=5,pady=5,ipadx=10,ipady=10)
leftPaneRow.pack(side=TOP,fill=X,padx=5,pady=5)
xNameL.pack(side=LEFT)
xNameE.pack(side=RIGHT)
left2.pack(side=LEFT)
left3.pack(side=RIGHT)

centerPane = Frame(root, bg='red')
rightPane = Frame(root, bg='blue')

lab_right = Label(rightPane, text='name of right variable')
lab_center = Label(centerPane, text='name of central variable')


rightPane.pack(side=RIGHT,fill=Y,padx=5,pady=5,ipadx=10,ipady=10)
lab_right.grid(row=1,column=1)

centerPane.pack()
lab_center.pack()

#lab1 = Label(root,text='label 1',bg='green').pack(side=LEFT,padx=5,ipadx=10,fill=BOTH)

#pane1 = Frame(root,bg='green')
#lab2 = Label(pane1, text='label 2', bg='blue',fg='white')
#pane1.pack(side=RIGHT,fill=BOTH)
#lab2.pack(side=RIGHT)

#lab3 = Label(root, text='label 3', bg='red').pack(side=TOP,fill=X)
#lab4 = Label(root, text='label 4', bg='cyan').pack(side=BOTTOM,fill=X)

'''
row1 = Frame(root)
check1 = Checkbutton(row1)
lab1 = Label(row1, text='x var name')
ent1 = Entry(row1,width=10)

row1.pack(side=TOP,padx=20,pady=5)
check1.pack(side=LEFT)
lab1.pack(side=LEFT)
ent1.pack(side=RIGHT)

pane1 = Frame(root,width=20,height=20,background='blue')
labb = Label(pane1,text='test')

pane1.pack(side=RIGHT,padx=5,pady=5,fill=X)
labb.pack(side=LEFT)
'''


root.mainloop()