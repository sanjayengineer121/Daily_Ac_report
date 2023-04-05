from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
import sqlite3,re
import tkinter as tk
import tkinter.font as tkFont
import ttkbootstrap as tb
from datetime import date
import tkinter,customtkinter
from tkcalendar import Calendar,DateEntry
import sqlite3,re
from ttkbootstrap import *
from tkinter import messagebox
from random import randint
import datetime as dd
from time import strftime

root=tb.Window(themename="solar")
root.title("Payment")
root.iconbitmap('img/payment-method.ico')
root.geometry(f"{1100}x{580}")

def create_code(event=""):
	paymthd=my_entry.get()
	ledger=ledgern.get()
	date=cal.entry.get()
	amo=amount.get()
	conn = sqlite3.connect('todo.db')
	cur1 = conn.cursor()
	cur1.execute("SELECT COUNT(*) as count_pet FROM payment")
	conn.commit()
	s=cur1.fetchall()
	vrch=str(s[0])[1:-2]
	rch=int(vrch)+1
	
	voucher="PE"+str(rch).zfill(5)


	if my_entry.get() == "" or my_entry.get().isspace() or ledgern.get()==""or amount.get()=="":
		messagebox.showerror(title="ERROR", message="Please Enter Required Data?")
		
            
		
	else:
		conn = sqlite3.connect('todo.db')
		cur = conn.cursor()

		cur.execute("INSERT INTO payment (paymethod,ledgername,Voucher,Amount,date) VALUES ( '"+paymthd+"', '"+ledger+"', '"+str(voucher)+"', '"+amo+"','"+date+"')")
		conn.commit()
		messagebox._show(title="Added", message="Succefully Added Payment Invoice")
		clear_all()



conn = sqlite3.connect('todo.db')
cur = conn.cursor()
cur.execute("SELECT COUNT(*) as count_pet FROM payment")
conn.commit()
s=cur.fetchall()

cur1 = conn.cursor()
cur1.execute("SELECT COUNT(*) as count_pet FROM payment")
conn.commit()
totalamo=cur1.fetchall()


import datetime
x='{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())

cur2 = conn.cursor()
cur2.execute("SELECT SUM(Amount) FROM payment")
conn.commit()
totalamo=cur2.fetchall()
totalamount=str(totalamo[0])[1:-2]

mete=tb.Meter(root,bootstyle="success",
subtext="Total Vouchers",
border="2px",
interactive=True,
stripethickness=10,
amounttotal=str(s[0])[1:-2],
amountused=str(s[0])[1:-2],
metersize=150,)
mete.place(x=868,y=20)

mq=tb.Meter(root,bootstyle="success",
subtext="Total Amount",
border="2px",
interactive=True,
stripethickness=10,
textleft="₹",
amounttotal=int(totalamount),
amountused=int(totalamount),
metersize=150,)
mq.place(x=868,y=200)

import datetime
x='{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())

cur2 = conn.cursor()
cur2.execute("SELECT sum(Amount) from payment WHERE date='"+x+"'")
conn.commit()
todayamo=cur2.fetchall()
todayamount=str(todayamo[0])[1:-2]
#print(todayamount)


if todayamount=="None":
	todayamount1="0"

	mq1=tb.Meter(root,bootstyle="success",
	subtext="Today Payment",
	border="2px",
	interactive=True,
	stripethickness=10,
	textleft="₹",
	amounttotal=100,
	amountused=0,
	metersize=150,)
	mq1.place(x=868,y=380)
else:
	todayamount1=str(todayamo[0])[1:-2]
	mq1=tb.Meter(root,bootstyle="success",
	subtext="Today Payment",
	border="2px",
	interactive=True,
	stripethickness=10,
	textleft="₹",
	amounttotal=int(todayamount1),
	amountused=int(todayamount1),
	metersize=150,)
	mq1.place(x=868,y=380)



from datetime import date
today = str(date.today())
print(today)

def clear_all(event=""):
	my_entry.delete(0, END)
	ledgern.delete(0, END)
	amount.delete(0, END)
	my_label.config(image='')


conn = sqlite3.connect('todo.db')
print("Connection.")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS payment (paymethod varchar(50) ,ledgername varchar(100),Voucher varchar(10) PRIMARY KEY,Amount varchar(8),date varchar(10))')
conn.commit()



conn = sqlite3.connect('todo.db')
print("Connection.")
c = conn.cursor()
c.execute("SELECT ledgername FROM Legders")
rows = c.fetchall()
#==============================payment/acceptance method
x = conn.cursor()
x.execute("SELECT paymthd from paymthd")
col=x.fetchall()
c=[]
#print(col)
for i in col:
    x=str(i)[2:-3]

    c.append(x)

