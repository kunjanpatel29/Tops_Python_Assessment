from tkinter import *
import tkinter.messagebox
import random
from tkinter import ttk
import time
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1050x650+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame,text = 'Pharmacy Management System',font=('arial',50,'bold'),bd=20,)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1 = Frame(self.frame, width=900,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=900,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame, width=900,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3, column=0,pady=2)

        #===============================================================================
        self.lblUsername = Label(self.Loginframe1,text = 'Username',font=('arial',30,'bold'),bd=20,)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername = Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword = Label(self.Loginframe1,text = 'Password',font=('arial',30,'bold'),bd=20,)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,
                                 textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1,padx=85)
        #===============================================================================

        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),
                                      command=self.Login_System)
        self.btnLogin.grid(row = 0, column = 0)
    
        self.btnReset = Button(self.Loginframe2,text="Reset",width=17,font=('arial',20,'bold'),
                                  command=self.Reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnExit = Button(self.Loginframe2,text="Exit",width=17,font=('arial',20,'bold'),
                                  command=self.iExit)
        self.btnExit.grid(row = 0, column = 2)

        #===============================================================================

        self.btnRegistration = Button(self.Loginframe3, text="Patients Registration System",
                                      state=DISABLED, command=self.Registration_window,font=('arial',20,'bold'))
        self.btnRegistration.grid(row = 0, column = 0)

        self.btnHospital = Button(self.Loginframe3,text="Hospital Management System",
                                  state=DISABLED,command=self.Hospital_window,font=('arial',20,'bold'))
        self.btnHospital.grid(row = 0, column = 1)
        #===============================================================================
    
