from tkinter import *
from tkinter import messagebox
import pyqrcode
import ttkbootstrap as tb
from ttkbootstrap import *
import tkinter,customtkinter
import os,sqlite3
import requests


ws = tb.Window(themename="solar")
ws.title("GET PAYMENT")
ws.iconbitmap('img/visa.ico')
ws.geometry(f"{1100}x{580}")
ws.resizable(False,FALSE)

#================================Generate QR code Block

def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        upiid="upi://pay?pa=yadav.154@paytm&am="+user_input.get()+"&cu=INR"
        qr = pyqrcode.create(upiid)
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass

#=====================LIST BOX TO SHOW LEDGER NAME

lis=Listbox(ws,width=45,height=26)
lis.place(x=800,y=120)
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute("SELECT ledgername FROM Legders")
rows = c.fetchall()

for row in rows:
    #print(type(row))
    ldelimiter = ','
    ldelimiter = ldelimiter.join(row)
    
    #x=ldelimiter[1:-2]
    lis.insert('0', ldelimiter)
conn.commit()


#================================Display QR code Block

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())

#=================================Add UPI Block

def addupi():
    print("add Upi clicked")

#=================================Add BANK Block

def addbank():
    pass

#=================================SEND QR CODE PARTY

def sendtoparty():

    #qr.svg('img/s.svg',scale=6)
    mbl=e.get()
    import glob
    x=os.path.abspath('img/s.svg')
    print(x)
    attach=x
    message="“Hacking Wifi” sounds really cool and interesting. But actually hacking wifi practically is much easier with a good wordlist. But this world list is of no use until we don’t have any idea of how to actually use that word list in order to crack a hash. And before cracking the hash we actually need to generate it. So, below are those steps along with some good wordlists to crack a WPA/WPA2 wifi."
    Api="http://127.0.0.1:8082/send_att?mobile="+mbl+"&message="+message+"&attach="+attach
    whatsAppHitApi = requests.get(Api)
    print(whatsAppHitApi)

def delete(self):
    s=self.lista.get(ANCHOR)
    print(s)
    s1=''.join(s)
    print(s1)
    print(type(s1))
    self.c.execute('DELETE FROM todo WHERE title="'+s1+'"')
    print(self.c.fetchall())
    self.conn.commit()
    self.lista.delete(ANCHOR)






#=================================SAVE QR CIDE Block
import png
def Saveqr():
    #qr.show(img)
    qr.svg('img/s.svg',scale=8)

#===================================LABEL of ENTER AMOUNT

lbl = Label(
    ws,
    text="ENTER AMOUNT OF PAYMENT QR CODE",
    background='#F25252'
    )
lbl.pack()

#=================================ENTER AMOUNT Block

user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
    )
entry.pack(padx=10,pady=10)

#=============================UPI BUTTON

UPIPIC=PhotoImage(file="img/upi_logo_.png")
UPI=UPIPIC.subsample(6,6)

button2 = ttk.Button(
    ws,
    image=UPI,
    text = "ADD UPI",
    width=15,
    compound=RIGHT,
    style='info.TButton',
    command = addupi
    )
button2.place(x=215,y=70)

#=============================BANK BUTTON

BANKPIC=PhotoImage(file="img/bank_78392.png")
BANK=BANKPIC.subsample(5,5)

button = Button(
    ws,
    image=BANK,
    text = "ADD BANK INFO",
    width=15,
    bootstyle='success',
    compound=RIGHT,
    command = addbank
    )
button.place(x=350,y=70)

#=============================QR GENRATE BUTTON

REpic=PhotoImage(file="img/qrcodescan.png")
qrc=REpic.subsample(6,6)

button1 = Button(
    ws,
    image=qrc,
    text = "generate_QR",
    width=15,
    compound=RIGHT,
    command = generate_QR
    )
button1.place(x=485,y=70)

#=============================SAVE BUTTON

PHOTOIM=PhotoImage(file="img/Save_37110.png")
SAVE=PHOTOIM.subsample(6,6)

button4 = Button(
    ws,
    image=SAVE,
    text = "SAVE QR",
    width=15,
    compound = RIGHT,
    bootstyle="dark",
    command = Saveqr
    )
button4.place(x=620,y=70)

#=============================WHATSAPPP SEND BUTTON

photo=PhotoImage(file="img/whatsapp (2).png")
img=photo.subsample(6,6)

button3 = Button(
    ws,
    image=img,
    text = "SEND QR",
    width=15,
    compound = LEFT,
    style='warning.TButton',
    command = sendtoparty,
    )
button3.place(x=755,y=70)

#=====================CUSTOMER NAME LABEL

lbl=Label(text="Customer Number")
lbl.place(x=900,y=50)

e=Entry(bootstyle="success")
e.place(x=900,y=70)

#=====================CUSTOMER NAME LABEL

def checkn():
    s=lis.get(ANCHOR)
    #print(s)
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT Mobile_no from Legders WHERE ledgername="'+s+'"')
    y = c.fetchall()

    number1=""
    for x in y:

        number = ','
        number = number.join(x)
        number1=number
    print(number1)

    e.delete(0, 'end')
    e.insert(0, number1)

    def leave(*args):
        e.delete(0, 'end')
        e.insert(0, number1)
                
    e.bind("Button-1", click)
    e.bind("<Button-1>", leave)

#================================Select Customer Button

CUS=PhotoImage(file="img/support.png")
PARTY=CUS.subsample(6,6)

button3 = Button(
    ws,
    image=PARTY,
    text = "CHOOSE PARTY",
    width=15,
    compound = LEFT,
    style='SUCCESS',
    command = checkn,
    )
button3.place(x=880,y=540)

#================================Display QR code Block

img_lbl = Label(
    ws,
    background='light blue')
img_lbl.pack(pady=33)
output = Label(
    ws,
    text="",
    background='#F25252'
    )
output.pack(pady=0)
 
ws.mainloop()