countries=c

e1_str1=tk.StringVar()
# Create GUI

my_label = Label(root, text='Reciept Method')
my_label.place(x=20,y=20)
frame = Frame(root)
frame.place(x=20,y=60)

Label(
    frame,
    font = ('Times',21),
    text='Countries in North America '
    ).place(x=20,y=60)

my_entry = AutocompleteCombobox(
    frame, 
    width=20, 
    font=('Times', 18),
    completevalues=countries
    )
my_entry.pack()

my_label = Label(root, text='Date')
my_label.place(x=350,y=20)

cal = DateEntry(root,width=20)
cal.place(x=350,y=60)
#recieptl=Listbox(root,width=43)
#recieptl.place(x=20,y=100)
my_label = Label(root, text='Select Ledger/Customer')
my_label.place(x=20,y=280)
my_label = Label(root, text='Amount')
my_label.place(x=350,y=280)
ledgern =Entry(bootstyle="success",font=("Helvetica", 18),textvariable=e1_str1)
ledgern.place(x=20,y=320)
amount = Label(root, text='₹')
amount.place(x=330,y=320)
amount = Entry(root, font=("Helvetica", 18),width=10)
amount.place(x=350,y=320)
ledger1=Listbox(root,width=43,height=26)
ledger1.place(x=550,y=160)
#====================================

#def update(data):
#	ledger1.delete(0,END)

#	for item in data:
#		x=''.join(item)
#		ledger1.insert(END, x)


#def update1(data):
#	recieptl.delete(0,END)
#
#	for item in data:
#		x=''.join(item)
#		recieptl.insert(END, x)




def my_upd1(my_widget): 
    my_w1 = my_widget.widget
    index = int(my_w1.curselection()[0]) 
    value = my_w1.get(index) 
    e1_str1.set(value) 
    for row in my_list1:
        if row[0]==value: 
            print("d: ",row[0])
                
            break
    ledger1.delete(0,END)





def my_down1(my_widget): 
    ledger1.focus()  
    ledger1.selection_set(0) 


#===================================

def fillout(e):
	ledgern.delete(0,END)

	ledgern.insert(0, ledger1.get(ACTIVE))

def fillout1(e):
	my_entry.delete(0,END)

	my_entry.insert(0, recieptl.get(ACTIVE))

#=======================================

def check(e):
	# grab what was typed
	typed = ledgern.get()

	if typed == '':
		data = rows
	else:
		data = []
		for item in rows:
			if typed.lower() in str(item).lower():
				data.append(item)

	# update our listbox with selected items
	update(data)	


#================================Method search
def check1(e):
	# grab what was typed
	typed = my_entry.get()

	if typed == '':
		data = col
	else:
		data = []
		for item in col:
			if typed.lower() in str(item).lower():
				data.append(item)

	# update our listbox with selected items
	update1(data)				
#list data



#list data
conn = sqlite3.connect('todo.db')
print("Connection.")
c = conn.cursor()
c.execute("SELECT ledgername FROM Legders")
rows = c.fetchall()
#==============================payment/acceptance method
x = conn.cursor()
x.execute("SELECT paymthd from paymthd")
col=x.fetchall()

my_list=col
my_list1=rows

def get_data1(*args): # populate the Listbox with matching options 
    search_str1=ledgern.get() # user entered string 
    ledger1.delete(0,END)     # Delete all elements of Listbox
    for element in my_list1:
        if(re.match(search_str1,element[0],re.IGNORECASE)):
            ledger1.insert(tk.END,element[0])



#=====================================
def addledger(event=""):
	from subprocess import call
	call(["python","ledger.py"])

my_button = customtkinter.CTkButton(master=root, text="Add Payment Voucher(CTRL+A)", command=create_code)
my_button.place(x=5,y=550)
root.bind('<Control-a>',create_code)
my_button = customtkinter.CTkButton(master=root, text="Add Customer(CTRL+L)",fg_color="pink",text_color="red", command=addledger)
my_button.place(x=210,y=550)
root.bind('<Control-l>',addledger)
my_button2 = customtkinter.CTkButton(master=root, text="Clear(Esc)",text_color="red",fg_color="yellow", command=clear_all)
my_button2.place(x=370,y=550)

def qui(event=""):
	quit()

root.bind('<F5>',qui)
root.bind('<Escape>',clear_all)


ledgern.bind('<Down>', my_down1) 
ledger1.bind('<Right>', my_upd1)
ledger1.bind('<Return>', my_upd1)

e1_str1.trace('w',get_data1)

root.mainloop()

