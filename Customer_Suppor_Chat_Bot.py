from tkinter import *
from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
import tkinter as tk
import random


root=Tk()
root.geometry("560x420+0+0")
root.title("Chat BOT")
root.configure(background='white')


Tops=Frame(root,width=560,height=100,bd=14,relief='raise')
Tops.pack(side=TOP)
f1=Frame(root,width=560,height=600,bd=10,background='blue',relief="raise")
f1.pack(side=BOTTOM)
f2=Frame(root,width=560,height=600,bd=10,background='blue',relief="raise")
f2.pack(side=BOTTOM)
frameBottom1=Frame(f2,width=560,height=600,bd=6,background='light green',relief="flat")
frameBottom1.pack(side=BOTTOM)
frameBottom=Frame(f1,width=560,height=600,bd=6,background='light green',relief="flat")
frameBottom.pack(side=BOTTOM)
f1a=Frame(f1,width=560,height=600,bd=0,background='white',relief="flat")
f1a.pack(side=TOP)
topLeft2=Frame(f1a,width=560,height=600,bd=8,background='white',relief="raise")
topLeft2.pack(side=TOP)


Tops.configure(background="light blue")
lblTitle=Label(Tops,font=('arial',25,'bold'),text="Customer Support Chat BOT",bd=12,background='light blue',width=25,justify='center')
lblTitle.grid(row=0,column=0)

var1=StringVar()
var1.set('')
var2=StringVar()
var2.set('')
var3=StringVar()
var3.set('')

entOneWay=Entry(frameBottom,font=('arial',20,'bold'),textvariable=var1,bd=2,width=15)
entOneWay.pack(side=LEFT)



scrollbary = Scrollbar(topLeft2)
scrollbary.pack(side=RIGHT, fill=Y)

text_box = Text(topLeft2,width = 63, height = 100)
text_box.bind("<Key>", lambda e: "break")
text_box.pack()



def product():
    if var2.get()=='laptop':
        text_box.insert("end-1c", "\nYOU-> " + 'laptop')
        text_box.insert("end-1c", "\nBOT-> Enter quantity\n")
    if var2.get()=='mobile':
        text_box.insert("end-1c", "\nYOU-> " + 'mobile')
        text_box.insert("end-1c", "\nBOT-> Enter quantity\n")
    if var2.get()=='book':
        text_box.insert("end-1c", "\nYOU-> " + 'book')
        text_box.insert("end-1c", "\nBOT-> Enter quantity\n")
    if var2.get()=='camera':
        text_box.insert("end-1c", "\nYOU-> " + 'camera')
        text_box.insert("end-1c", "\nBOT-> Enter quantity\n")

def quantity():
    if var3.get()=='1':
        text_box.insert("end-1c", "\nYOU-> " + '1')
        text_box.insert("end-1c", "\nBOT-> Order placed\n")
    if var3.get()=='2':
        text_box.insert("end-1c", "\nYOU-> " + '2')
        text_box.insert("end-1c", "\nBOT-> Order placed\n")
    if var3.get()=='3':
        text_box.insert("end-1c", "\nYOU-> " + '3')
        text_box.insert("end-1c", "\nBOT-> Order placed\n")
    if var3.get()=='4':
        text_box.insert("end-1c", "\nYOU-> " + '4')
        text_box.insert("end-1c", "\nBOT-> Order placed\n")


def quit():
    root.destroy()

 

