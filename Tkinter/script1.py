from tkinter import *




#GUI are generated using window & widgets

window = Tk()

"""
def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

b1=Button(window,text="Execute",command=km_to_miles)
# pack & grid are used to make these button to visible
b1.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)
"""

def kg_to_others():
    grams.delete("1.0",END)
    pounds.delete("1.0",END)
    ounces.delete("1.0",END)
    grams.insert(END,float(kg.get())*1000)
    pounds.insert(END,float(kg.get())*2.20426)
    ounces.insert(END,float(kg.get())*35.274)    

kg_label = Label(window,text="Kgs : ")

kg_value = StringVar()
kg = Entry(window,textvariable=kg_value)
grams = Text(window,height=1,width=20)
pounds = Text(window,height=1,width=20)
ounces = Text(window,height=1,width=20)
convertbtn = Button(window,text="Convert",command=kg_to_others)

kg_label.grid(row=0,column=0)
kg.grid(row=0,column=1)
convertbtn.grid(row=0,column=2)

grams.grid(row=1,column=0)
pounds.grid(row=1,column=1)
ounces.grid(row=1,column=2)

window.mainloop()
