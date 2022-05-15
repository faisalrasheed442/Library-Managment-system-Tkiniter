from tkinter import *
from tkinter import  messagebox
import mysql.connector

class addbook(Toplevel):
        def __init__(self):
            Toplevel.__init__(self)
            self.geometry("400x600")
            self.resizable(False, False)
            self.title("Add Book")
            # Frames/////////////////////////////////////////////
            # Frames/////////////////////////////////////////////
            self.top = Frame(self, height=150, bg="white")
            self.top.pack(fill=X)
            self.bottom = Frame(self, height=450, bg="#B3E5FC")
            self.bottom.pack(fill=X)
            # styling///////////////////
            # Heading,image and date in top frame
            self.top_image = PhotoImage(file="imgs\\add_book1.png")
            self.toplbl = Label(self.top, image=self.top_image, bg="white")
            self.toplbl.grid(row=0, column=0, padx=40)
            self.heading = Label(self.top, text="Add book",
                                 font="centaur 14", bg="white")
            self.heading.grid(row=0, column=1)
            # Label 1
            self.book_name = Label(self.bottom, text="book Name",
                                   bg="#E1F5FE")
            self.book_name.place(x=40,y=10)
            self.book_name1 = Entry(self.bottom, font="centaur 11", bg="white")
            self.book_name1.place(x=120,y=10)
            # label2
            self.author_name = Label(
                self.bottom, text="Author Name", bg="#E1F5FE")
            self.author_name.place(x=40,y=40)
            self.author_name1 = Entry(self.bottom, bg="white")
            self.author_name1.place(x=120,y=40)
            # label 3
            self.btnicon2 = PhotoImage(file="imgs\\add_book.png")
            self.add_people = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add Book",command=self.bookad,
                                    font="centaur 11", bg="white", width=120)
            self.add_people.place(x=150, y=100)
        def bookad(self):
            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="1234",
                    database="library",)
                mycursor = db.cursor()
                mycursor.execute(
                    f"INSERT INTO books (book_name,book_author) VALUES('%s','%s')" % (self.book_name1.get(), self.author_name1.get()))
                db.commit()
                mbox=messagebox.showinfo("Sucess","Book has been added")
                self.destroy()
            except:
                mbox=messagebox.showerror("Warning","Please Enter Missing fileds")
