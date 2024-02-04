from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms
import managexam as me
import manageprof as mp



class managemnt:
  def __init__(self,mainfram):
    self.mainfram=mainfram
    self.mangmen=Frame(self.mainfram,pady=10,padx=10)
    self.mangmen.grid(row=0,column=1,sticky="senw")
    self.imgmn=Image.open('code/image/manager.png')
    self.imgmn.thumbnail((250,250))
    self.new_imagmn=ImageTk.PhotoImage(self.imgmn)
    self.mnimag=Label(self.mangmen,image=self.new_imagmn,pady=10,padx=10)
    self.mnimag.pack()
    self.mnbtn=Button(self.mangmen,command=self.openmanagewindow,text="managments",font=("Times New Roman",15),bg="#446CB3",fg="white",pady=10,padx=10)
    self.mnbtn.pack()

  def openmanagewindow(self):
    manage=managmentwin()


class managmentwin:
    def __init__(self):
      self.master=Toplevel()
      self.master.title('managment')
      self.width=self.master.winfo_screenwidth()
      self.height=self.master.winfo_screenheight()
      self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
      self.master.state('zoomed')
      self.topfram=Frame(self.master,bg="#446CB3",height=100)
      self.topfram.pack(fill=X)
      self.sms=Label(self.topfram,text='exams managment system',bg="#446CB3",fg='white',font=("Times New Roman",30),pady=30)
      self.sms.pack()
      ##################main fraim##########################
      self.mainfram=Frame(self.master,height=100)
      self.mainfram.pack(fill=X)
      self.main2fram=Frame(self.master,height=100)
      self.main2fram.pack(fill=X)
      std=mp.managemntprf(self.mainfram)
      std=me.managemntexam(self.mainfram)


      self.mainfram.grid_columnconfigure(0,weight=1)
      self.mainfram.grid_columnconfigure(1,weight=1)


