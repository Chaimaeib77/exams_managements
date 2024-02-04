from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms



class cc:
  def __init__(self,mainfram):
    self.mainfram=mainfram
    self.exam=Frame(self.mainfram,pady=10,padx=10)
    self.exam.grid(row=0,column=2,sticky="senw")
    self.imgex=Image.open('code/image/schedule.png')
    self.imgex.thumbnail((250,250))
    self.new_imagex=ImageTk.PhotoImage(self.imgex)
    self.eximag=Label(self.exam,image=self.new_imagex,pady=10,padx=10)
    self.eximag.pack()
    self.exbtn=Button(self.exam,text="exams space ",command=self.openexamwindow,font=("Times New Roman",15),bg="#446CB3",fg="white",pady=10,padx=10)
    self.exbtn.pack()


  def openexamwindow(self):
    exwin=examanwindow()

class examanwindow:
    def __init__(self):
        self.master=Toplevel()
        self.master.title('exams')
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state('zoomed')
        self.frame_left = Frame(self.master, width=350)
        self.frame_left.pack(side="left", fill=Y)  # fill y | height

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

        self.data_frame = Frame(self.frame_right, bg="red")
        self.data_frame.pack(fill=BOTH,padx=20,pady=20)

        self.table = ttk.Treeview(self.data_frame, height=300,columns=("ID","filliere",	"module",	"date",	"time",	"local"	), show='headings')
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("filliere", text="filliere")
        self.table.heading("module", text="module")
        self.table.heading("date", text="date")
        self.table.heading("time", text="time")
        self.table.heading("local", text="local")

        self.table.column("ID", width=2 ,anchor=W)
        self.table.column("filliere", anchor=W)
        self.table.column("module", anchor=W)
        self.table.column("date", anchor=W)
        self.table.column("time", anchor=W)
        self.table.column("local", anchor=W)
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
        sql = "SELECT * FROM examan WHERE filliere=%s"
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
        sql = "SELECT * FROM examan WHERE filliere=%s"
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
      sql = "SELECT * FROM examan WHERE filliere=%s"
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
      sql = "SELECT * FROM examan WHERE filliere=%s"
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
      sql = "SELECT * FROM examan WHERE filliere=%s"
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
      sql = "SELECT * FROM examan WHERE filliere=%s"
      mycursor.execute(sql, (val,))
      result = mycursor.fetchall()
      self.table.delete(*self.table.get_children())
      if result:
          for res in result:
              self.table.insert('', 'end', values=res)
      else:
          ms.showinfo("No Data", "No data found for filiere=IDA",parent=self.master)
      mydb.close()



