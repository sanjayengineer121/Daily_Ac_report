import tkinter
from tkinter import *
import pyqrcode
import tkinter.messagebox
import customtkinter
import requests
import webbrowser
from tkinter import filedialog
import sqlite3
import webbrowser
from tkinter import ttk
import tkinter as tk

##importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time

w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='DAILY A/C REPORT', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='red', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('img/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('img/c1.png'))




for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
w.mainloop()




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
con = sqlite3.connect('todo.db')
cur = con.cursor()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Daily Use")
        self.geometry(f"{1100}x{580}")

#=====================configure grid layout (4x4)===================================

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

#======================create sidebar frame with widgets=============================

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Generate Qr",command=self.genqr)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Pay By Qr",command=self.Paybyqr)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="SCAN Qr",command=self.scanqr)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="NOTES",command=self.crnotes)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame,text="MORE",command=self.more)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance :", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Window Size :", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

#====================create main entry and button============================================

        #entry1_var = customtkinter.StringVar(value='Test')

        self.mobile = customtkinter.CTkEntry(self, placeholder_text="Mobile No.")
        self.mobile.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #print(entry1_var.get())

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,command=self.sendsms,text="SEND",text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

#================================create textbox/Listbox/Treeview====================================================
        #self.Listbox = customtkinter.listbox(self, width=250)
        #self.Listbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        style = ttk.Style()

#=====================Pick a theme

        style.theme_use("default")

#======================Style configure

        style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
#=========================Change selected color
        style.map('Treeview', 
        background=[('selected', 'blue')])

#============================Create Treeview Frame
        tree_frame = Frame(self)
        tree_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

#==============================Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

#================================Create Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

#===============================Pack to the screen
        my_tree.pack()

#===============================Configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

#=================================Define Our Columns
        my_tree['columns'] = ("Title", "Desc", "Date","Status")

#=================================Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Title", anchor=W, width=100)
        my_tree.column("Desc", anchor=CENTER, width=300)
        my_tree.column("Date", anchor=W, width=60)
        my_tree.column("Status", anchor=CENTER, width=40)
		

#====================================Create Headings 
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Title", text="Title", anchor=W)
        my_tree.heading("Desc", text="Description", anchor=CENTER)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Status", text="Status", anchor=W)

        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

#====================================Connecting Database

        con1 = sqlite3.connect("todo.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM todo")

        rows = cur1.fetchall()

        


            #self.Listbox.insert('end', row)

#==============================getting data in form of table

        global count
        count=0

        for record in rows:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3]), tags=('oddrow',))

            count += 1
    


#=============================================create tabview=================================

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CREATE")
        self.tabview.add("ALTER")
        self.tabview.add("VOUCHER")
        self.tabview.tab("CREATE").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("ALTER").grid_columnconfigure(0, weight=1)
        self.tabview.tab("VOUCHER").grid_columnconfigure(0, weight=1)
        
#=============================================CREATE any Tab buttons tabview=================================

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CREATE"), text="Ledger",
                                                           command=self.addledger)

        self.paymentvOUCHER = customtkinter.CTkButton(self.tabview.tab("CREATE"), text="Stock Item",
                                                           command=self.addproduct)
        
        self.unitofproduct = customtkinter.CTkButton(self.tabview.tab("CREATE"), text="Unit(Measerment)",
                                                           command=self.addunit)

        self.voucherscerate = customtkinter.CTkButton(self.tabview.tab("CREATE"), text="S",
                                                           command=self.paymentvrch)
        
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.paymentvOUCHER.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.unitofproduct.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.voucherscerate.grid(row=5, column=0, padx=20, pady=(10, 10))
        
#=============================================Alter any Tab buttons tabview=================================

        self.string_input_button1 = customtkinter.CTkButton(self.tabview.tab("ALTER"), text="Ledger",
                                                           command=self.addledger)
        #self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab(""), text="CTkLabel on Tab 2")
        self.string_input_button1.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.paymentvOUCHER = customtkinter.CTkButton(self.tabview.tab("ALTER"), text="Stock Item",
                                                           command=self.addproduct)
        
        self.unitofproduct = customtkinter.CTkButton(self.tabview.tab("ALTER"), text="Unit(Measerment)",
                                                           command=self.addunit)

        self.paymentvOUCHER.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.unitofproduct.grid(row=2, column=0, padx=20, pady=(10, 10))

