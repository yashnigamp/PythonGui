from tkinter import *
from tkinter.messagebox import showinfo
#from reportlab.pdfbase.acroform import visibilities
def customerform():
    
    root = Tk()
    root.title("Project")
    root.maxsize(1000,1000)
    root.minsize(1000, 1000)
    
    
    hframe = Frame(root)
    hframe.pack(fill=X)
            
    hl1 = Label(hframe, text="Inventory", width=25,font="times 24 bold italic underline",fg="#001dff")
    #lbl1.config(font=("Courier", 18))
    hl1.pack(side=TOP, padx=5, pady=5)
    
    frame1 = Frame(root)
    frame1.pack(fill=X)
            
    lbl1 = Label(frame1, text="Supplier-Id", width=10,font="times 18 bold underline",fg="green")
    #lbl1.config(font=("Courier", 18))
    lbl1.pack(side=LEFT, padx=20, pady=20)           
           
    entry1 = Entry(frame1,font="times 18 bold")
    entry1.pack(fill=X, padx=10, expand=True)
    
    frame2 = Frame(root)
    frame2.pack(fill=X)
            
    lbl2 = Label(frame2, text="Supplied Series", width=12,font="times 18 bold")
    lbl2.pack(side=LEFT, padx=20, pady=20)        
    
    entry2 = Entry(frame2)
    entry2.pack(fill=X, padx=10,expand=True)
    
    frame3 = Frame(root)
    frame3.pack(fill=X)
            
    lbl3 = Label(frame3, text="Quantity", width=12,font="times 18 bold")
    lbl3.pack(side=LEFT, padx=20, pady=20)        
    
    entry3 = Entry(frame3)
    entry3.pack(fill=X, padx=10,expand=True)
    
    
    frame4 = Frame(root)
    frame4.pack(fill=X)
            
    lbl4 = Label(frame4, text="Date", width=12,font="times 18 bold")
    lbl4.pack(side=LEFT, padx=20, pady=20)        
    
    entry4 = Entry(frame4)
    entry4.pack(fill=X, padx=10,expand=True)
    
    
    
    frame5 = Frame(root)
    frame5.pack(fill=X)
            
    lbl5 = Label(frame5, text="Invoice No.", width=12,font="times 18 bold")
    lbl5.pack(side=LEFT, padx=20, pady=20)        
    
    entry5 = Entry(frame5)
    entry5.pack(fill=X, padx=20,expand=True)
    
    buttonframe=Frame(root)
    buttonframe.pack(fill=X,padx=50)
    
    b1 = Button(buttonframe, text="Add", width=6,font="times 18 bold")
    b1.pack(side=LEFT, padx=5, pady=5) 
    
    b2 = Button(buttonframe, text="Delete", width=6)
    b2.pack(side=LEFT, padx=5, pady=5) 
    # b3=Button(buttonframe,text="Add")
    # b3.pack()
    def reply():
        #showinfo(message=Lb1.selection_get())
        
        entry1.delete(0, END)
        entry1.insert(0,Lb1.selection_get())
    def show():
        Lb1.pack(side=TOP, padx=5, pady=5)
        b4.config(state=NORMAL)
        print("show")
        #b4.config(state=NORMAL)
    b3 = Button(buttonframe, text="Update", width=6)
    b3.pack(side=LEFT, padx=5, pady=5) 
    b4 = Button(buttonframe,state=DISABLED, text="Search", width=6,command=reply)
    b4.pack(side=LEFT, padx=5, pady=5) 
    b5 = Button(buttonframe, text="Show", width=6,command=show)
    b5.pack(side=LEFT, padx=5, pady=5)
    listframe=Frame(root,bg="red")
    #listframe.pack(fill=X,padx=160,pady=25)
    listframe.pack(side=LEFT,pady=25)
    
    Lb1 = Listbox(listframe)
    Lb1.insert(1, "Samsung")
    Lb1.insert(2, "Iphone")
    Lb1.insert(3, "Pixel")
    Lb1.insert(4, "L.G")
    Lb1.insert(5, "Motorola")
    #Lb1.insert(6, "Ruby")
    
    
             
    
    #Lb1.pack(side=TOP, padx=5, pady=5)
    
    # b4=Button(buttonframe,text="Add")
    # b4.pack()
    root.mainloop()