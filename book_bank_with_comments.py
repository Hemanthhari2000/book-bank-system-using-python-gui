# For better understanding, read the code from the main functions
# Import all the tkinter packages `note: Install tkinter and sqlite3`
from tkinter import *
# Import The Warning message box module from tkinter as "MessageBox"
import tkinter.messagebox as MessageBox
from tkinter import ttk                     # Import ttk module from tkinter
import sqlite3                              # Import sqlite3


# Function declaration for add_to_db function
def add_to_db():
    # start of try block (tries the following code)
    try:
        # Creates a connection to the database db.sql and assigns it to a variable "conn"
        conn = sqlite3.connect('db.sql')
        # creates a cursor for conn and stores it in a variable "c"
        c = conn.cursor()
        # uses the cursor to execute the sql command in the table "book"
        c.execute("insert into book (name, author) values (?,?)",  # Inserts 2 data entries "?" and "?" into the columns name and author respectively
                  (e_bname.get(), e_bauth.get()))  # get() function gets the values of e_bname and e_bauth and passes as arguments in place of "?" and "?"
        conn.commit()  # commits the changes to the database table
    # except block (if any error, gets the error and stores in variable "e")
    except Exception as e:
        # Displays the exception stored in "e"
        print(e)
    finally:                                # finally block
        conn.close()                        # closes the database connection

# Function declaration for get_from_db function


def get_from_db():

    # start of try block (tries the following code)
    try:
        # Creates a connection to the database db.sql and assigns it to a variable "conn"
        conn = sqlite3.connect('db.sql')
        # creates a cursor for conn and stores it in a variable "c"
        c = conn.cursor()
        # uses the cursor to execute the sql command in the table "book"
        # selects all data entries from table book
        c.execute('select * from book')
        # uses the cursor to fetch all the data and stores it in variable "data"
        data = c.fetchall()
        if(data == []):
            detail_view()
        else:
            # for i in data:
            #     print(i)
            return data                     # returns the variable "data"
        conn.commit()                       # commits the changes to the database table
    # except block (if any error, gets the error and stores in variable "e")
    except Exception as e:
        # Displays the exception stored in variable "e"
        print(e)
    finally:                                # finally block
        conn.close()                        # closes the database connection

# Function declaration for del_from_db function


def del_from_db():
    # start of try block (tries the following code)
    try:
        # Creates a connection to the database db.sql and assigns it to a variable "conn"
        conn = sqlite3.connect('db.sql')
        # creates a cursor for conn and stores it in a variable "c"
        c = conn.cursor()
        # uses the cursor to execute the sql command in the table "book"
        c.execute('delete from book')       # deletes the table book
        conn.commit()                       # commits the changes to the database table
    # except block (if any error, gets the error and stores in variable "e")
    except Exception as e:
        # Displays the exception stored in variable "e"
        print(e)
    finally:                                # finally block
        conn.close()                        # closes the database connection

# Button "bauth" triggers this function "reset"


def reset():
    # A messagebox pops up with title "warning" and text "Data will be reset"
    MessageBox.showwarning("Warning", "Data Will be RESET!")
    # calls del_from_db() function
    del_from_db()

# Button "paymentBtn" triggers this function "payment"


def payment():
    pass  # Skips over this part

# Button "bview" triggers this function "detail_view"