#=============================================CREATE any Tab buttons tabview=================================


        self.string_input_button2 = customtkinter.CTkButton(self.tabview.tab("VOUCHER"), text="Sale Voucher",
                                                           command=self.salesvrch)
        #self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab(""), text="CTkLabel on Tab 2")
        self.string_input_button2.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.string_input_button3 = customtkinter.CTkButton(self.tabview.tab("VOUCHER"), text="Reciept Voucher",
                                                           command=self.recirptvrch)
        #self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab(""), text="CTkLabel on Tab 2")
        self.string_input_button3.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.string_input_button4 = customtkinter.CTkButton(self.tabview.tab("VOUCHER"), text="Payment Voucher",
                                                           command=self.paymentvrch)
        #self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab(""), text="CTkLabel on Tab 2")
        self.string_input_button4.grid(row=2, column=0, padx=20, pady=(10, 10))

#=====================create radiobutton frame======================

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Select Payment Mode:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,text="UPI(VPA)", value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,text="BANK", value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, text="CASH",value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

#================================create checkbox and switch frame===============

        self.checkbox_slider_frame = customtkinter.CTkFrame(self,fg_color="blue")
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.labelofmenu= customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="-------MENU.-----",fg_color="red")


        self.labelofmenu.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        #self.flash()

        


        self.salesreport = customtkinter.CTkButton(master=self.checkbox_slider_frame,text="Sales Report",
                                                           command=self.salesrepo)

        self.salesreport.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        
        self.recieptreport = customtkinter.CTkButton(master=self.checkbox_slider_frame,text="Reciepr Report",
                                                           command=self.recieptrepo)

        self.recieptreport.grid(row=3, column=0, pady=10, padx=20, sticky="n")

        self.recieptreport = customtkinter.CTkButton(master=self.checkbox_slider_frame,text="Payment Report",
                                                           command=self.paymentvrch2)

        self.recieptreport.grid(row=4, column=0, pady=10, padx=20, sticky="n")


        self.search= customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Search..")

        self.search.grid(row=5, column=0, pady=10, padx=20, sticky="n")

        self.entrysearch= customtkinter.CTkEntry(master=self.checkbox_slider_frame, placeholder_text="Enter Voucher/Ledgers..")

        self.entrysearch.grid(row=6, column=0, pady=10, padx=20, sticky="n")

        self.buttonsearch = customtkinter.CTkButton(master=self.checkbox_slider_frame,text="Search Entry",
                                                           command=self.searchinfo)

        self.buttonsearch.grid(row=7, column=0, pady=10, padx=20, sticky="n")


#=======================create slider and progressbar frame==========================

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
       


#================================create textbox/Listbox/Treeview====================================================
        #self.Listbox = customtkinter.listbox(self, width=250)
        #self.Listbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        style = ttk.Style()

#=====================Pick a theme

        style.theme_use("default")

#======================Style configure

        style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
#=========================Change selected color
        style.map('Treeview', 
        background=[('selected', 'blue')])

#============================Create Treeview Frame
        newframe = Frame(self)
        newframe.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(60, 0), sticky="nsew")

#==============================Treeview Scrollbar
        myscrol = Scrollbar(newframe)
        myscrol.pack(side=RIGHT, fill=Y)

        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")


#================================Create Treeview
        transactiontree = ttk.Treeview(newframe, yscrollcommand=myscrol.set, selectmode="extended",columns=cols)

#===============================Pack to the screen
        transactiontree.pack()

#===============================Configure the scrollbar
        myscrol.config(command=transactiontree.yview)

#=================================Define Our Columns
        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")

        for i in cols:
                transactiontree.heading(column=f'{i}',text=f'{i}',anchor='w')
                transactiontree.column(column=f'{i}', width=150,minwidth=50,stretch=False)

#=================================Formate Our Columns
        
        transactiontree.tag_configure('oddrow', background="white")
        transactiontree.tag_configure('evenrow', background="lightblue")

#====================================Connecting Database

        con1 = sqlite3.connect("todo.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM payment")

        row = cur1.fetchall()

        


            #self.Listbox.insert('end', row)

#==============================getting data in form of table

        global count1
        count1=0

        for record in row:
            if count1 % 2 == 0:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
            else:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))

            count1 += 1
    





