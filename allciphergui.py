from tkinter import *
from tkinter import messagebox
from pycipher import Caesar, Playfair

top = Tk()
top.geometry("500x500")
top.configure(background='black')


l1 = Label(top,text = "Message",bd =5, bg='cyan')
l1.place(x = 180,y = 250)

t1 = Entry(top,bd =5)
t1.place(x = 250,y = 250)



class cipher():

    def encr(self):
        global t1,t2,var
        val = t1.get()
        e_msg = Caesar(key=-3).encipher(val)
        msg = messagebox.showinfo('Encrypted', e_msg)

        var = StringVar()
        var.set(e_msg)
        t2 = Entry(top, bd=5, textvariable=var)
        t2.place(x=250, y=350)


    def decr(self):

        val = t2.get()
        e_msg = Caesar(key=-3).decipher(val)
        msg = messagebox.showinfo('Decrypted', e_msg)

        var1 = StringVar()
        var1.set(e_msg)
        t1 = Entry(top, bd=5, textvariable=var1)
        t1.place(x=250, y=250)

a = cipher()

b1 = Button(text = "Encrypt", bd = 3, command = a.encr, bg= 'green', activebackground = 'yellow')
b1.place(x =180,y = 300 )

b2 = Button(text="Decrypt", bd=3, command= a.decr, bg='green', activebackground='orange')
b2.place(x=320, y=300)






top.mainloop()

