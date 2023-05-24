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
    def Login_System(self):
        user = (self.Username.get())
        pas= (self.Password.get())

        if (user == str(1234)) and (pas == str(2345)):
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid login details")
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Cofirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return
            
        
        #===============================================================================

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
        
class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Patients Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        #==============================================================================

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()

        Membership = StringVar()
        Membership.set("0")

        # Functions Declared

        def iExit():
            iExit = tkinter.messagebox.askyesno("Patients Registration System", "Cofirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("0")

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMembership.config(state=DISABLED)


        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Patients Registration System", "Confirm if You Want to add a New Record")

            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return

        def Ref_No():

            x=random.randint(10903,600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t" + Ref.get()+ "\t\t" + Firstname.get() + "\t\t"
                                + Surname.get()+ "\t\t" + Address.get()+ "\t\t" + DateofOrder.get()+ "\t\t"
                                + Telephone.get()+ "\t\t" + Membership.get()+ "\n")

        def Membership_Fees():

            if(var4.get() == 1):
                self.txtMembership.configure(state=NORMAL)
                Item1 = float(50)
                Membership.set("" + str(Item1))

            elif(var4.get() == 0):
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")
                
       
