from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms
import managexam as me
import manageprof as mp

class managemntexam:
  def __init__(self,mainfram):
    self.mainfram=mainfram
    self.mangmen=Frame(self.mainfram,pady=10,padx=10)
    self.mangmen.grid(row=0,column=1,sticky="senw")
    self.imgmn=Image.open('code/image/manage_exam.png')
    self.imgmn.thumbnail((250,250))
    self.new_imagmn=ImageTk.PhotoImage(self.imgmn)
    self.mnimag=Label(self.mangmen,image=self.new_imagmn,pady=10,padx=10)
    self.mnimag.pack()
    self.mnbtn=Button(self.mangmen,command=self.openmanagewindow,text="manage exams",font=("Times New Roman",15),bg="#446CB3",fg="white",pady=10,padx=10)
    self.mnbtn.pack()

  def openmanagewindow(self):
    manage=managmentexamwin()


class managmentexamwin:
    def __init__(self):
      self.master=Toplevel()
      self.master.title('managment')
      self.width=self.master.winfo_screenwidth()
      self.height=self.master.winfo_screenheight()
      self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
      self.master.state('zoomed')
      self.frameleft=Frame(self.master,width=450)
      self.frameleft.pack(side="left",fill=Y)#fill y | height
      ##################addings########################### 
      self.filiere = Label(self.frameleft, text='filiere:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.filiere.place(x=10,y=20,width=100,height=40)
      self.module = Label(self.frameleft, text='module:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.module.place(x=10,y=70,width=100,height=40)
      self.date = Label(self.frameleft, text='date:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.date.place(x=10,y=120,width=100,height=40)
      self.time = Label(self.frameleft, text='time:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.time.place(x=10,y=170,width=100,height=40)
      self.local = Label(self.frameleft, text='local:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.local.place(x=10,y=220,width=100,height=40)

      self.filiere = StringVar()
      self.module = StringVar()
      self.local = StringVar()
      self.date = StringVar()
      self.time = StringVar()
      

      
      self.fillliereEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.filiere)
      self.fillliereEntry.place(x=120,y=20,width=200,height=40)
      self.moduleEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.module)
      self.moduleEntry.place(x=120,y=70,width=200,height=40)
      self.dateEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.date)
      self.dateEntry.place(x=120,y=120,width=200,height=40)
      self.timeEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.time)
      self.timeEntry.place(x=120,y=170,width=200,height=40)
      self.localEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.local)
      self.localEntry.place(x=120,y=220,width=200,height=40)
      

      self.buttonAdd=Button(self.frameleft,text="ADD",command=self.ADD, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonAdd.place(x=20,y=370,width=60,height=60)
      self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.UPDATE, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonUpdate.place(x=100, y=370,width=60,height=60)
      self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.DELETE, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonDelete.place(x=180, y=370,width=60,height=60)
      self.buttonReset = Button(self.frameleft, text="RESET", command=self.RESET, bg="#446CB3",font=('tahoma', 10, 'bold'))
      self.buttonReset.place(x=260, y=370, width=60, height=60)
      ####################right fram##########################
      self.framright = Frame(self.master, width=self.width-350)
      self.framright.pack(side="right", fill=BOTH)
      ####################the viwe fram##########################
      self.datafram=Frame(self.framright)
      self.datafram.pack(fill=BOTH)

      self.table = ttk.Treeview(self.datafram,height=300,columns=("ID", "filiere", "module",  "date", "time","local"), show='headings')
      self.table.pack(fill=BOTH,pady=50)

      self.table.heading("ID", text="ID")
      self.table.heading("filiere", text="filiere")
      self.table.heading("module", text="module")      
      self.table.heading("date", text="date")
      self.table.heading("time", text="time")      
      self.table.heading("local", text="local")

      self.table.column("ID",width=2 ,anchor=W)
      self.table.column("filiere",anchor=W)
      self.table.column("module" ,anchor=W)
      self.table.column("date" , anchor=W)
      self.table.column("time",anchor=W)
      self.table.column("local" ,anchor=W)
      self.READ()
      self.table.bind("<ButtonRelease-1>", self.show)

    def READ(self):
      mydb=mc.connect(
        host="localhost",
        user="root",
        password="",
        database="uni"
      )
      mycursor=mydb.cursor()
      sql="SELECT * FROM examan "
      mycursor.execute(sql)
      result=mycursor.fetchall()
      self.table.delete(*self.table.get_children())
      for res in result:
        self.table.insert('','end',iid=res[0],values=res)
      mydb.commit() 
      mydb.close()

    def show(self,ev):
      self.iid=self.table.focus()
      alldata=self.table.item(self.iid)
      val=alldata["values"]
      self.filiere.set(val[1])
      self.module.set(val[2])
      self.date.set(val[3])
      self.time.set(val[4])
      self.local.set(val[5])

    def ADD(self):
      mydb=mc.connect(
      host="localhost",
      user="root",
      password="",
      database="uni"
    )
      mycursor=mydb.cursor()
      v=0
      mycursor=mydb.cursor()
      sql2=("SELECT * from examan")
      mycursor.execute(sql2)
      result=mycursor.fetchall()
      for res in result:
        if self.filiere.get()=="" or self.module.get()=="" or self.local.get()=="" or self.date.get()=="" or self.time.get()=="":
          ms.showinfo("error","insert the data y",parent=self.master)
          v=1
          break
        if self.filiere.get().strip() == res[1].strip() and self.module.get().strip() == res[2].strip() :
          ms.showinfo("error","the exam has already been planed",parent=self.master)
          v=1
          break
        elif self.date.get().strip() == res[3].strip() and self.time.get().strip() == res[4].strip() and self.local.get().strip()== res[5].strip():
          ms.showinfo("error","the local is reserved for this date",parent=self.master)
          v=1
          break
      if v==0 :
        sql="INSERT INTO examan (filliere,module,date,time,local) values(%s,%s,%s,%s,%s)"
        val = ( self.filiere.get(),self.module.get(),self.date.get(),self.time.get(),self.local.get())
        mycursor.execute(sql,val)
        mydb.commit() 
        self.filiere.set("")
        self.module.set("")
        self.local.set("")
        self.date.set("")
        self.time.set("")
        ms.showinfo("data inserted","the data is inserted sucesfuly",parent=self.master)
        mydb.close()
        self.READ()



    def UPDATE(self):
      mydb = mc.connect(
          host="localhost",
          user="root",
          password="",
          database="uni"
      )
      v = 0
      mycursor = mydb.cursor()
      sql2 = ("SELECT * from examan")
      mycursor.execute(sql2)
      result = mycursor.fetchall()
      for res in result:
          if  (self.local.get()=="" or self.date.get()=="" or self.time.get()==""):
            ms.showinfo("error","the exam has already been planed",parent=self.master)
            v=1
            break
          elif (self.date.get().strip() == res[3].strip() and self.time.get().strip() == res[4].strip() and self.local.get().strip()== res[5].strip()):
              ms.showinfo("error", "the data inserted already exist")
              v = 1
              break
      if v == 0:
          sql = "UPDATE examan SET local=%s,date=%s,time=%s WHERE id=%s"
          val = (self.local.get(), self.date.get(), self.time.get(), self.iid)
          mycursor.execute(sql, val)
          mydb.commit()
          self.filiere.set("")
          self.module.set("")
          self.local.set("")
          self.date.set("")
          self.time.set("")
          ms.showinfo("data inserted", "the data is inserted successfully")
          mydb.close()
          self.READ()




    def DELETE(self):
      mydb = mc.connect(
          host="localhost",
          user="root",
          password="",
          database="uni"
      )
      mycursor = mydb.cursor()
      sql = ("DELETE FROM examan WHERE id="+self.iid)  
      mycursor.execute(sql)
      mydb.commit()
      mydb.close()
      self.READ()
      self.RESET()






    def RESET(self):
      self.filiere.set("")
      self.module.set("")
      self.date.set("")
      self.time.set("")
      self.local.set("")


    

