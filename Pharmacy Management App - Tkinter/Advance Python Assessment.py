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
        #==================================== Frame =======================================        
        Mainframe=Frame(self.frame)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=20, width=1200, padx=35,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'),text="Patient Registration System",padx=4)
        self.lblTitle.grid()

        #==================================== LowerFrames ======================================= 
        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)

        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame,bd=10,width=800,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,
                                   font=('arial',12,'bold'),text= "Customer Name",relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        #==================================================================================
        self.lblReferenceNo=Label(MembersName_F,font=('arial',14,'bold'),text="Reference No",bd=7)
        self.lblReferenceNo.grid(row=0,column=0,sticky=W)
        self.txtReferenceNo=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Ref,
                                  state=DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)

        self.lblFirstname=Label(MembersName_F,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname=Label(MembersName_F,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress=Label(MembersName_F,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Address, insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPostCode=Label(MembersName_F,font=('arial',14,'bold'),text="PostCode",bd=7)
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=PostCode, insertwidth=2)
        self.txtPostCode.grid(row=4,column=1)

        self.lblTelephone=Label(MembersName_F,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=5,column=0,sticky=W)
        self.txtTelephone=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Telephone, insertwidth=2)
        self.txtTelephone.grid(row=5,column=1)

        self.lblDate=Label(MembersName_F,font=('arial',14,'bold'),text="Date",bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)
        self.txtDate=Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=DateofOrder, insertwidth=2)
        self.txtDate.grid(row=6,column=1)

        #===============================Member Information==================================
        self.lblProve_of_ID = Label(MembersName_F,font=('arial',14,'bold'),text="Prove of ID",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)


        self.cboProve_of_ID = ttk.Combobox(MembersName_F,textvariable=var1,state='readonly',font=('arial',14,'bold'),width=19)
        self.cboProve_of_ID['value']=('','Pilot Licence','Driving Licence','Passport','Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)

        self.lblType_of_Member=Label(MembersName_F,font=('arial',14,'bold'), text="Type of Member",bd=7)
        self.lblType_of_Member.grid(row=8,column=0,sticky=W)

        self.cboType_of_Member= ttk.Combobox(MembersName_F, textvariable=var2, state='readonly',font=('arial',14,'bold'),width=19)
        self.cboType_of_Member['value']=('','Full Member','Annual Membership','Pay As You Go','Honorary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)

        self.lblMethod_of_Payment = Label(MembersName_F,font=('arial',14,'bold'), text="Method of Payment",bd=7)
        self.lblMethod_of_Payment.grid(row=9,column=0,sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F,textvariable=var3,state='readonly',font=('arial',14,'bold'),width=19)  

        self.cboMethod_of_Payment['value']=('','Visa Card','Master Card','Debit Card','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1)

        #======================================Check Button=============================
        self.chkMembership = Checkbutton(MembersName_F,text='Patient Fees',variable=var4,onvalue=1,
                                         offvalue=0,font=('arial',16,'bold'),command=Membership_Fees).grid(row=10,column=0,sticky=W)
        self.txtMembership=Entry(MembersName_F,font=('arial',14,'bold'),textvariable=Membership,bd=7,
                                 insertwidth=2,state=DISABLED, justify=RIGHT)

        self.txtMembership.grid(row=10,column=1)

        #======================================Receipt=============================
        self.lblLabel = Label(Receipt_ButtonFrame,font=('arial',10,'bold'),pady=10,
            text="Patient Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\t Patient Paid",bd=7)
        self.lblLabel.grid(row=0,column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame,width=112,height=22,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1,column=0,columnspan=4)

        #======================================Buttons===================================
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text='Receipt',
                               command=Receipt).grid(row=2,column=0)
        self.btnReset=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text='Reset',
                               command=Reset).grid(row=2,column=1)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text='Exit',
                               command=iExit).grid(row=2,column=2)

        #=========================================================================

    def close_windows(self):
        self.master.destroy()

    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno("Patient Registration System","Confrim if you want to exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            return


class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        #===========================================Frame=================================

        cmbNameTablets=StringVar()
        Ref=StringVar()
        Dose=StringVar()
        NumberofTablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientID=StringVar()
        NHSNumber=StringVar()
        PatientName=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()

        #===================================== Function Declaration========================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confirm if You Want to Exit?")
            if iExit > 0:
                self.master.destroy()
                return

        def iPrescription():
            self.txtPrescription.insert(END,'Name of Tablets: \t\t\t\t' + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,'Reference No: \t\t\t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(END,'Dose: \t\t\t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(END,'Number of Tablets: \t\t\t\t' + NumberofTablets.get() + "\n")
            self.txtPrescription.insert(END,'Lot: \t\t\t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(END,'Issued Date: \t\t\t\t' + IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,'Exp. Date: \t\t\t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,'Daily Dose: \t\t\t\t' + DailyDose.get() + "\n")
            self.txtPrescription.insert(END,'Possible Side Effects: \t\t\t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END,'Further Information: \t\t\t\t' + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END,'Storage Advice: \t\t\t\t' + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,'Drivng or Using Machines: \t\t\t\t' + DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(END,'How to Use Medication: \t\t\t\t' + HowtoUseMedication.get() + "\n")
            self.txtPrescription.insert(END,'Patient ID: \t\t\t\t' + PatientID.get() + "\n")
            self.txtPrescription.insert(END,'NHS Number: \t\t\t\t' + NHSNumber.get() + "\n")
            self.txtPrescription.insert(END,'Patient Name: \t\t\t\t' + PatientName.get() + "\n")
            self.txtPrescription.insert(END,'Date of Birth: \t\t\t\t' + DateofBirth.get() + "\n")
            self.txtPrescription.insert(END,'PatientAddress: \t\t\t\t' + PatientAddress.get() + "\n")
            return

        def iPrescriptionData():
            self.txtFrameDetail.insert(END, cmbNameTablets.get()+ "\t\t"+Ref.get()+"\t"+Dose.get()+"\t\t"+
            NumberofTablets.get()+ "\t"+Lot.get()+"\t"+IssuedDate.get()+"\t\t"+ExpDate.get()+"\t"+
            DailyDose.get() + "\t\t"+StorageAdvice.get()+ "\t"+ NHSNumber.get()+ "\t\t"+PatientName.get()
            +"\t"+DateofBirth.get()+"\t"+PatientAddress.get()+ "\n")
            return

        def iDelete():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberofTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return

        def iReset():
            
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberofTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            return

        #===================================Frame ======================================      
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=20, width=1200, padx=35,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'),text="Hosptal Management System",padx=4)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,
                                 font=('arial',12,'bold'),text="Patient Information",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,
                                 font=('arial',12,'bold'),text="Prescription",)
        DataFrameRIGHT.pack(side=RIGHT)

        #==================================DataFrameLEFT====================================
        self.lblNameTablet = Label(DataFrameLEFT, font=('arial',12,'bold'),text="Name of Tablets:",
                                   padx=2,pady=2)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state='readonly',
                                         font=('arial',12,'bold'),width=23)
        self.cboNameTablet['value']=('','Co-codamol','Paracetamol','Amlodipine','DSR')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Further Information:",padx=2,pady=2)
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation,width=25)
        self.txtFurtherInfo.grid(row=0,column=3)
        
        self.lblRef = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Reference No:",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.txtRef.grid(row=1,column=1)

        self.lblStorage = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=2)
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.txtStorage=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=StorageAdvice,width=25)
        self.txtStorage.grid(row=1,column=3)

        self.lblDose = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dose:",padx=2,pady=2)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose,width=25)
        self.txtDose.grid(row=2,column=1)

        self.lblDUseMachine = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Driving Machines:",padx=2,pady=2)
        self.lblDUseMachine.grid(row=2,column=2,sticky=W)
        self.txtDUseMachine=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DrivingUsingMachines,width=25)
        self.txtDUseMachine.grid(row=2,column=3)

        self.lblNoOfTablets = Label(DataFrameLEFT,font=('arial',12,'bold'),text="No. of Tablets:",padx=2,pady=2)
        self.lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= NumberofTablets,width=25)
        self.txtNoOfTablets.grid(row=3,column=1)

        self.lblUseMedication = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Medication:",padx=2,pady=2)
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= HowtoUseMedication,width=25)
        self.txtUseMedication.grid(row=3,column=3)

        self.lblLot = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Lot:",padx=2,pady=2)
        self.lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= Lot,width=25)
        self.txtLot.grid(row=4,column=1)

        self.lblPatientID = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient ID:",padx=2,pady=2)
        self.lblPatientID.grid(row=4,column=2,sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientID,width=25)
        self.txtPatientID.grid(row=4,column=3)

        self.lblIssuedDate = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Issued Date:",padx=2,pady=2)
        self.lblIssuedDate.grid(row=5,column=0,sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= IssuedDate,width=25)
        self.txtIssuedDate.grid(row=5,column=1)

        self.lblNHSNumber = Label(DataFrameLEFT,font=('arial',12,'bold'),text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber.grid(row=5,column=2,sticky=W)
        self.txtNHSNumber=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= NHSNumber,width=25)
        self.txtNHSNumber.grid(row=5,column=3)

        self.lblExpDate = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Exp Date:",padx=2,pady=2)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtExpDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= ExpDate,width=25)
        self.txtExpDate.grid(row=6,column=1)

        self.lblPatientName = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Name:",padx=2,pady=2)
        self.lblPatientName.grid(row=6,column=2,sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientName,width=25)
        self.txtPatientName.grid(row=6,column=3)

        self.lblDailyDose = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Daily Dose:",padx=2,pady=2)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtDailyDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DailyDose,width=25)
        self.txtDailyDose.grid(row=7,column=1)

        self.lblDateofBirth = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date of Birth:",padx=2,pady=2)
        self.lblDateofBirth.grid(row=7,column=2,sticky=W)
        self.txtDateofBirth=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DateofBirth,width=25)
        self.txtDateofBirth.grid(row=7,column=3)

        self.lblSideEffects = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Side Effects:",padx=2,pady=2)
        self.lblSideEffects.grid(row=8,column=0,sticky=W)
        self.txtSideEffects=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PossibleSideEffects,width=25)
        self.txtSideEffects.grid(row=8,column=1)

        self.lblPatientAddress = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Address:",padx=2,pady=2)
        self.lblPatientAddress.grid(row=8,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientAddress,width=25)
        self.txtPatientAddress.grid(row=8,column=3)

        #================================DataFrameRight====================================

        self.txtPrescription=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=43,height=12,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #================================ButtonFrame=======================================

        self.btnPrescription=Button(ButtonFrame,text='Prescription',font=('arial',12,'bold'),width=24,bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        
        self.btnPrescriptionData=Button(ButtonFrame,text='Prescription Data',font=('arial',12,'bold'),
                                        width=24,bd=4,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)
        
        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width=24,bd=4,
                              command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width=24,bd=4,
                             command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=24,bd=4,
                            command=iExit)
        self.btnExit.grid(row=0,column=4)
       