def detail_view():
    # Instantiates a child window and assigns it to variable "top"
    top = Toplevel()
    # This specifies the title of the child window using the object "top"
    top.title('Detail View')
    # This specifies the dimensions of the child window using the object "top"
    top.geometry('800x400')
    # calls get_from_db() function
    data = get_from_db()

    # Creates an Instatiation of ttk function TreeView and stores in variable "tv"
    # --> We specify "top" to position the Widget in the "top" window
    tv = ttk.Treeview(top)
    # Creates 2 columns "Name" and "Author"
    tv['columns'] = ('NAME', 'AUTHOR')

    # Specifies the name of the first column and its position and dimensions
    tv.column("#0", width=0)
    # Specifies the name of the second column and its position and dimensions
    tv.column("NAME", anchor=W, width=400)
    # Specifies the name of the third column and its position and dimensions
    tv.column("AUTHOR", anchor=W, width=400)

    # Specifies the name of the first column heading
    tv.heading("#0")
    # Specifies the name of the second column heading and its text and position
    tv.heading("NAME", text="NAME", anchor=W)
    # Specifies the name of the third column heading and its text and position
    tv.heading("AUTHOR", text='AUTHOR', anchor=CENTER)

    # It makes the "data" list as an interator like ((0. [1,2,3,4]), (1, [5,6,7,8]))
    for i, row in enumerate(data):
        tv.insert(parent='', index='end', iid=i, values=(row[1], row[2]))

    # packs the tv widget into the window container
    tv.pack()

    # Creates a Button Widget and assigns it to a variable "paymentbtn"

    # --> We specify "top" to position the Widget in the "top" window
    paymentBtn = Button(top,
                        # Specifies the text to be displayed in the label.
                        text="PAYMENT",
                        # Specifies the font and the text size
                        font=("bold", 10), bg="white",
                        command=payment)                # Triggers the function to be called on Button Click
    # It specifies the position relative to the x and y axis
    paymentBtn.place(x=200, y=300)
    # Creates a Button Widget and assigns it to a variable "exitBtn"

    # --> We specify "top" to position the Widget in the "top" window
    exitBtn = Button(top,
                     # Specifies the text to be displayed in the label.
                     text="RESET",
                     # Specifies the font and the text size
                     font=("bold", 10), bg="white",
                     command=top.destroy)            # Triggers the function to be called on Button Click
    # It specifies the position relative to the x and y axis
    exitBtn.place(x=400, y=300)

# Button "bname" triggers this function "submit"


def submit():
    # get() function gets the velue of the variable "e_bname" and assigns it to the variable "name"
    name = e_bname.get()
    # get() function gets the velue of the variable "e_bauth" and assigns it to the variable "auth"
    auth = e_bauth.get()

    if(name == "" or auth == ""):  # if the name and auth are empty when the user submits,
        # A messagebox pops up with title "message" and text "All fields are required"
        MessageBox.showinfo("Message", "All Fields are Required")
    else:  # or else
        # A messagebox pops up with title "message" and text "Successfully Registered"
        MessageBox.showinfo("Message", "Successfully Registered!!")
        # InputData gets sent to database
        add_to_db()  # calls the add_to_db() function
        # data = get_from_db()
        detail_view()  # calls the detail_view function

# Button "a" triggers this function "Continue Window"


