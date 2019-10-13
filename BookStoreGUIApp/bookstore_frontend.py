"""
A program that stores this book information
Title, Author
year, ISBN

User can:
View all records
Search an entru
Add entry
Update Entry
Delete
Close
"""
from tkinter import *
import bookstore_backend

def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in bookstore_backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in bookstore_backend.search(titletext.get(),authortext.get(),yeartext.get(),isbntext.get()):
        list1.insert(END,row)

def addentry_command():
    bookstore_backend.insert(titletext.get(),authortext.get(),yeartext.get(),isbntext.get())
    search_command()

def update_command():
    bookstore_backend.update(selected_tuple[0],titletext.get(),authortext.get(),yeartext.get(),isbntext.get())
    view_command()

def delete_command():
    bookstore_backend.delete(selected_tuple[0])
    view_command()

def close_command():
    window 


window = Tk()

window.wm_title("BookStore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

titletext=StringVar()
e1=Entry(window,textvariable=titletext)
e1.grid(row=0,column=1)
authortext=StringVar()
e2=Entry(window,textvariable=authortext)
e2.grid(row=0,column=3)

yeartext=StringVar()
e3=Entry(window,textvariable=yeartext)
e3.grid(row=1,column=1)
isbntext=StringVar()
e4=Entry(window,textvariable=isbntext)
e4.grid(row=1,column=3)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.config(yscrollcommand=sb1.set,exportselection=FALSE)
sb1.config(command=list1.yview)


list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=addentry_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()

