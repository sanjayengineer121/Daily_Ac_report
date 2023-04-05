from tkinter import messagebox
from tkinter import *
import sqlite3
import tkinter
from datetime import date

class ToDoList:
    """To Do List in python with Tkinter."""

    def __init__(self):
        self.window = Tk()
        tasks=[]
        #self.placeholder = placeholder
        self.window.title('TODO')
        self.window.iconbitmap('img/notes (2).ico')
        self.window.resizable(False, False)
        self.conn = sqlite3.connect('todo.db')
        print("Connection.")
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS todo (title varchar(25) PRIMARY KEY,Desc varchar(100),DATE varchar(15),status varchar(2))')
        self.conn.commit()
        self.window.config(pady=20, padx=20, bg='#378060')
        self.lbl = Label(text="Introduce TODO List:", font=('Lucida Console', 12), bg='#378060')
        self.lbl.grid(row=0, column=0)
        self.entrada = Entry(fg='#0c573f', font=('Helvetica', 12))
        self.entrada.grid(row=1, column=0, pady=5)
        self.entrada.focus()
        self.entrada.insert(0, 'Title')
        self.entrada.grid(row=1, column=0, pady=5)

        self.entrada1 = Entry(fg='#0c573f', font=('Helvetica', 12))
        self.entrada1.grid(row=2, column=0, pady=5)
        self.entrada1.focus()
        self.entrada1.insert(0, 'Desc.')
        self.entrada1.grid(row=2, column=0, pady=5)
        

        def click(*args):
            self.entrada.delete(0, 'end')
            self.entrada1.delete(0, 'end')
  
# call function when we leave entry box
        def leave(*args):
            self.entrada.delete(0, 'end')
            self.entrada.insert(0, 'Title')
            self.entrada1.delete(0, 'end')
            self.entrada1.insert(0, 'Desc.')
            self.window.focus()
            
        self.entrada.bind("<Button-1>", click)
        #self.entrada.bind("<Leave>", leave)

        self.entrada1.bind("<Button-2>", click)
        #self.entrada1.bind("<Leave>", leave)

        
        self.add_task = Button(text="Add Todo Task", highlightthickness=0, command=self.add, font=('Lucida Console', 12),
                               bg='#51b031')
        self.add_task.grid(row=3, column=0, sticky=EW, pady=5, padx=20)
        self.delete_task = Button(text="Delete Task", highlightthickness=0, command=self.delete, font=('Lucida Console', 12),
                                  bg='#51b031')
        self.delete_task.grid(row=4, column=0, sticky=EW, pady=5, padx=20)
        self.fulldelete_task = Button(text="Delete All Task", highlightthickness=0, command=self.delete_all,
                                      font=('Lucida Console', 12), bg='#51b031')
        self.fulldelete_task.grid(row=5, column=0, sticky=EW, pady=5, padx=20)
        self.exit_task = Button(text="CLOSE", highlightthickness=0, command=self.quit1,
                                font=('Lucida Console', 12), bg='#51b031')
        self.exit_task.grid(row=6, column=0, sticky=EW, pady=5, padx=20)
        self.window.bind('<Escape>',self.quit1)

        
        #self.window.bind('<Escape>',self.GButton_235_command)
        self.lista = Listbox(width=50, height=10, highlightthickness=0, font=('Andalus', 12, 'bold'),
                             selectmode=SINGLE, bg='#044f19', fg='#65eb8a', selectbackground='#aed6b9',
                             selectforeground='#68786d', selectborderwidth=3, activestyle=NONE)
        self.lista.grid(row=0, column=1, rowspan=7)
        self.lista.bind('<Double-Button>', self.function)
        self.scroll = Scrollbar(self.window, orient=VERTICAL)
        self.scroll2 = Scrollbar(self.window, orient=HORIZONTAL)
        self.scroll2.grid(row=7, column=1, sticky=EW)
        self.scroll.grid(row=0, column=3, sticky=NS, rowspan=7)
        self.lista.config(yscrollcommand=self.scroll.set, xscrollcommand=self.scroll2.set)
        self.scroll.config(command=self.lista.yview)
        self.scroll2.config(command=self.lista.xview)
        self.ver()

        self.window.mainloop()
        self.conn.close()
        print("Connection closed")

    def function(self, var):
        self.entrada.delete(0, 'end')
        self.entrada.insert('end', self.lista.get(self.lista.curselection()))
        messagebox.showinfo(title="Info", message=self.lista.get(self.lista.curselection()))

    
        

    def ver(self):
        self.c.execute("SELECT title FROM todo")
        rows = self.c.fetchall()
        for row in rows:
            self.lista.insert('end', row)
        self.conn.commit()
    
    
    def quit1(self,event=""):
            quit()
    

    def add(self):
        if self.entrada.get() == "" or self.entrada.get().isspace() or self.entrada.get().isnumeric():
            messagebox.showinfo(title="Info", message="Please Enter TODO?")
        else:
            STAT="0"
            self.c.execute("INSERT INTO todo (title,Desc,DATE,status) VALUES ( '"+self.entrada.get()+"', '"+self.entrada1.get()+"','"+str(date.today())+"','"+STAT+"')")
            self.lista.insert('end', self.entrada.get())
            self.entrada.delete(0, 'end')
        self.conn.commit()
        
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
        

    def delete_all(self):
        mb = messagebox.askyesno(title="After Delete You won't Recover",message="Do You Want To Delete All List")

        if mb:
            self.c.execute(f'DELETE FROM todo')
            self.lista.delete(0, 'end')
        self.conn.commit()

        self.lista = tkinter.Listbox(self.window)
        self.lista.grid(row=0, column=1, rowspan=7)


if __name__ == "__main__":
    todo = ToDoList()