def continue_window():
    # Instantiates a child window and assigns it to variable "top"
    top = Toplevel()
    # This specifies the title of the child window using the object "top"
    top.title('Book Bank')
    # This specifies the dimensions of the child window using the object "top"
    top.geometry("600x300")
    # We are creating a Label Widget to display text and assigning it to the variable "head"

    # --> We specify "top" to position the Widget in the "top" window
    head = Label(top,
                 # Specifies the text to be displayed in the label.
                 text='GIVE BOOK DETAILS',
                 font=('bold', 15))                  # Specifies the font and the text size
    # It anchors the widget "head" to the center and specifies the position relative to the x and y axis
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    # We are creating a Label Widget to display text and assigning it to the variable "b_name"

    # --> We specify "top" to position the Widget in the "top" window
    b_name = Label(top,
                   # Specifies the text to be displayed in the label.
                   text='BOOK NAME',
                   font=('bold', 15))                  # Specifies the font and the text size
    # It anchors the widget "b" to the center and specifies the position relative to the x and y axis
    b_name.place(relx=0.1, rely=0.4, anchor=W)
    # Declares a global variable "e_bname" to be accessed by all functions
    global e_bname
    # We are creating a Entry Widget to display a text field and Get input from the user and assigning it to variable e_bname

    # --> We specify "top" to position the Widget in the "top" window
    e_bname = Entry(top)
    # It anchors the widget "e_bname" to the East and specifies the position relative to the x and y axis
    e_bname.place(relx=0.9, rely=0.4, anchor=E)
    # Specifies the dimensions of the textfield "e_bname"
    e_bname.config(width=30)

    # We are creating a Label Widget to display text and assigning it to the variable "b_auth"

    # --> We specify "top" to position the Widget in the "top" window
    b_auth = Label(top,
                   # Specifies the text to be displayed in the label.
                   text='BOOK AUTHOR',
                   font=('bold', 15))                  # Specifies the font and the text size
    # It anchors the widget "b_auth" to the West and specifies the position relative to the x and y axis
    b_auth.place(relx=0.1, rely=0.6, anchor=W)
    # Declares a global variable "e_bauth" to be accessed by all functions
    global e_bauth
    # We are creating a Entry Widget to display a text field and Get input from the user and assigning it to variable e_bauth

    # --> We specify "top" to position the Widget in the "top" window
    e_bauth = Entry(top)
    # It anchors the widget "e_bauth" to the East and specifies the position relative to the x and y axis
    e_bauth.place(relx=0.9, rely=0.6, anchor=E)
    # Specifies the dimensions of the textfield "e_bauth"
    e_bauth.config(width=30)

    # Creates a Button Widget and assigns it to a variable "bname"

    # --> We specify "top" to position the Widget in the "top" window
    bname = Button(top,
                   # Specifies the text to be displayed in the label.
                   text="SUBMIT",
                   # Specifies the font and the text size
                   font=("bold", 10), bg="white",
                   command=submit)                     # Triggers the function to be called on Button Click
    # It anchors the widget "bname" to the West and specifies the position relative to the x and y axis
    bname.place(relx=0.2, rely=0.8, anchor=W)
    # Specifies the dimensions of the button "bname"
    bname.config(height=1, width=10)

    # Creates a Button Widget and assigns it to a variable "bview"

    # --> We specify "top" to position the Widget in the "top" window
    bview = Button(top,
                   # Specifies the text to be displayed in the label.
                   text='VIEW',
                   # Specifies the font and the text size
                   font=('bold', 10), bg='white',
                   command=detail_view)                # Triggers the function to be called on Button Click
    # It anchors the widget "bview" to the Center and specifies the position relative to the x and y axis
    bview.place(relx=0.5, rely=0.8, anchor=CENTER)
    # Specifies the dimensions of the button "bname"
    bname.config(height=1, width=10)

    # Creates a Button Widget and assigns it to a variable "bauth"

    # --> We specify "top" to position the Widget in the "top" window
    bauth = Button(top,
                   # Specifies the text to be displayed in the label.
                   text="RESET",
                   # Specifies the font and the text size
                   font=("bold", 10), bg="white",
                   command=reset)                      # Triggers the function to be called on Button Click
    # It anchors the widget "bauth" to the East and specifies the position relative to the x and y axis
    bauth.place(relx=0.8, rely=0.8, anchor=E)
    # Specifies the dimensions of the button "bauth"
    bauth.config(height=1, width=10)


# Button "b" triggers this function "cancel"
def cancel():
    # Destroys (Terminates) the "root" window
    root.destroy()
    exit()                                          # Exits from the program


# ================================= MAIN =================================

# This instantiates am object of Tk() class  to create the base window
root = Tk()
# This specifies the dimensions of the base window using the object "root"
root.geometry("600x300")
# This specifies the title of the base window using the object "root"
root.title("Book Bank")

# We are creating a Label Widget to display text and assigning it to the variable "id"

# --> We specify "root" to position the Widget in the "root" window
id = Label(root,
           # Specifies the text to be displayed in the label.
           text='WELCOME TO THE BOOK BANK MANAGEMENT SYSTEM',
           font=('bold', 15))                                  # Specifies the font and the text size
# It anchors the widget "id" to the center and specifies the position relative to the x and y axis
id.place(relx=0.5, rely=0.2, anchor=CENTER)

# Creates a Button Widget and assigns it to a variable "a"

# --> We specify "root" to position the Widget in the "root" window
a = Button(root,
           # Specifies the text to be displayed in the label.
           text="DO YOU WANT TO CONTINUE",
           # Specifies the font and the text size
           font=("bold", 10), bg="white",
           command=continue_window)                            # Triggers the function to be called on Button Click
# It anchors the widget "a" to the center and specifies the position relative to the x and y axis
a.place(relx=0.5, rely=0.4, anchor=CENTER)
# Specifies the dimensions of the button "a"
a.config(height=1, width=30)

# Creates a Button Widget and assigns it to a variable "a"

# --> We specify "root" to position the Widget in the "root" window
b = Button(root,
           # Specifies the text to be displayed in the label.
           text="CANCEL",
           # Specifies the font and the text size
           font=("bold", 10), bg="white",
           command=cancel)                                     # Triggers the function to be called on Button Click
# It anchors the widget "b" to the center and specifies the position relative to the x and y axis
b.place(relx=0.5, rely=0.6, anchor=CENTER)
# Specifies the dimensions of the button "b"
b.config(height=1, width=10)

# Keeps the Window Running
mainloop()
