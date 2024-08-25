from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from report import Report





def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        #############BACKGROUND IMAGE###############
        img1=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\look3.png")
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)



        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        
        img1=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\logo.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",fg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=90)

        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="gold",bg='black')
        get_str.place(x=95,y=100)

        #---------------label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        


        ######################ICON IMAGES#########################

        img2=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\username login images.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\login_image\password images.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        ##########BUTTON#############
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Foregetpassbutton
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotelmanagement")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM login WHERE email=%s", (self.txtuser.get(),))
                user_data = my_cursor.fetchone()
                
                if user_data is None:
                    messagebox.showerror("Error", "Invalid Email")
                elif user_data[6] != self.txtpass.get():  # Assuming password is stored in the third column
                    messagebox.showerror("Error", "Invalid Password")
                else:
                    # messagebox.showinfo("Success", "Welcome!")
                    # Proceed with your application logic here
                    open_main=messagebox.askyesno("YesNo","Access only admin")
                    if open_main:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                    else:
                        return
                conn.commit()
            

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {e}")

            finally:
                if 'conn' in locals() and conn.is_connected():
                    my_cursor.close()
                    conn.close()
        
        ###################### reset password..................

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
            my_cursor=conn.cursor()
            qury=("select * from login where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2)
            else:
                query=("Update login set password=%s  where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()







        ######################### forget password window......................
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="hotelmanagement")
            my_cursor=conn.cursor()

            query=("Select * from login where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.resizable(FALSE,FALSE)

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                           




            


###___________________REGISTER PAGE________________________


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
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() == "" or self.var_confpass.get() == "":
            messagebox.showerror("Error", "Password and confirm password must be filled")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotelmanagement")
                my_cursor = conn.cursor()
                
                # Check if the user already exists
                query = "SELECT * FROM login WHERE email = %s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    # Insert new user data into the database
                    insert_query = "INSERT INTO login (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    insert_values = (self.var_fname.get(), self.var_lname.get(), self.var_contact.get(),
                                    self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(),
                                    self.var_pass.get())
                    my_cursor.execute(insert_query, insert_values)
                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {e}")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    my_cursor.close()
                    conn.close()
             

                        
    def return_login(self):
        self.root.destroy()         


# hotel management system project 

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
        #self.root.resizable(False,False)
        
        ###_________frst image----------------------------
        
        
        img1=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\7-1-1080x584.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        
        ###____________LOGO___________________
        
        img2=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\logo2.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        
        ###________________TITLE___________________________________
        
        lbl_title=Label(self.root,text="HOSPITALITY PRO",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        
        ###________________MAIN FRAME____________________
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        ###_______________MENU___________________________-
        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        ###________________BTN FRAME____________________
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",command=self.des_report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        
        ###____________RIGHT SIDE IMAGE__________________
        
        img3=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\three3.jpeg")
        img3=img3.resize((1300,570),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)
        
        
        ###__________DOWN IMAGES__________________________
        
        img4=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\eat2.png")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=210)
        
        
        img5=Image.open(r"C:\Users\vicky\OneDrive\Desktop\Hotel Management System Project\images\look3.png")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=420,width=230,height=190)
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window) 
        
    def des_report(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window) 
        
        
    def logout(self):
        self.root.destroy()   



if __name__=="__main__":
    main()
    