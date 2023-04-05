import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
import sqlite3
import ttkbootstrap as tb
from time import strftime
import datetime as dd
from datetime import date



class App:
    def __init__(self):
        #setting title
        self.window = tb.Window(themename="solar")
        self.window.title('PRODUCT')
        self.window.iconbitmap('img/product.ico')
        width=1100
        height=580
        #self.geometry('1100x580')

        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)


        conn = sqlite3.connect('todo.db')
        cur = conn.cursor()
        data="SELECT COUNT(*) as count_pet FROM product"
        cur.execute("SELECT COUNT(*) as count_pet FROM product")
        conn.commit()
        s=cur.fetchall()

        mete=tb.Meter(self.window,bootstyle="success",
        subtext="TOTAL Product",
        border="2px",
        interactive=True,
        stripethickness=10,
        amounttotal=str(s[0])[1:-2],
        amountused=str(s[0])[1:-2],
        metersize=150,)
        mete.place(x=868,y=20)

        
        import datetime as dd

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        date = dd.datetime.now()
        lbl = tk.Label(self.window, font=('calibri', 40, 'bold'),background='purple',foreground='white')
        lbl.place(x=500,y=20)
        time()

        


        self.conn = sqlite3.connect('todo.db')
        print("Connection.")
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS product (Productname varchar(50) PRIMARY KEY,quantity varchar(30),rate varchar(100),value varchar(10))')
        self.conn.commit()


        self.GLabel_70=Label(self.window,highlightthickness=2)
        #self.GLabel_70["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_70["font"] = ft
        self.GLabel_70["justify"] = "center"
        self.GLabel_70["text"] = "Name (alias)"
        self.GLabel_70.place(x=20,y=20,width=70,height=25)

        self.GLineEdit_555=Entry(self.window,highlightthickness=1)
        #self.GLineEdit_555["anchor"] = "s"
        self.GLineEdit_555["borderwidth"] = "1px"
        self.GLineEdit_555["disabledforeground"] = "#8b878f"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_555["font"] = ft
        self.GLineEdit_555["fg"] = "YELLOW"
        self.GLineEdit_555["justify"] = "center"
        self.GLineEdit_555.place(x=130,y=20,width=230,height=30)

        self.GLabel_356=Label(self.window,highlightthickness=2)
        #self.GLabel_356["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_356["font"] = ft
        self.GLabel_356["justify"] = "center"
        self.GLabel_356["text"] = "Category "
        self.GLabel_356.place(x=20,y=240,width=70,height=25)

        self.GLabel_319=Label(self.window,highlightthickness=2)
        ft = tkFont.Font(family='Times',size=12)
        self.GLabel_319["font"] = ft
        self.GLabel_319["justify"] = "center"
        self.GLabel_319["text"] = "Products Rate"
        self.GLabel_319["relief"] = "ridge"
        self.GLabel_319.place(x=330,y=150,width=106,height=30)

        self.GLabel_639=Label(self.window,highlightthickness=2)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_639["font"] = ft
        self.GLabel_639["justify"] = "center"
        self.GLabel_639["text"] = "Quantity"
        self.GLabel_639.place(x=330,y=200,width=70,height=25)

        self.GLabel_758=Label(self.window,border=1,highlightthickness=2)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_758["font"] = ft
        self.GLabel_758["justify"] = "center"
        self.GLabel_758["text"] = "Rate"
        self.GLabel_758.place(x=330,y=250,width=70,height=25)

        self.GLabel_77=Label(self.window,highlightthickness=2)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_77["font"] = ft
        self.GLabel_77["justify"] = "center"
        self.GLabel_77["text"] = "Per."
        self.GLabel_77.place(x=330,y=320,width=70,height=25)

        self.GLabel_237=Label(self.window,highlightthickness=2)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_237["font"] = ft
        self.GLabel_237["justify"] = "center"
        self.GLabel_237["text"] = "Value"
        self.GLabel_237.place(x=330,y=410,width=70,height=25)

        self.GLineEdit_78=Entry(self.window,highlightthickness=2)
        self.GLineEdit_78["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_78["font"] = ft
        self.GLineEdit_78["fg"] = "yellow"
        self.GLineEdit_78["justify"] = "center"
        self.GLineEdit_78["text"] = "Quantity"
        self.GLineEdit_78.place(x=450,y=200,height=30)

        
        self.GLineEdit_732=Entry(self.window,highlightthickness=2)
        self.GLineEdit_732["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_732["font"] = ft
        self.GLineEdit_732["fg"] = "yellow"
        self.GLineEdit_732["justify"] = "center"
        self.GLineEdit_732["text"] = "Rate"
        self.GLineEdit_732.place(x=450,y=250,height=30)

        
        self.GLineEdit_22=Entry(self.window,highlightthickness=2)
        self.GLineEdit_22["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_22["font"] = ft
        self.GLineEdit_22["fg"] = "#333333"
        self.GLineEdit_22["justify"] = "center"
        self.GLineEdit_22["text"] = "Value"
        self.GLineEdit_22.place(x=460,y=410,width=114,height=30)

        

        GButton_235=tk.Button(self.window,highlightthickness=2)
        GButton_235["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_235["font"] = ft
        GButton_235["fg"] = "#000000"
        GButton_235["justify"] = "center"
        GButton_235["text"] = "Quit"
        GButton_235.place(x=40,y=550,width=70,height=25)
        GButton_235["command"] = self.GButton_235_command

        GButton_125=tk.Button(self.window,highlightthickness=2)
        GButton_125["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_125["font"] = ft
        GButton_125["fg"] = "#000000"
        GButton_125["justify"] = "center"
        GButton_125["text"] = "Accept"
        GButton_125.place(x=500,y=550,width=70,height=25)
        GButton_125["command"] = self.GButton_125_command
        self.window.bind('<Control-a>',self.GButton_125_command)
        self.window.bind('<Escape>',self.GButton_235_command)

        self.lista=Listbox(self.window,width=30,highlightthickness=1,font=('Andalus', 12, 'bold'),selectmode=BROWSE,bg='light blue',selectbackground='#89a592',selectforeground='#ff1493', selectborderwidth=3, activestyle=NONE)
        self.lista.place(x=720,y=180,width=300,height=400)
        self.scroll = Scrollbar(self.window, orient=VERTICAL)
        self.scroll2 = Scrollbar(self.window, orient=HORIZONTAL)
        self.lista.config(yscrollcommand=self.scroll.set, xscrollcommand=self.scroll2.set)
        self.scroll.config(command=self.lista.yview)
        self.scroll2.config(command=self.lista.xview)
        self.ver()
        self.window.mainloop()
        #root.Listbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


    def function(self, var):
        self.entrada.delete(0, 'end')
        self.entrada.insert('end', self.lista.get(self.lista.curselection()))
        messagebox.showinfo(Productname="Info", message=self.lista.get(self.lista.curselection()))


    def ver(self):
        self.c.execute("SELECT Productname FROM product")
        rows = self.c.fetchall()
        for row in rows:
            self.lista.insert('end', row)
        self.conn.commit()

    def GButton_235_command(self,event=""):
        quit()


    def GButton_125_command(self,event=""):
        Productname=self.GLineEdit_555.get()
        quantity=self.GLineEdit_78.get()
        rate=self.GLineEdit_732.get()
        value=self.GLineEdit_22.get()
        print(Productname)
        print(quantity)
        print(rate)
        print(value)

        if self.GLineEdit_555.get() == "" or self.GLineEdit_555.get().isspace() or self.GLineEdit_22.get()==""or self.GLineEdit_732.get()=="":
            messagebox.showinfo(title="UNIT", message="Please Enter Products&Details ?")
            
        else:

        
            self.conn = sqlite3.connect('todo.db')
            #conn = create_connection()
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM product WHERE Productname='"+Productname+"'")
            record = self.cur.fetchone()
            if record is None:
                self.cur.execute("INSERT INTO product (Productname,quantity,rate,value) VALUES ( '"+Productname+"', '"+quantity+"','"+rate+"','"+value+"')")
                print("customer null: ")
                self.conn.commit()
                messagebox.showinfo("Product","'"+Productname+"' Added To DataBase")
            else:
                print("customer not null: ")
                messagebox.showerror("Error","'"+Productname+"' Already To Exist")
            return record  
    

        
        
        self.conn.commit()

if __name__ == "__main__":
    app = App()
