from tkinter import *
from PIL import Image,ImageTk 
import examans as e
import mangments as m
import professeur as s


class university:
  def __init__(self,mas):
    ####################main window##########################
    self.master=Toplevel()
    self.master.title('school management systeme')
    self.width=self.master.winfo_screenwidth()
    self.height=self.master.winfo_screenheight()
    self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
    self.master.state('zoomed')
    ####################top fram##########################
    self.topfram=Frame(self.master,bg="#446CB3",height=100)
    self.topfram.pack(fill=X)
    self.sms=Label(self.topfram,text='exams managment system',bg="#446CB3",fg='white',font=("Times New Roman",30),pady=30)
    self.sms.pack()
    ##################main fraim##########################
    self.mainfram=Frame(self.master,height=100)
    self.mainfram.pack(fill=X)
    std=s.prof(self.mainfram)
    std=e.cc(self.mainfram)
    std=m.managemnt(self.mainfram)

    self.mainfram.grid_columnconfigure(0,weight=1)
    self.mainfram.grid_columnconfigure(1,weight=1)
    self.mainfram.grid_columnconfigure(2,weight=1)
