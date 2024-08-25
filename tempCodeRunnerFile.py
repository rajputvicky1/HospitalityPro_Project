from tkinter import *
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import os
from mysql.connector import Error
from report import Report
from tkcalendar import Calendar, DateEntry


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        
        self.root.geometry("1295x550+230+220")
        self.root.resizable(False,False)        
        
        ###_______________VARIABLE_______________________________
        
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        ###________________TITLE___________________________________
        
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        
        ###____________LOGO___________________
        
        img2=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\logo2.jpg")
        img2=img2.resize((100,45),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=4,y=2,width=100,height=45)
        
        ###__________LABEL FRAME_______________
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        ###______________LABEL AND ENTRY___________________
       #cust contact 
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:-",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # Fetch data button
        
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)
        
        
        # #check in date
       
        # check_in_date=Label(labelframeleft,text="Check_In Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        # check_in_date.grid(row=1,column=0,sticky=W)
        # txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        # txtcheck_in_date.grid(row=1,column=1)
        
        # #check_out date
        
        
        # lbl_check_out=Label(labelframeleft,text="Check_Out Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        # lbl_check_out.grid(row=2,column=0,sticky=W)
        # txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        # txt_check_out.grid(row=2,column=1)
        
        # Create a DateEntry widget for check-in date
        check_in_date = Label(labelframeleft, text="Check_In Date:-", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = DateEntry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)

        # Create a DateEntry widget for check-out date
        lbl_check_out = Label(labelframeleft, text="Check_Out Date:-", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_out.grid(row=2, column=0, sticky=W)
        txt_check_out = DateEntry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txt_check_out.grid(row=2, column=1)
        
        # Room Type
        
        label_RoomType=Label(labelframeleft,text="Room Type:-",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from room")
        ide=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        room_types = ["Single", "Double", "laxary"]
        combo_RoomType["value"] = room_types
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1) 