from tkinter import *
from tkinter import ttk
import mysql.connector
import datetime
from tkinter import messagebox
#
def booklis():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="library",)
    mycursor = db.cursor()
    mycursor.execute("SELECT * from books WHERE book_borrow=0")
    final = mycursor.fetchall()
    book_listi = list()
    for x in range(len(final)):
        y = str(str(final[x][0])+"-"+str(final[x][1]))
        book_listi.insert(x, y)
    return book_listi

class lend_book(Toplevel):
    def __init__(self,book_list=booklis()):
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
        self.top_image = PhotoImage(file="imgs\\give_book1.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Give Book",font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        #
        self.book_list=list(book_list)
        # Label 1
        self.book_name = Label(self.bottom, text="Book Name",font="centaur 11", bg="#E1F5FE")
        self.book_name.place(x=40, y=10)
        self.como_book_value=StringVar()
        self.como_book = ttk.Combobox(
            self.bottom, textvariable=self.como_book_value, values=self.book_list)
        self.como_book.configure(state="readonly")
        self.como_book.place(x=160, y=10)
        # 
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="library",)
        mycursor = db.cursor()
        # como functioni
        mycursor.execute("SELECT * FROM member")
        final = mycursor.fetchall()
        member_list = list()
        for x in range(len(final)):
            y = str(str(final[x][0])+"-"+str(final[x][1]))
            member_list.insert(x, y)
        # label2
        self.book_name = Label(self.bottom, text="Book Name",font="centaur 11", bg="#E1F5FE")
        self.book_name.place(x=40, y=40)
        self.member_detail = StringVar()
        self.como_member = ttk.Combobox(self.bottom, textvariable=self.member_detail, values=member_list)
        self.como_member.place(x=160, y=40)
        self.como_member.configure(state="readonly")
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="imgs\\give_book.png")
        self.add_member = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Give Book",font="centaur 11", bg="white", width=120, command=self.give_booknow)
        self.add_member.place(x=150, y=100)

    def give_booknow(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="library",)
            mycursor = db.cursor()
            name=self.member_detail.get()
            name=name.split("-")
            name=name[1]
            book=self.como_book_value.get()
            book=book.split("-")
            book=book[0]
            today = str(datetime.datetime.today())
            today = today.split()
            today = today[0]
            sql_update = "UPDATE books SET book_borrow=1, taken_by='%s', borrow_date='%s' WHERE book_id='%s'" % (name,today , book)
            mycursor.execute(sql_update)
            db.commit()
            mbox = messagebox.showinfo("Sucess", f"Book has been given to {name}")
            self.destroy()
        except:
            mbox = messagebox.showerror(
                "Warning", "Please Enter Missing fileds")
