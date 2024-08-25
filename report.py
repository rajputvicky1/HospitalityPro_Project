from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter as tk




class Report:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")
        
        
        
        self.var_contact=StringVar()
        self.var_description=StringVar()
###________________TITLE___________________________________
        
        lbl_title=Label(self.root,text="CUSTOMER BEHAVIOUR",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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
        
        #cust contact 
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:-",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # Fetch data button
        
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

##--------- FETCH DATA --------------------------------------------------    
        
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
              showDataframe.place(x=50,y=120,width=300,height=140)
              
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
              
            ## Address
              
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              query=("select Address from customers where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              
              lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
              lbladdress.place(x=0,y=90)
              
              lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl5.place(x=90,y=90)
              
    ## ----- Right side Frame ----------------------------------------------------
    
            
              Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Description",font=("arial",12,"bold"),padx=2)
              Table_Frame.place(x=450,y=55,width=700,height=400)
            

              self.text_widget =Text(Table_Frame,font=("Arial",12))
              self.text_widget.pack(fill=BOTH,expand=True)
       
              Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
              Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
         
         # Save Button 
         
              save_button =Button(self.root,text="Save text",font=("arial",16,"bold"),bg="black",fg="gold",command=self.save_text)
              save_button.place(x=970,y=460)

    def save_text(self):
      description = self.text_widget.get("1.0",END)

      if description.strip()=="": 
          messagebox.showerror("Error","Description are required",parent=self.root)
      else:
          try:
              conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
              my_cursor=conn.cursor()
              my_cursor.execute("insert INTO report (description) values(%s)",(description,))
              conn.commit()
              # self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Report has been Submited",parent=self.root)
          except Exception as es:
              messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)       


if __name__ =="__main__":
    root=Tk()
    obj=Report(root)
    root.mainloop()