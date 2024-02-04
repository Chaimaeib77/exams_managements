from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms
import managexam as me
import manageprof as mp

class managemntprf:
  def __init__(self,mainfram):
    self.mainfram=mainfram
    self.mangmen=Frame(self.mainfram,pady=10,padx=10)
    self.mangmen.grid(row=0,column=0,sticky="senw")
    self.imgmn=Image.open('code/image/prof_manage.png')
    self.imgmn.thumbnail((250,250))
    self.new_imagmn=ImageTk.PhotoImage(self.imgmn)
    self.mnimag=Label(self.mangmen,image=self.new_imagmn,pady=10,padx=10)
    self.mnimag.pack()
    self.mnbtn=Button(self.mangmen,command=self.openmanagewindow,text="manage surveillance",font=("Times New Roman",15),bg="#446CB3",fg="white",pady=10,padx=10)
    self.mnbtn.pack()

  def openmanagewindow(self):
    manage=managmentprfwin()


class managmentprfwin:
    def __init__(self):
      self.master=Toplevel()
      self.master.title('managment')
      self.width=self.master.winfo_screenwidth()
      self.height=self.master.winfo_screenheight()
      self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
      self.master.state('zoomed')
      self.frameleft=Frame(self.master,width=450)
      self.frameleft.pack(side="left",fill=Y)
      ##################addings########################### 
      self.CIN = Label(self.frameleft, text='CIN:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.CIN.place(x=10,y=20,width=100,height=40)
      self.firstName=Label(self.frameleft,text='prenom:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.firstName.place(x=10,y=70,width=100,height=40)
      self.lastName = Label(self.frameleft, text='nom:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.lastName.place(x=10,y=120,width=100,height=40)
      self.filiere = Label(self.frameleft, text='filiere:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.filiere.place(x=10,y=170,width=100,height=40)
      self.module = Label(self.frameleft, text='module:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.module.place(x=10,y=220,width=100,height=40)
      self.local = Label(self.frameleft, text='local:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.local.place(x=10,y=270,width=100,height=40)
      self.date = Label(self.frameleft, text='date:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.date.place(x=10,y=329,width=100,height=40)
      self.time = Label(self.frameleft, text='heur:',fg='#4F4F4F',font=('tahoma',12,'bold'))
      self.time.place(x=10,y=370,width=100,height=40)

      self.cin = StringVar()
      self.name=StringVar()
      self.last = StringVar()
      self.filiere = StringVar()
      self.module = StringVar()
      self.local = StringVar()
      self.date = StringVar()
      self.time = StringVar()
      

      self.CINentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.cin)  
      self.CINentry.place(x=120,y=20,width=200,height=40)
      self.firstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.name)
      self.firstNameEntry.place(x=120,y=70,width=200,height=40)
      self.lastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.last)
      self.lastNameEntry.place(x=120,y=120,width=200,height=40)
      self.fillliereEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.filiere)
      self.fillliereEntry.place(x=120,y=170,width=200,height=40)
      self.moduleEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.module)
      self.moduleEntry.place(x=120,y=220,width=200,height=40)
      self.localEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.local)
      self.localEntry.place(x=120,y=270,width=200,height=40)
      self.dateEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.date)
      self.dateEntry.place(x=120,y=320,width=200,height=40)
      self.timeEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.time)
      self.timeEntry.place(x=120,y=370,width=200,height=40)
      

      self.buttonAdd=Button(self.frameleft,text="ADD",command=self.ADD, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonAdd.place(x=20,y=470,width=60,height=60)
      self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.UPDATE, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonUpdate.place(x=100, y=470,width=60,height=60)
      self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.DELETE, bg="#446CB3",font=('tahoma',10,'bold'))
      self.buttonDelete.place(x=180, y=470,width=60,height=60)
      self.buttonReset = Button(self.frameleft, text="RESET", command=self.RESET, bg="#446CB3",font=('tahoma', 10, 'bold'))
      self.buttonReset.place(x=260, y=470, width=60, height=60)

      

      ####################right fram##########################
      self.framright = Frame(self.master, width=self.width-350)
      self.framright.pack(side="right", fill=BOTH)
      ####################the viwe fram##########################
      self.datafram=Frame(self.framright)
      self.datafram.pack(fill=BOTH)

      self.table = ttk.Treeview(self.datafram,height=300,columns=("ID", "CIN", "nom_prof", "pre_nom", "filiere", "module", "local", "date", "time"), show='headings')
      self.table.pack(fill=BOTH,pady=50)

      self.table.heading("ID", text="ID")
      self.table.heading("CIN", text="CIN")
      self.table.heading("nom_prof", text="nom_prof")
      self.table.heading("pre_nom", text="pre_nom")
      self.table.heading("filiere", text="filiere")
      self.table.heading("module", text="module")
      self.table.heading("local", text="local")
      self.table.heading("date", text="date")
      self.table.heading("time", text="time")

      self.table.column("ID",width=2,anchor=W)
      self.table.column("CIN",anchor=W)
      self.table.column("nom_prof", anchor=W)
      self.table.column("pre_nom",anchor=W)
      self.table.column("filiere",anchor=W)
      self.table.column("module",anchor=W)
      self.table.column("local", anchor=W)
      self.table.column("date", anchor=W)
      self.table.column("time", anchor=W)

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
      sql="SELECT * FROM prof "
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
      self.cin.set(val[1])
      self.name.set(val[2])
      self.last.set(val[3])
      self.filiere.set(val[4])
      self.module.set(val[5])
      self.local.set(val[6])
      self.date.set(val[7])
      self.time.set(val[8])


    def ADD(self):
      mydb = mc.connect(
          host="localhost",
          user="root",
          password="",
          database="uni"
      )
      v = 0
      mycursor = mydb.cursor()

      sql_prof = "SELECT * FROM prof WHERE CIN = %s"
      mycursor.execute(sql_prof, (self.cin.get(),))
      result_prof = mycursor.fetchall()

      sql_exam = "SELECT * FROM examan WHERE filliere = %s AND module = %s AND date = %s AND time = %s AND local = %s"
      val_exam = (self.filiere.get(), self.module.get(), self.date.get(), self.time.get(), self.local.get())
      mycursor.execute(sql_exam, val_exam)
      result_exam = mycursor.fetchall()

      if result_exam:
          for res_prof in result_prof:
              if self.local.get().strip() == res_prof[6].strip() and self.date.get().strip() == res_prof[7].strip() and self.time.get().strip() == res_prof[8].strip():
                  ms.showinfo("error", "the is occupied on this date", parent=self.master)
                  v = 1
                  break
              elif self.date.get().strip() == res_prof[7].strip() and self.time.get().strip() == res_prof[8].strip():
                  ms.showinfo("error", "the prof is occupied on this date", parent=self.master)
                  v = 1
                  break
      else:
          v = 2

      if v == 0:
          sql_insert_prof = "INSERT INTO prof (CIN, nom_prof, pre_nom, filiere, module, local, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
          val_insert_prof = (self.cin.get(), self.name.get(), self.last.get(), self.filiere.get(), self.module.get(), self.local.get(), self.date.get(), self.time.get())
          mycursor.execute(sql_insert_prof, val_insert_prof)
          mydb.commit()

          self.cin.set("")
          self.name.set("")
          self.last.set("")
          self.filiere.set("")
          self.module.set("")
          self.local.set("")
          self.date.set("")
          self.time.set("")
          ms.showinfo("data inserted", "the data is inserted successfully", parent=self.master)
          mydb.close()
          self.READ()
      elif v == 2:
          ms.showinfo("error", "the exam plan doesn't exist", parent=self.master)




    def UPDATE(self):
        mydb = mc.connect(
          host="localhost",
          user="root",
          password="",
          database="uni"
      )
        v = 0
        mycursor = mydb.cursor()

        sql_prof = "SELECT * FROM prof WHERE CIN = %s"
        mycursor.execute(sql_prof, (self.cin.get(),))
        result_prof = mycursor.fetchall()

        sql_exam = "SELECT * FROM examan WHERE filliere = %s AND module = %s AND date = %s AND time = %s AND local = %s"
        val_exam = (self.filiere.get(), self.module.get(), self.date.get(), self.time.get(), self.local.get())
        mycursor.execute(sql_exam, val_exam)
        result_exam = mycursor.fetchall()

        if result_exam:
            for res_prof in result_prof:
                if self.local.get().strip() == res_prof[6].strip() and self.date.get().strip() == res_prof[7].strip() and self.time.get().strip() == res_prof[8].strip():
                    ms.showinfo("error", "the is occupied on this date", parent=self.master)
                    v = 1
                    break
                elif self.date.get().strip() == res_prof[7].strip() and self.time.get().strip() == res_prof[8].strip():
                    ms.showinfo("error", "the prof is occupied on this date", parent=self.master)
                    v = 1
                    break
        else:
            v = 2
        if v == 0:
            sql = "UPDATE prof SET CIN=%s,nom_prof=%s,pre_nom=%s,filiere=%s,module=%s,local=%s,date=%s,time=%s WHERE id=%s"
            val = (self.cin.get(), self.name.get(), self.last.get(), self.filiere.get(),self.module.get(), self.local.get(), self.date.get(), self.time.get(), self.iid)
            mycursor.execute(sql, val)
            mydb.commit()
            self.cin.set("")
            self.name.set("")  
            self.last.set("")
            self.filiere.set("")
            self.module.set("")
            self.local.set("")
            self.date.set("")
            self.time.set("")
            ms.showinfo("data inserted", "the data is inserted successfully",parent=self.master)
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
      sql = ("DELETE FROM prof WHERE id="+self.iid)  
      mycursor.execute(sql)
      mydb.commit()
      mydb.close()
      self.READ()
      self.RESET()


    def RESET(self):
      self.cin.set("")
      self.name.set("")
      self.last.set("")
      self.filiere.set("")
      self.module.set("")
      self.local.set("")
      self.date.set("")
      self.time.set("")

