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

        
