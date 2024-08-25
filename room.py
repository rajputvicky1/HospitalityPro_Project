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
        
        
        #check in date
       
        check_in_date=Label(labelframeleft,text="Check_In Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        
        #check_out date
        
        
        lbl_check_out=Label(labelframeleft,text="Check_Out Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txt_check_out.grid(row=2,column=1)
        
        
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
        
        # Available Room
        
        lblRoomAvailable=Label(labelframeleft,text="Available Room:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select Room from room")
        rows=my_cursor.fetchall()
        
        # combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        # room_available=["Yes", "No"]
        # combo_RoomNo["value"]=room_available
        # combo_RoomNo.current(0)
        # combo_RoomNo.grid(row=4,column=1) 
        
        # Meal
        
        lblMeal=Label(labelframeleft,text="Meal:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)
        
        # No of Days
        
        lblNoofDays=Label(labelframeleft,text="No Of Days:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=6,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_noOfdays,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=6,column=1)
        
        # Paid 
        
        lblNoofDays=Label(labelframeleft,text="Paid Tax:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=7,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=7,column=1)
        
        # Sub Total
        
        lblNoofDays=Label(labelframeleft,text="Sub Total:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=8,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=8,column=1)
        
        # Total Cost
        lblNoofDays=Label(labelframeleft,text="Total Cost:-",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=9,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=9,column=1)
        
        
        ###_________________BIll Button_____________
        
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
        ###------------PRINT Button--------------
        
        btnprint=Button(labelframeleft,text="Print",command=self.print_receipt,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnprint.grid(row=10,column=1,padx=1,sticky=W)
        
        
        
        ###______________btns__________________
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=416,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        ### _________Rightside Image___________________________
        
        img3=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\bed2.png")
        img3=img3.resize((530,380),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=50,width=530,height=380)
        
        
        
        ###___________TABLE FRAME search system______________________________
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        
        ###____________________________SHOW DATA TABLE_________________
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)
        
        
        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)
        
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No Of Days")
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

     ##--Add Data
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_contact.get(),
                                                                                  self.var_checkin.get(),
                                                                                  self.var_checkout.get(),
                                                                                  self.var_roomtype.get(),
                                                                                  self.var_roomavailable.get(),
                                                                                  self.var_meal.get(),
                                                                                  self.var_noOfdays.get()
                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
    
    ## Fetch Data
        
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from room")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
           self.room_table.delete(*self.room_table.get_children())
           for i in rows:
             self.room_table.insert("",END,values=i)
           conn.commit()
         conn.close() 
    
    ## Get cursor
         
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])
    
    ## Update function    
        
    def update(self):
        if self.var_contact.get()=="":
           messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where contact=%s",(
                                                                                                                                                          
                                                                                                                          self.var_checkin.get(),
                                                                                                                          self.var_checkout.get(),
                                                                                                                          self.var_roomtype.get(),
                                                                                                                          self.var_roomavailable.get(),
                                                                                                                          self.var_meal.get(),
                                                                                                                          self.var_noOfdays.get(),
                                                                                                                          self.var_contact.get()       
                                                                                                                        ))
                          
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
            
            
      ## Delete function
            
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
           conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
           my_cursor=conn.cursor()
           query="delete from room where contact=%s"
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value)
        else:
            if not mDelete:
              return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    ## Reset function
    
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
                
          
             
       ###______________ALL DATA FETCH____________
       
        
    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
      else:
          conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
          my_cursor=conn.cursor()
          query=("select Name from customers where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          if row==None:
            messagebox.showerror("Error","This Number Not Found",parent=self.root)
          else:
              conn.commit()
              conn.close()
              
              ## Name
              
              showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
              showDataframe.place(x=450,y=55,width=300,height=180)
              
              lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
              lblName.place(x=0,y=0)
              
              lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl.place(x=90,y=0)
              
              ## Gender
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              query=("select Gender from customers where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
              lblGender.place(x=0,y=30)
              
              lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl2.place(x=90,y=30)
              
              ## Email
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              query=("select Email from customers where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              
              lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
              lblemail.place(x=0,y=60)
              
              lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl3.place(x=90,y=60)
              
              ## Nationality
              
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              query=("select Nationality from customers where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lblnationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
              lblnationality.place(x=0,y=90)
              
              lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl4.place(x=90,y=90)
              
              ## Address
              
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              query=("select Address from customers where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
              lbladdress.place(x=0,y=120)
              
              lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl5.place(x=90,y=120)
     
     ### Search system
     
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotelmanagement")
        my_cursor = conn.cursor()
    
        query = "SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get())
        search_pattern = '%' + self.txt_search.get() + '%'

        my_cursor.execute(query, (search_pattern,))
        rows = my_cursor.fetchall()
    
        if len(rows) != 0:
           self.room_table.delete(*self.room_table.get_children())
           for i in rows:
               self.room_table.insert("", END, values=i)
           conn.commit()
    
        conn.close() 
        
        
    def print_receipt(self):
        contact = self.var_contact.get()
        checkin = self.var_checkin.get()
        checkout = self.var_checkout.get()
        roomtype = self.var_roomtype.get()
        roomavailable = self.var_roomavailable.get()
        meal = self.var_meal.get()
        noOfdays = self.var_noOfdays.get()
        paidtax = self.var_paidtax.get()
        actualtotal = self.var_actualtotal.get()
        total = self.var_total.get()
    
        receipt_content = f"Customer Contact: {contact}\n" \
                          f"Check-in Date: {checkin}\n" \
                          f"Check-out Date: {checkout}\n" \
                          f"Room Type: {roomtype}\n" \
                          f"Room Available: {roomavailable}\n" \
                          f"Meal: {meal}\n" \
                          f"No. of Days: {noOfdays}\n" \
                          f"Paid Tax: {paidtax}\n" \
                          f"Actual Total: {actualtotal}\n" \
                          f"Total Cost: {total}\n"

        try:
            # Save receipt content to a text file
            filename = f"Receipt_{contact}.txt"
            with open(filename, 'w') as f:
                f.write(receipt_content)

            # Open the file using the default text editor for the system
            os.system(filename)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while printing: {str(e)}")

              
    def total(self):
      inDate = self.var_checkin.get()
      outDate = self.var_checkout.get()

      if not inDate or not outDate:
          self.display_error_message("Please provide both check-in and checkout dates.")
          return

      try:
          inDate = datetime.strptime(inDate, "%d/%m/%Y")
          outDate = datetime.strptime(outDate, "%d/%m/%Y")
          
          if outDate < inDate:
              self.display_error_message("Checkout date cannot be earlier than check-in date")
              return  # Return if there's an error

          # Calculate number of days
          
          num_of_days = abs((outDate - inDate).days)
          self.var_noOfdays.set(num_of_days)  # Set the value of var_noOfdays
          
          # Determine meal and room costs based on user input
          meal_cost = 0
          room_cost = 0
    
          if self.var_meal.get().lower() == "breakfast":
              meal_cost = 150
          elif self.var_meal.get().lower() == "lunch":
              meal_cost = 250
          elif self.var_meal.get().lower() == "dinner":
              meal_cost = 300

          if self.var_roomtype.get().lower() == "single":
              room_cost = 500
          elif self.var_roomtype.get().lower() == "double":
              room_cost = 700
          elif self.var_roomtype.get().lower() == "luxury":
              room_cost = 1000

          # Calculate total cost without tax
          total_cost = (meal_cost + room_cost) * num_of_days
          
          # Calculate GST
          gst_rate = 0.09  # Assuming a 9% GST rate
          gst_amount = total_cost * gst_rate
          
          # Calculate total cost including tax
          total_with_gst = total_cost + gst_amount

          # Set values in GUI variables
          self.var_paidtax.set("Rs. %.2f" % gst_amount)
          self.var_actualtotal.set("Rs. %.2f" % total_cost)
          self.var_total.set("Rs. %.2f" % total_with_gst)
          
      except ValueError:
          self.display_error_message("Invalid date format. Please use dd/mm/yyyy format.")
          
    def display_error_message(self, message):
      messagebox.showerror("Error",message,parent=self.root)
            
if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()