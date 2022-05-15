from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import add_book
import add_member
import mysql.connector
import give_book
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="library",)
mycursor = db.cursor()
class application():
    def __init__(self, master):
        self.master = master
        # Frames
        main_frame=Frame(self.master)
        main_frame.pack()
        # top Frame
        topframe=Frame(main_frame,width=1350,height=50,bg="white",relief=SUNKEN,borderwidth=2)
        topframe.pack(fill=X,side=TOP)
        # bottom
        center_frame = Frame(main_frame, width=1350, height=700,relief=RIDGE, bg="#E1F5FE")
        center_frame.pack(fill=X)
        # Left Frame
        left_frame = Frame(center_frame, width=900, height=700,
                           borderwidth=2, relief=SUNKEN, bg="#E1F5FE")
        left_frame.pack(fill=X,side=LEFT)
        # rigfth fram
        right_frame = Frame(center_frame, width=450, height=700,
                            borderwidth=2, relief=SUNKEN, bg="#E1F5FE")
        right_frame.pack(fill=X)
        # Main desiging + function
        # search bar
        search_bar = LabelFrame(
            right_frame, text="Search Box", width=450, height=175, bg="#E1F5FE")
        search_bar.pack(fill=BOTH,side=TOP)
        # search buttion and lables
        self.search_label = Label(search_bar, text="Search", bg="#E1F5FE")
        self.search_label.grid(row=0,column=0,padx=20,pady=10)
        self.search_entry=Entry(search_bar,width=30)
        self.search_entry.grid(row=0,column=1)
        self.search_btn =Button(
            search_bar, text="Search", bg="white",width=10,command=self.sear)
        self.search_btn.grid(row=0,column=3,padx=10)
        # list bar
        # 
        list_bar = LabelFrame(right_frame, text="List Box",
            width=450, height=175, bg="#E1F5FE")
        list_bar.pack(fill=BOTH,side=TOP)
        # list bar btn////
        self.list_label=Label(list_bar,font=12,text="Sort By",bg="#E1F5FE")
        self.list_label.grid(row=0,column=1)
        # Radio btn
        self.choose=IntVar()
        self.list_radio1 = Radiobutton(
            list_bar, text="All Books", var=self.choose, value=0, bg="#E1F5FE")
        self.list_radio1.grid(row=1,column=0,pady=5)
        self.list_radio2=Radiobutton(list_bar,text="Taken Books",var=self.choose,value=1,bg="#E1F5FE")
        self.list_radio2.grid(row=1,column=1)
        self.list_radio3 = Radiobutton(
            list_bar, text="In Library", var=self.choose, value=2, bg="#E1F5FE")
        self.list_radio3.grid(row=1, column=2)
        # list btn
        self.list_btn = Button(list_bar, text="List Books", bg="white",width=10,command=self.sor)
        self.list_btn.place(x=255,y=30)
        # AddBook Button
        self.add_book_icon=PhotoImage(file="imgs\\add_book.png")
        self.add_book=Button(topframe,image=self.add_book_icon,compound=LEFT,text="Add Book",bg="white",command=self.adbook)
        self.add_book.pack(side=LEFT)
        # Add member Button
        self.add_member_icon = PhotoImage(file="imgs\\add_member.png")
        self.add_member = Button(
            topframe, image=self.add_member_icon, compound=LEFT, text="Add Member", bg="white",command=self.addmember)
        self.add_member.pack(side=LEFT)
        # Give Book Button
        self.give_book_icon = PhotoImage(file="imgs\\give_book.png")
        self.give_book = Button(
            topframe, image=self.give_book_icon, compound=LEFT, text="Give Book", bg="white",command=self.givee_book)
        self.give_book.pack(side=LEFT)
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.ss = ttk.Style()
        self.ss.configure("Bold.TButton", background="black")
        # //////////////////////Left frame work tabs////////////////////////////////////////////////////////
        self.tab1_icon=PhotoImage(file="imgs\library.png")
        self.tab2_icon = PhotoImage(file="imgs\statistics.png")
        self.tabs = ttk.Notebook(
            left_frame, width=900, height=700, style="Bold.TButton")
        self.tabs.pack(fill=BOTH)
        self.tab1 = Frame(self.tabs, bg="#E1F5FE")
        self.tab2 = Frame(self.tabs, bg="#E1F5FE")
        self.tabs.add(self.tab1,text="Library",image=self.tab1_icon,compound=LEFT)
        self.tabs.add(self.tab2,text="Statistics",image=self.tab2_icon,compound=LEFT)
        # //////////////////List box
        self.list_box = Listbox(self.tab1, width=40,
                                height=45, bg="#E1F5FE", selectmode=SINGLE)
        self.list_box.grid(row=0,column=0,sticky=N)
        self.sb=Scrollbar(self.tab1,orient=VERTICAL,command=self.list_box.yview,bg="white")
        self.list_box.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S+E)
        # ///////////////////List box detai
        self.list_box_detail = Listbox(
            self.tab1, width=110, height=45, bg="#E1F5FE")
        self.list_box_detail.grid(row=0,column=2,sticky=N)
        # /////////////////////list box mini function////////////
        def itminlist(self):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="library",)
            mycursor.execute("SELECT * FROM books")
            result = mycursor.fetchall()
            for x in range(len(result)):
                self.list_box.insert(x, str(result[x][0])+"-"+str(result[x][1]))
        itminlist(self)
        # ///////////////////////////////////////////////endend/
        # \
        # binding list box
        # 
        self.list_box.bind("<Button-1>", self.info)
        self.list_box.bind('<Double-Button-1>',self.lendi)
        # 
        # static function
        def statici(event):
                # listing all
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="library",)
            mycursor.execute("SELECT * FROM books")
            total = mycursor.fetchall()
            # 
            # total member
            mycursor.execute("SELECT * FROM member")
            total_member = mycursor.fetchall()
            # borrow book
            mycursor.execute("SELECT * FROM books WHERE book_borrow=1")
            borrow = mycursor.fetchall()
            # in library
            mycursor.execute("SELECT * FROM books WHERE book_borrow=0")
            in_lib = mycursor.fetchall()
            # total book
            self.book_total = Label(
                self.tab2, text="Total Books", font=14, bg="#E1F5FE")
            self.book_total.place(x=280, y=20)
            self.book_total1 = Entry(self.tab2, font=14, bg="#E1F5FE")
            self.book_total1.insert(0, len(total))
            self.book_total1.configure(state="readonly")
            self.book_total1.place(x=460, y=20)
            # book memeber
            self.book_member = Label(
                self.tab2, text="Total Members", font=14, bg="#E1F5FE")
            self.book_member.place(x=280, y=60)
            self.book_member1 = Entry(self.tab2, font=14, bg="#E1F5FE")
            self.book_member1.insert(0, len(total_member)) 
            self.book_member1.configure(state="readonly")
            self.book_member1.place(x=460, y=60)
            # book in library
            self.book_in_library = Label(
                self.tab2, text="Book Borrow", font=14, bg="#E1F5FE")
            self.book_in_library.place(x=280, y=100)
            self.book_in_library1 = Entry(self.tab2, font=14, bg="#E1F5FE")
            self.book_in_library1.insert(0, len(borrow))
            self.book_in_library1.configure(state="readonly")
            self.book_in_library1.place(x=460, y=100)
            # books land
            self.book_lend = Label(
                self.tab2, text="Book in Library", font=14, bg="#E1F5FE")
            self.book_lend.place(x=280, y=140)
            self.book_lend1 = Entry(self.tab2, font=14, bg="#E1F5FE")
            self.book_lend1.insert(0, len (in_lib))
            self.book_lend1.configure(state="readonly")
            self.book_lend1.place(x=460, y=140)
            self.list_box.delete(0,"end")
            itminlist(self)
        # 
        # 
        self.tabs.bind("<Button-1>", statici)
        statici(self)
    def adbook(self):
        add_book.addbook()
    def addmember(self):
        add_member.addmember()
    def info(self,event):
        try:
            self.select=self.list_box.curselection()
            for itm in self.select:
                self.idi=str(self.list_box.get(itm))
            self.idi=self.idi.split("-")
            self.idi=self.idi[0]
            mycursor.execute(f"SELECT * FROM books WHERE book_id={self.idi}")
            self.final=mycursor.fetchall()
            # book name
            self.book_name = Label(
                self.tab1, text="Book Name", font=14, bg="#E1F5FE")
            self.book_name.place(x=280,y=20)
            self.book_name1 = Entry(self.tab1, font=14, bg="#E1F5FE")
            self.book_name1.insert(0,self.final[0][1])
            self.book_name1.configure(state="readonly")
            self.book_name1.place(x=460,y=20)
            # book author
            self.book_author = Label(
                self.tab1, text="Book Author", font=14, bg="#E1F5FE")
            self.book_author.place(x=280,y=60)
            self.book_author1 = Entry(self.tab1, font=14, bg="#E1F5FE")
            self.book_author1.insert(0,self.final[0][2])
            self.book_author1.configure(state="readonly")
            self.book_author1.place(x=460,y=60)
            # book borrow
            self.book_borrow = Label(
                self.tab1, text="Book Borrow", font=14, bg="#E1F5FE")
            self.book_borrow.place(x=280,y=100)
            self.book_borrow1 = Entry(self.tab1, font=14, bg="#E1F5FE")
            self.book_borrow1.insert(0,self.final[0][4])
            self.book_borrow1.configure(state="readonly")
            self.book_borrow1.place(x=460,y=100)
            # book date
            self.book_date = Label(
                self.tab1, text="Book borrow date", font=14, bg="#E1F5FE")
            self.book_date.place(x=280,y=140)
            self.book_date1 = Entry(self.tab1, font=14, bg="#E1F5FE")
            self.book_date1.insert(0,self.final[0][5])
            self.book_date1.configure(state="readonly")
            self.book_date1.place(x=460,y=140)
        except :
            pass 
    def givee_book(self):
        give_book.lend_book()
    def sear(self):
        self.list_box.delete(0,"end")
        sear=self.search_entry.get()
        sql = f"SELECT * FROM books where book_name LIKE '%{sear}%'"
        mycursor.execute(sql)
        final = mycursor.fetchall()
        for x in range(len(final)):
            self.list_box.insert(x, str(final[x][0])+"-"+str(final[x][1]))
    def sor(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="library",)
        mycursori = db.cursor()
        self.valu=self.choose.get()
        if self.valu==0:
            mycursori.execute("SELECT * FROM books")
            self.list_box.delete(0, "end")
            result = mycursori.fetchall()
            for x in range(len(result)):
                self.list_box.insert(x, str(result[x][0])+"-"+str(result[x][1]))
        elif self.valu==1:
            mycursori.execute("SELECT * FROM books WHERE book_borrow=1")
            self.list_box.delete(0, "end")
            self.list_box.delete(0, "end")
            result = mycursori.fetchall()
            for x in range(len(result)):
                self.list_box.insert(
                    x, str(result[x][0])+"-"+str(result[x][1]))
        elif self.valu==2:
            mycursori.execute("SELECT * FROM books WHERE book_borrow=0")
            self.list_box.delete(0, "end")
            self.list_box.delete(0, "end")
            result = mycursori.fetchall()
            for x in range(len(result)):
                self.list_box.insert(
                    x, str(result[x][0])+"-"+str(result[x][1]))
    def lendi(self,event):
        try:
            self.select = self.list_box.curselection()
            for itm in self.select:
                self.idi = str(self.list_box.get(itm))
            val=[self.idi]
            give_book.lend_book(val)
        except:
            pass
def main(): 
    root = Tk()
    root.title("Library")
    root.geometry("1275x740")
    root.resizable(False,False)
    # root.iconbitmap(
    #     "../imgs/icon.ico")
    app = application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
