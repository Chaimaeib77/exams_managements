from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import mysql.connector as mc
import tkinter.messagebox as ms
import main as m


class LoginPage:
    def __init__(self, window):
        self.user = StringVar()
        self.password = StringVar()
        self.window = window
        self.width=self.window.winfo_screenwidth()
        self.height=self.window.winfo_screenheight()
        self.window.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.window.state('zoomed')
        self.window.title('Login Page')
        ##########frame top###############
        self.frametop = Frame(self.window, bg='#446CB3',height=100)
        self.frametop.pack(fill=X)
        logo_path = "code\\images\\fst.png" 
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((200, 100))
        logo_photo = ImageTk.PhotoImage(logo_img)

        self.logo_label = Label(self.frametop, image=logo_photo, bg='#446CB3')
        self.logo_label.image = logo_photo
        self.logo_label.pack(side='left', pady=10, padx=20) 
        self.sms=Label(self.frametop,text='exams managment system',bg="#446CB3",fg='white',font=("Times New Roman",30),pady=30)
        self.sms.pack(side='top', pady=10, anchor='center')
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('code\\images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#FFFFFF', width=900, height=600)
        self.lgn_frame.place(x=200, y=130)        
        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('code\\images\\perfect.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.side_image_label.image = photo
        self.side_image_label.place(x=2, y=100)
        

        # ========================================================================
        # ============ Sign In =============================================
        # ========================================================================
        self.sign_in_image = Image.open('code\\images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#FFFFFF", fg="black",font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username/Email", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69',textvariable=self.user)
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open('code\\images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('code\\images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label,command=self.login, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"),)
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69',textvariable=self.password)
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        self.password_icon = Image.open('code\\images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='code\\images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='code\\images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def login(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="uni"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM login"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        login_successful = False

        for res in result:
            if self.user.get().strip() == res[0] or self.user.get().strip()==res[1]:
                if self.password.get().strip() == res[2]:
                    login_successful = True
                    break
            elif self.user.get() == "" or self.password.get() == "":
                ms.showinfo("error", "Fill all the required spaces", parent=self.window)
                break

        if login_successful:
            main=m.university(self.window)

        else:
            ms.showinfo("error", "the user name or the password are not correct", parent=self.window)






window = Tk()
LoginPage(window)
window.mainloop()