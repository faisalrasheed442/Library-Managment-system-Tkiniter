from tkinter import *
from tkinter import ttk
import mysql.connector
import datetime
from tkinter import messagebox
# 
class addmember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x600")
        self.resizable(False, False)
        self.title("Add People")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#E1F5FE")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="imgs\\add_member1.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Add Member",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#E1F5FE")
        self.name.place(x=40, y=10)
        self.name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.name1.place(x=160, y=10)
        # label2
        self.Department_name = Label(self.bottom, text="Department Name",
                              font="centaur 11", bg="#E1F5FE")
        self.Department_name.place(x=40, y=40)
        self.Department_name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.Department_name1.place(x=160, y=40)
        # label 3
        self.phone = Label(self.bottom, text="Contact No.",
                            font="centaur 11", bg="#E1F5FE")
        self.phone.place(x=40, y=70)
        self.phone1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.phone1.place(x=160, y=70)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="imgs\\add_member.png")
        self.add_member = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add member",
                                 font="centaur 11", bg="white", width=120, command=self.add_membernow)
        self.add_member.place(x=150, y=100)

    def add_membernow(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="library",)
            mycursor = db.cursor()
            mycursor.execute(
                f"INSERT INTO member (member_name,member_department,member_phone) VALUES('%s','%s','%s')" % (self.name1.get(), self.Department_name1.get(), self.phone1.get()))
            db.commit()
            mbox = messagebox.showinfo("Sucess", "Member has been Registered")
            self.destroy()
        except:
            mbox = messagebox.showerror(
                "Warning", "Please Enter Missing fileds")
        
