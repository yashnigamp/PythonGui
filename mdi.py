from  tkinter import *
from  tkinter import filedialog
import subprocess,sysconfig
import os

def hello():
    pass  
def cust():
    import cust
    cust.customerform() 
    #button.pack()

root = Tk()
root.minsize(888,888)
root.maxsize(888,888)
menubar = Menu(root)

custmenu = Menu(menubar,tearoff=0)#to avoid dashed line
menubar.add_cascade(label="Inventory", command=cust)

estmenu = Menu(menubar,tearoff=0)#to avoid dashed line
menubar.add_cascade(label="CustomerDetails", command=hello)

root.config(menu=menubar)
root.mainloop()