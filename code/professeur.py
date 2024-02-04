from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms

class prof:
    def __init__(self, mainfram):
        self.mainfram = mainfram
        self.prof = Frame(self.mainfram, pady=10, padx=10)
        self.prof.grid(row=0, column=0, sticky="senw")
        self.imgst = Image.open('code/image/prof.png')
        self.imgst.thumbnail((250, 250))
        self.new_imagst = ImageTk.PhotoImage(self.imgst)
        self.stimag = Label(self.prof, image=self.new_imagst, pady=10, padx=10)
        self.stimag.pack()
        self.stbtn = Button(self.prof, command=self.open_prof_window, text="professeurs space", font=("Times New Roman", 15), bg="#446CB3", fg="white", pady=10, padx=10)
        self.stbtn.pack()

    def open_prof_window(self):
        prf_window = ProfWindow()


class ProfWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('professor')
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))
        self.master.state('zoomed')
        self.CIN = StringVar() 
##############################FRAME LEFT####################################################
        self.frame_left = Frame(self.master, width=350)
        self.frame_left.pack(side="left", fill=Y)  
        self.button_MIP = Button(self.frame_left, command=self.MIP, text="MIP", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_MIP.place(x=20, y=10, width=200, height=60)
        self.button_MIPC = Button(self.frame_left, command=self.MIPC, text="MIPC", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_MIPC.place(x=20, y=110, width=200, height=60)
        self.button_BCG = Button(self.frame_left, command=self.BCG, text="BCG", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_BCG.place(x=20, y=210, width=200, height=60)
        self.button_GEGM = Button(self.frame_left, command=self.GEGM, text="GEGM", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_GEGM.place(x=20, y=310, width=200, height=60)
        self.button_ADD = Button(self.frame_left, command=self.ADD, text="ADD", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_ADD.place(x=20, y=410, width=200, height=60)
        self.button_IDA = Button(self.frame_left, command=self.IDA, text="IDA", font=('tahoma', 10, 'bold'), bg="#446CB3")
        self.button_IDA.place(x=20, y=510, width=200, height=60)
###########################frame right#############################
        self.frame_right = Frame(self.master, width=self.width-350)
        self.frame_right.pack(side="right", fill=BOTH)
        self.frame_top_right = Frame(self.frame_right, width=self.width-350)
        self.frame_top_right.pack(fill=X)

        self.searchbar = Entry(self.frame_top_right, font=('tahoma', 12, 'bold'), width=70, textvariable=self.CIN)
        self.searchbar.grid(row=0, column=0, padx=10, pady=10)

        self.searchbarbtn = Button(self.frame_top_right, command=self.search, text="search", font=('tahoma', 12, 'bold'))
        self.searchbarbtn.grid(row=0, column=1, padx=10, pady=10)

        self.data_frame = Frame(self.frame_right, bg="red")
        self.data_frame.pack(fill=BOTH)

        self.table = ttk.Treeview(self.data_frame, height=300,columns=("ID", "CIN", "nom_prof", "pre_nom", "filiere", "module", "local", "date", "time"), show='headings')
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("CIN", text="CIN")
        self.table.heading("nom_prof", text="nom_prof")
        self.table.heading("pre_nom", text="pre_nom")
        self.table.heading("filiere", text="filiere")
        self.table.heading("module", text="module")
        self.table.heading("local", text="local")
        self.table.heading("date", text="date")
        self.table.heading("time", text="time")

        self.table.column("ID",width=2 ,anchor=W)
        self.table.column("CIN",width=2 , anchor=W)
        self.table.column("nom_prof", width=2 ,anchor=W)
        self.table.column("pre_nom", width=2 ,anchor=W)
        self.table.column("filiere", width=2 ,anchor=W)
        self.table.column("module", width=2 ,anchor=W)
        self.table.column("local", width=2 ,anchor=W)
        self.table.column("date", width=2 ,anchor=W)
        self.table.column("time", width=2 ,anchor=W)
###################MIP#########################
    def MIP(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'MIP'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=MIP",parent=self.master)
        mydb.close()
###################MIPC#########################
    def MIPC(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'MIPC'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=MIPC",parent=self.master)
        mydb.close()
###################BCG#########################
    def BCG(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'BCG'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=BCG",parent=self.master)
        mydb.close()
###################GEGM#########################
    def GEGM(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'GEGM'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=GEGM",parent=self.master)
        mydb.close()
###################ADD#########################
    def ADD(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'ADD'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=ADD",parent=self.master)
        mydb.close()
###################IDA#########################
    def IDA(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = 'IDA'
        sql = "SELECT * FROM prof WHERE filiere=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for filiere=IDA",parent=self.master)
        mydb.close()
###################SEARCH#########################
    def search(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        val = (self.CIN.get())
        sql = "SELECT * FROM prof WHERE CIN=%s"
        mycursor.execute(sql, (val,))
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        if result:
            for res in result:
                self.table.insert('', 'end', values=res)
        else:
            ms.showinfo("No Data", "No data found for CIN={}".format(val),parent=self.master)
        mydb.close()



