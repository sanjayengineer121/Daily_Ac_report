import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from datetime import date
import datetime as dd
import tkinter,customtkinter
from tkcalendar import Calendar,DateEntry
from time import strftime
import sqlite3
import ttkbootstrap as tb

#root = Tk()
#root.title("Add Ledger")
#root.iconbitmap('img/ledger.ico')
#root.geometry(f"{1100}x{580}")
#root.resizable(width=False, height=False)

import ttkbootstrap as tb

root=tb.Window(themename="solar")
root.title("Ledger/Customer")
root.iconbitmap('img/ledger.ico')
root.geometry(f"{1100}x{580}")
root.resizable(width=False, height=False)


conn = sqlite3.connect('todo.db')
print("Connection.")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Legders (Ledgername varchar(50) PRIMARY KEY,cus_name varchar(30),address varchar(100),Mobile_no varchar(10),GST varchar(15),Pan varchar(10))')
conn.commit()

# Create GUI

conn = sqlite3.connect('todo.db')
cur = conn.cursor()
data="SELECT COUNT(*) as count_pet FROM Legders"
cur.execute("SELECT COUNT(*) as count_pet FROM Legders")
conn.commit()
s=cur.fetchall()

mete=tb.Meter(root,bootstyle="success",
subtext="TOTAL CUSTOMER",
border="2px",
interactive=True,
stripethickness=10,
amounttotal=str(s[0])[1:-2],
amountused=str(s[0])[1:-2],
metersize=150,)
mete.place(x=868,y=0)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

date = dd.datetime.now()
lbl = tk.Label(root, font=('calibri', 40, 'bold'),background='purple',foreground='white')
lbl.place(x=500,y=20)
time()

name_alias = Label(root, text='Name(alias)',highlightthickness=2)
name_alias.place(x=20,y=20)
alias = Entry(root, font=("Helvetica", 18),highlightthickness=2)
alias.place(x=130,y=20)

my_label = Label(root, text='Category',highlightthickness=2)
my_label.place(x=20,y=240)

mailaddr = Label(root, text='Mailing Details',highlightthickness=2)
mailaddr.place(x=330,y=150)

namead = Label(root, text='Name',highlightthickness=2)
namead.place(x=330,y=200)

addr = Label(root, text='Address',highlightthickness=2)
addr.place(x=330,y=250)

mbl = Label(root, text='Mobile No.',highlightthickness=2)
mbl.place(x=330,y=320)

Banking = Label(root, text='Banking Info',highlightthickness=2)
Banking.place(x=330,y=380)

pan = Label(root, text='PAN',highlightthickness=2)
pan.place(x=330,y=440)

gst = Label(root, text='GST',highlightthickness=2)
gst.place(x=330,y=480)

nameinfo = Entry(root, font=("Helvetica", 18),highlightthickness=2)
nameinfo.place(x=460,y=210)

addrinfo = Entry(root, font=("Helvetica", 18),highlightthickness=2)
addrinfo.place(x=460,y=260)

mblinfo = Entry(root, font=("Helvetica", 18),highlightthickness=2)
mblinfo.place(x=460,y=330)

paninfo = Entry(root, font=("Helvetica", 18),highlightthickness=2)
paninfo.place(x=460,y=440)

gstinfo = Entry(root, font=("Helvetica", 18),highlightthickness=2)
gstinfo.place(x=460,y=480)


def ver():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT Ledgername FROM Legders")
    rows = c.fetchall()
    for row in rows:
        lista.insert('0', row)
    conn.commit()

lista=Listbox(root,width=30,highlightthickness=1,font=('Andalus', 12, 'bold'),selectmode=BROWSE,bg='light blue',selectbackground='#89a592',selectforeground='#ff1493', selectborderwidth=3, activestyle=NONE)
lista.place(x=720,y=150,width=300,height=400)
scroll = Scrollbar(root, orient=VERTICAL)
scroll2 = Scrollbar(root, orient=HORIZONTAL)
lista.config(yscrollcommand=scroll.set, xscrollcommand=scroll2.set)
scroll.config(command=lista.yview)
scroll2.config(command=lista.xview)

ver()

def GButton_235_command(event=""):
    quit()


def GButton_125_command(event=""):
        Ledgername=alias.get()
        cus_name=nameinfo.get()
        address=addrinfo.get()
        Mobile_no=mblinfo.get()
        GST=paninfo.get()
        Pan=gstinfo.get()
        print(Ledgername)
        print(cus_name)
        print(address)
        print(Mobile_no)
        print(GST)
        print(Pan)

        if alias.get() == "" or alias.get().isspace() or nameinfo.get()==""or mblinfo.get()=="":
            messagebox.showinfo(title="Error", message="Please Enter Ledger&Mobile No. ?")
            
        else:

        
            conn = sqlite3.connect('todo.db')
            #conn = create_connection()
            cur = conn.cursor()
            cur.execute("SELECT * from Legders WHERE ledgername='"+Ledgername+"'")
            record = cur.fetchone()
            if record is None:
                cur.execute("INSERT INTO Legders (Ledgername,cus_name,address,Mobile_no,GST,Pan) VALUES ( '"+Ledgername+"', '"+cus_name+"','"+address+"','"+Mobile_no+"','"+GST+"','"+Pan+"')")
                print("customer null: ")
                conn.commit()
                messagebox.showinfo("Ledger","'"+Ledgername+"' Added To DataBase")
            else:
                print("customer not null: ")
                messagebox.showerror("Error","'"+Ledgername+"' Already To Exist")
            return record  
    
    #cur.close()


        



GButton_235 = customtkinter.CTkButton(root, text="Close",text_color="red",fg_color="yellow", command=GButton_235_command)

GButton_235.place(x=40,y=550)
    #btn = Button

GButton_125 = customtkinter.CTkButton(root, text="Add Ledger", command=GButton_125_command)

GButton_125.place(x=540,y=550)
root.bind('<Control-a>',GButton_125_command)
root.bind('<Escape>',GButton_235_command)
root.mainloop()

