#calculator
from audioop import add
from tkinter import *
root=Tk()
input=Entry(root,width=50)#creating input box
input.grid(row=0,column=0,columnspan=4,padx=15, pady=15)#it gives space in the horizontal and vertical side of input box

def click(num):
    current=input.get()#to get the element which is already present in the entry box
    input.delete(0,END)#after storing the current value in the variable, delete it.
    input.insert(0,str(current)+str(num))#then print both the already present value and the newly entered value.
    return


def add():
    click("+")
    input.delete(2,END)
    cur=input.get()
    click("+")
    global fnum
    fnum=int(cur)
    return 
    

def sub():
    click("-")
    input.delete(2,END)
    cur=input.get()
    click("-")
    global fnum
    fnum=int(cur)
    return 


def mul():
    click("*")
    input.delete(2,END)
    cur=input.get()
    click("*")
    global fnum
    fnum=int(cur)
    return       


def div():
    click("/")
    input.delete(2,END)
    cur=input.get()
    click("+")
    global fnum
    fnum=int(cur)
    return


def mod():
    click("%")
    input.delete(2,END)
    cur=input.get()
    click("%")
    global fnum
    fnum=int(cur)
    return    

def clear():
    input.delete(0,END)
    return


def equ():
    input.delete(0,3)
    cur=input.get()
    snum=int(cur)
    input.delete(0,END)
    input.insert(0,str(fnum+snum))
    return           

bt1=Button(root,text="1",padx=50,pady=25,command=lambda:click(1))#we cannot simply pass the value here in to those function,so we are using lambda .
bt2=Button(root,text="2",padx=50,pady=25,command=lambda:click(2))
bt3=Button(root,text="3",padx=50,pady=25,command=lambda:click(3))
bt4=Button(root,text="4",padx=50,pady=25,command=lambda:click(4))
bt5=Button(root,text="5",padx=50,pady=25,command=lambda:click(5))
bt6=Button(root,text="6",padx=50,pady=25,command=lambda:click(6))
bt7=Button(root,text="7",padx=50,pady=25,command=lambda:click(7))
bt8=Button(root,text="8",padx=50,pady=25,command=lambda:click(8))
bt9=Button(root,text="9",padx=50,pady=25,command=lambda:click(9))
bt0=Button(root,text="0",padx=110,pady=25,command=lambda:click(0))
btadd=Button(root,text="+",padx=50,pady=25,command=add)
btsub=Button(root,text="-",padx=50,pady=25,command=sub)
btmul=Button(root,text="*",padx=50,pady=25,command=mul)
btdiv=Button(root,text="/",padx=50,pady=25,command=div)
btmod=Button(root,text="%",padx=50,pady=25,command=mod)
btdot=Button(root,text=".",padx=50,pady=25,command=click)
allclr=Button(root,text="AC",padx=45,pady=25,command=clear)
btequ=Button(root,text="=",padx=105,pady=25,command=equ)


allclr.grid(row=1,column=0)
btmod.grid(row=1,column=1)
btdiv.grid(row=1,column=2)
btmul.grid(row=1,column=3)
bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)
btadd.grid(row=2,column=3)
bt4.grid(row=3,column=0)
bt5.grid(row=3,column=1)
bt6.grid(row=3,column=2)
btsub.grid(row=3,column=3)
bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)
bt3.grid(row=4,column=2)
btdot.grid(row=4,column=3)
bt0.grid(row=5,column=0,columnspan=2)
btequ.grid(row=5,column=2,columnspan=2)


root.mainloop()