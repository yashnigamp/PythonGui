from tkinter import *
master=Tk()
master.maxsize(444,444)
master.minsize(444,444)
master.title("Easy shop")
Label(master,text="            ").grid(row=0)
Label(master,text="Name").grid(row=0,column=1)
e1=Entry(master).grid(row=0,column=2,)
Label(master,text="           ").grid(row=0,column=3)
Label(master,text="Id").grid(row=0,column=4)
e2=Entry(master).grid(row=0,column=5)

Label(master,text="Name").grid(row=1,column=1)
e1=Entry(master).grid(row=1,column=2,)
Label(master,text="           ").grid(row=1,column=3)
Label(master,text="Id").grid(row=1,column=4)
e2=Entry(master).grid(row=1,column=5)

Label(master,text="Name").grid(row=2,column=1)
e1=Entry(master).grid(row=2,column=2,)
Label(master,text="           ").grid(row=2,column=3)
Label(master,text="Id").grid(row=2,column=4)
e2=Entry(master).grid(row=2,column=5)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

#Button(master,text='Add').grid(row=3,column=1, sticky=E+W)

Button(master,text='Delete').grid(row=3,column=2,sticky=E+W)
Button(master,text='Add').grid(row=3,column=5,columnspan=3, sticky=E+W)

Button(master,text='Delete').grid(row=4,column=2,sticky=E+W)
Button(master,text='Add').grid(row=4,column=5,columnspan=3, sticky=E+W)

mainloop()