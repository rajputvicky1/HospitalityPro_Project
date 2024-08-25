from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ########......... varialble

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        ########### bg image ################
        img1=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\look3.png")
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)

        ############ left image #######################
        
        img2=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\look1.png")
        img2=img2.resize((520,800),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=520,height=800)


        
        ###### main frame ######################

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="gold",bg="black")
        register_lbl.place(x=20,y=20)

        ############ label and entry #################

        ###............row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="gold")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="gold")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        ######........row2
         
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="black",fg="gold")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="gold")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #########..........row3

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="gold")
        security_Q.place(x=50,y=240)
        
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="gold")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        ############..............row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="gold")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="gold")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm.place(x=370,y=340,width=250)


        ###############............. checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="black",fg="gold",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #############.........Buttons

        img=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Login and Reg. program\Images\register.png")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="black")
        b1.place(x=20,y=420,width=200)



        img1=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Login and Reg. program\Images\login.png")
        img1=img1.resize((200,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="black")
        b1.place(x=370,y=420,width=200)


        #############.......function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")


        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
            my_cursor=conn.cursor()
            query=("select * from login where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_securityQ.get(),
                                                                                     self.var_securityA.get(),
                                                                                     self.var_pass.get()

                                                                                ))  
            conn.commit()
            conn.close()
            messagebox.showinfo("success","Register Successfully") 

            
    



if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()