def x(event = None):
    #Get the string of the user_entry widget
    guess = var1.get()
    
    if guess=='new order' :
        cboDestination = ttk.Combobox(frameBottom, textvariable=var2, state='readonly', font=('arial', 12, 'bold'), width=9)
        cboDestination['value'] = ('Products', 'laptop', 'mobile', 'book', 'camera')
        cboDestination.current(0)
        cboDestination.pack(side=LEFT)
        btnOk = Button(frameBottom, text='Ok', padx=2, pady=2, bd=3, fg="black", background='light blue',
                        font=('Arial Rounded MT', 8, 'bold'), width=4, height=1, command=product).pack(side=LEFT)
        cboDestination = ttk.Combobox(frameBottom, textvariable=var3, state='readonly', font=('arial', 12, 'bold'), width=9)
        cboDestination['value'] = ('Quantity', '1', '2', '3', '4')
        cboDestination.current(0)
        cboDestination.pack(side=LEFT)
        btnQuan = Button(frameBottom, text='Add', padx=2, pady=2, bd=3, fg="black", background='light blue',
                        font=('Arial Rounded MT', 8, 'bold'), width=4, height=1, command=quantity).pack(side=RIGHT)
   
    
    y=['order status','cancel order','new order','offers','faq']
    c=["laptop","mobile","book","camera"]
    faq=['how to cancel order','how to change password','how to change phone number']
    offers=["flat ₹100 off on first order","100% cashback upto ₹50 on visa cards","buy 1 get 1 on grossery on last date of every month"]
    status=['Item Packed and ready to be shipped','Item dispathced/shipped','Shipment arrived at facility near you','Product out for delivery','Item delivered']
    o_st=random.choices(status)
    ran=random.randint(1, 5)
    o_no="AMZ"+str(ran)
    if guess=="thankyou":
        text_box.insert("end-1c", "\n\nYOU-> " + guess)
        text_box.insert("end-1c", "\nBOT-> Thank You have a nice day\nVisit again\n\n")
    if guess=='quit':
        quit()
    if guess == 'hi':
        text_box.insert("end-1c", "YOU-> " + 'hi')
        text_box.insert("end-1c", "\nBOT-> Hi!\n")
        text_box.insert("end-1c", "How may I help you!!\n")
        list1 = ["1.Order status", "2.Cancel order", "3.New Order", "4.Offers", "5.Help"]
        for i in range(0, len(list1)):
            text_box.insert("end-1c", list1[i] + "\n")

        text_box.config(yscrollcommand=scrollbary.set)
        scrollbary.config(command=text_box.yview)

    for i in range(0,len(y)):
        if y[0]==guess:
            text_box.insert("end-1c","\nYOU-> "+guess)
            text_box.insert("end-1c","\nBOT-> Your order no. = {}".format(o_no)+"\n")
            text_box.insert("end-1c",o_st)
            break
        elif y[1]==guess:
            text_box.insert("end-1c","\n\nYOU-> "+guess)
            text_box.insert("end-1c","\nBOT-> Your order id "+o_no+" is cancelled successfully\n")
            break
        elif y[2]==guess:
            text_box.insert("end-1c","\n\nYOU-> "+guess)
            text_box.insert("end-1c","\nBOT-> Enter product name\n")
            
            for j in range(0, len(c)):
                text_box.insert("end-1c", c[j] + "\n")
            break
        elif y[3]==guess:
            text_box.insert("end-1c", "\n\nYOU-> " + guess)
            text_box.insert("end-1c", "\nBOT-> Offers =>\n")
            for j in range(0, len(offers)):
                text_box.insert("end-1c", "*"+offers[j] + "\n")
            break
    for x in range(0,len(faq)):
        if guess==faq[0]:
            text_box.insert("end-1c", "\n\nYOU-> " + guess)
            text_box.insert("end-1c", "\nBOT-> To cancel order follow steps :-\n")
            text_box.insert("end-1c","\nGo to My Orders->Select order->Click on cancel order->Enter valid reason and click OK\n")
            break
        elif guess==faq[1]:
            text_box.insert("end-1c", "\n\nYOU-> " + guess)
            text_box.insert("end-1c", "\nBOT-> To change password follow steps :-\n")
            text_box.insert("end-1c","\nGo to My Profile->Security->Password->Enter current password->Enter new password and save\n")
            break
        elif guess==faq[2]:
            text_box.insert("end-1c", "\n\nYOU-> " + guess)
            text_box.insert("end-1c", "\nBOT-> To change mobile number follow steps :-\n")
            text_box.insert("end-1c","\nGo to My Profile->Edit Profile->Mobile number->Click Edit number->Enter new mobile number->Click Save\n")
            break
        guess=entOneWay.get()
    
        entOneWay.delete(0,END)


entOneWay.bind("<Return>", x)

root.mainloop()