#====================set default values======================

        #self.checkbox_2.configure(state="disabled")
        #self.switch_2.configure(state="disabled")
        
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
        self.seg_button_1.configure(values=["PAYMENT", "RECIEPT", "SALES"])
        self.seg_button_1.set("Value 2")

#==========================ADDITION OF LEDGER BTN
    def addledger(self):
        from subprocess import call
        call(["python", "ledger.py"])
        
        #dialog1 = customtkinter.CTkInputDialog(text="ENTER LEDGERS DETAILS.:", title="LEDGERS.")
        #print("LEDGERS DETAIL is:")
    
#==========================ADDITION OF PRODUCT

    def addproduct(self):
        from subprocess import call
        call(["python", "product.py"])

#==========================ADDITION OF unIT

    def addunit(self):
        from subprocess import call
        call(["python", "unit.py"])

#==========================SENDING SMS WITH WHATSAPP API

    def sendsms(self):
        mbl=self.mobile.get()
        print(mbl)
        message="“Hacking Wifi” sounds really cool and interesting. But actually hacking wifi practically is much easier with a good wordlist. But this world list is of no use until we don’t have any idea of how to actually use that word list in order to crack a hash. And before cracking the hash we actually need to generate it. So, below are those steps along with some good wordlists to crack a WPA/WPA2 wifi."
        Api="http://127.0.0.1:8082/send?mobile="+mbl+"&message="+message
        whatsAppHitApi = requests.get(Api)
        
        
        #Api="http://127.0.0.1:8082/send_att?mobile=6388574919&message=HOW ARE YOU SIR"
        #whatsAppHitApi = requests.get(Api)
        #x = requests.get('https://api.github.com')
        print(whatsAppHitApi)

#==========================set appearance mode

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

#==========================CALLING GENERATION OF QR CODE

    def genqr(self):
        #dialog = customtkinter.CTkInputDialog(text="ENTER UNIT HERE.:", title="UNITS")
        #print("Number is:", dialog.get_input())
        import os
        from subprocess import call
        call(["python", "scandocument.py"])
        #exec(open('test.py').read())
        #from test import my_generate
        #Popen('scandocument.py')
        #import scandocument

#==========================GET PAYMENT FROM QR CODE

    def Paybyqr(self):
        from subprocess import call
        call(["python", "readqr.py"])
    
#==========================SCAN DOWNLOADED QR CODE

    def scanqr(self):
        from subprocess import call
        call(["python", "readqr.py"])
    
    #def crnotes(self):
        #print("sidebar_button click")

#==========================GET SOME MORE OPTION

    def more(self):
        from subprocess import call
        #call(["python", "server.py"])

#==========================GENERATE -TODO- INFO FROM THIS APP

    def crnotes(self):

        from subprocess import call
        call(["python", "notes.py"])

#==========================GET PAYMENT VOUCHER
    def paymentvrch(self):
        from subprocess import call
        call(["python","payment.py"])

#==========================GET SALES VOUCHER

    def salesvrch(self):
        pass

    def searchinfo(self):
        data=self.entrysearch.get()
        
        print(data)

        

        style = ttk.Style()

#=====================Pick a theme

        style.theme_use("default")

#======================Style configure

        style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
#=========================Change selected color
        style.map('Treeview', 
        background=[('selected', 'blue')])

#============================Create Treeview Frame
        newframe = Frame(self)
        newframe.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(60, 0), sticky="nsew")

#==============================Treeview Scrollbar
        myscrol = Scrollbar(newframe)
        myscrol.pack(side=RIGHT, fill=Y)

        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")


#================================Create Treeview
        transactiontree = ttk.Treeview(newframe, yscrollcommand=myscrol.set, selectmode="extended",columns=cols)

#===============================Pack to the screen
        transactiontree.pack()

#===============================Configure the scrollbar
        myscrol.config(command=transactiontree.yview)

#=================================Define Our Columns
        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")

        for i in cols:
                transactiontree.heading(column=f'{i}',text=f'{i}',anchor='w')
                transactiontree.column(column=f'{i}', width=150,minwidth=50,stretch=False)

#=================================Formate Our Columns
        
        transactiontree.tag_configure('oddrow', background="white")
        transactiontree.tag_configure('evenrow', background="lightblue")

#====================================Connecting Database

        con1 = sqlite3.connect("todo.db")

        cur1 = con1.cursor()
        cur2 = con1.cursor()

        cur1.execute("SELECT * from payment WHERE ledgername like'"+data+"%'")
        cur2.execute("SELECT * FROM reciept WHERE ledgername like'"+data+"%'")

        row = cur1.fetchall()
        row1 = cur2.fetchall()

        row=row+row1
        #print(row1)

        


            #self.Listbox.insert('end', row)

#==============================getting data in form of table

        global count1
        count1=0

        for record in row:
            if count1 % 2 == 0:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
            else:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))

            count1 += 1

        


#==========================GET RECIEPT VOUCHER

    def recirptvrch(self):
        from subprocess import call
        call(["python","reciept.py"])

#==========================CALLING MAIN FUNCTION

    def paymentvrch2(self):
        
        style = ttk.Style()

#=====================Pick a theme

        style.theme_use("default")

#======================Style configure

        style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
#=========================Change selected color
        style.map('Treeview', 
        background=[('selected', 'blue')])

#============================Create Treeview Frame
        newframe = Frame(self)
        newframe.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(60, 0), sticky="nsew")

#==============================Treeview Scrollbar
        myscrol = Scrollbar(newframe)
        myscrol.pack(side=RIGHT, fill=Y)

        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")


#================================Create Treeview
        transactiontree = ttk.Treeview(newframe, yscrollcommand=myscrol.set, selectmode="extended",columns=cols)

#===============================Pack to the screen
        transactiontree.pack()

#===============================Configure the scrollbar
        myscrol.config(command=transactiontree.yview)

#=================================Define Our Columns
        cols = ("Payment_method", "Ledger_ac", "Voucher", "Amount", "Date")

        for i in cols:
                transactiontree.heading(column=f'{i}',text=f'{i}',anchor='w')
                transactiontree.column(column=f'{i}', width=150,minwidth=50,stretch=False)

#=================================Formate Our Columns
        
        transactiontree.tag_configure('oddrow', background="white")
        transactiontree.tag_configure('evenrow', background="lightblue")

#====================================Connecting Database

        con1 = sqlite3.connect("todo.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM payment")

        row = cur1.fetchall()

        


            #self.Listbox.insert('end', row)

#==============================getting data in form of table

        global count1
        count1=0

        for record in row:
            if count1 % 2 == 0:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
            else:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))

            count1 += 1
            
        

    def salesrepo():
        pass






#==========================CALLING MAIN FUNCTION

    def recieptrepo(self):
        style = ttk.Style()

#=====================Pick a theme

        style.theme_use("default")

#======================Style configure

        style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
#=========================Change selected color
        style.map('Treeview', 
        background=[('selected', 'blue')])

#============================Create Treeview Frame
        newframe = Frame(self)
        newframe.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(60, 0), sticky="nsew")

#==============================Treeview Scrollbar
        myscrol = Scrollbar(newframe)
        myscrol.pack(side=RIGHT, fill=Y)

        cols = ("Reciept_method", "Ledger_ac", "Voucher", "Amount", "Date")


#================================Create Treeview
        transactiontree = ttk.Treeview(newframe, yscrollcommand=myscrol.set, selectmode="extended",columns=cols)

#===============================Pack to the screen
        transactiontree.pack()

#===============================Configure the scrollbar
        myscrol.config(command=transactiontree.yview)

#=================================Define Our Columns
        cols = ("Reciept_method", "Ledger_ac", "Voucher", "Amount", "Date")

        for i in cols:
                transactiontree.heading(column=f'{i}',text=f'{i}',anchor='w')
                transactiontree.column(column=f'{i}', width=150,minwidth=50,stretch=False)

#=================================Formate Our Columns
        
        transactiontree.tag_configure('oddrow', background="white")
        transactiontree.tag_configure('evenrow', background="lightblue")

#====================================Connecting Database

        con1 = sqlite3.connect("todo.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM reciept")

        row = cur1.fetchall()

        


            #self.Listbox.insert('end', row)

#==============================getting data in form of table

        global count1
        count1=0

        for record in row:
            if count1 % 2 == 0:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('evenrow',))
            else:
                transactiontree.insert(parent='', index='end', iid=count1, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))

            count1 += 1
    



if __name__ == "__main__":
    app = App()
    app.mainloop()
    