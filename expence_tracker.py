
import datetime
import sqlite3
from tkcalendar import DateEntry
import sqlite3;cx = sqlite3.connect("test.db") # test.db will be created or opened
from tkinter import *
import tkinter.ttk as ttk

# Connecting to the Database
connector = sqlite3.connect("Expense Tracker.db")
cursor = connector.cursor()
connector.execute('CREATE TABLE IF NOT EXISTS ExpenseTracker (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Date DATETIME, Payee TEXT, Description TEXT, Amount FLOAT, ModeOfPayment TEXT)')
connector.commit()

# Backgrounds and Fonts
dataentry_frame_bg = 'Red'
buttons_frame_bg = 'Tomato'
hlb_btn_bg = 'IndianRed'
lbl_font = ('Georgia', 13)
entry_font = 'Times 13 bold'
btn_font = ('Gill Sans MT', 13)

# Initializing the GUI window
root = Tk()
root.title('PythonGeeks Expense Tracker')
root.geometry('1200x550')
root.resizable(0, 0)

Label(root, text='EXPENSE TRACKER', font=('Noto Sans CJK TC', 15, 'bold'), bg=hlb_btn_bg).pack(side=TOP, fill=X)

# StringVar and DoubleVar variables
desc = StringVar()
amnt = DoubleVar()
payee = StringVar()
MoP = StringVar(value='Cash')

# Frames
data_entry_frame = Frame(root, bg=dataentry_frame_bg)
data_entry_frame.place(x=0, y=30, relheight=0.95, relwidth=0.25)

buttons_frame = Frame(root, bg=buttons_frame_bg)
buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)

tree_frame = Frame(root)
tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)

# Data Entry Frame
Label(data_entry_frame, text='Date (M/DD/YY) :', font=lbl_font, bg=dataentry_frame_bg).place(x=10, y=50)
def DateEntry():
 date = DateEntry(data_entry_frame, date=datetime.datetime.now().date(), font=entry_font)
def date():
 date.place(x=160, y=50)

Label(data_entry_frame, text='Payee\t             :', font=lbl_font, bg=dataentry_frame_bg).place(x=10, y=230)
Entry(data_entry_frame, font=entry_font, width=31, text=payee).place(x=10, y=260)

Label(data_entry_frame, text='Description           :', font=lbl_font, bg=dataentry_frame_bg).place(x=10, y=100)
Entry(data_entry_frame, font=entry_font, width=31, text=desc).place(x=10, y=130)

Label(data_entry_frame, text='Amount\t             :', font=lbl_font, bg=dataentry_frame_bg).place(x=10, y=180)
Entry(data_entry_frame, font=entry_font, width=14, text=amnt).place(x=160, y=180)

Label(data_entry_frame, text='Mode of Payment:', font=lbl_font, bg=dataentry_frame_bg).place(x=10, y=310)
dd1 = OptionMenu(data_entry_frame, MoP, *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
dd1.place(x=160, y=305)
dd1.configure(width=20, font=entry_font)
def add_another_expense():
 Button(data_entry_frame, text='Add expense', command=add_another_expense, font=btn_font, width=30, bg=hlb_btn_bg).place(x=10, y=395)
 Button(data_entry_frame, text='Convert to words before adding', font=btn_font, width=30, bg=hlb_btn_bg).place(x=10, y=450)

# Buttons' Frame
def remove_expense():
    Button(buttons_frame, text='Delete Expense', font=btn_font, width=25, bg=hlb_btn_bg, command=remove_expense).place(x=30, y=5)
def clear_fields():
 Button(buttons_frame, text='Clear Fields in DataEntry Frame', font=btn_font, width=25, bg=hlb_btn_bg, command=clear_fields).place(x=335, y=5)
def remove_all_expenses():  
 Button(buttons_frame, text='Delete All Expenses', font=btn_font, width=25, bg=hlb_btn_bg, command=remove_all_expenses).place(x=640, y=5)
def view_expense_details():
 Button(buttons_frame, text='View Selected Expense\'s Details', font=btn_font, width=25, bg=hlb_btn_bg, command=view_expense_details).place(x=30, y=65)
def edit_expense():
 Button(buttons_frame, text='Edit Selected Expense', command=edit_expense, font=btn_font, width=25, bg=hlb_btn_bg).place(x=335, y=65)
def selected_expense_to_words():
 Button(buttons_frame, text='Convert Expense to a sentence', font=btn_font, width=25, bg=hlb_btn_bg, command=selected_expense_to_words).place(x=640, y=65)

# Treeview Frame
table = ttk.Treeview(tree_frame, selectmode=BROWSE, columns=('ID', 'Date', 'Payee', 'Description', 'Amount', 'Mode of Payment'))
X_Scroller = Scrollbar(table, orient=HORIZONTAL, command=table.xview)
Y_Scroller = Scrollbar(table, orient=VERTICAL, command=table.yview)
X_Scroller.pack(side=BOTTOM, fill=X)
Y_Scroller.pack(side=RIGHT, fill=Y)
table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)
table.heading('ID', text='S No.', anchor=CENTER)
table.heading('Date', text='Date', anchor=CENTER)
table.heading('Payee', text='Payee', anchor=CENTER)
table.heading('Description', text='Description', anchor=CENTER)
table.heading('Amount', text='Amount', anchor=CENTER)
table.heading('Mode of Payment', text='Mode of Payment', anchor=CENTER)
table.column('#0', width=0, stretch=NO)
table.column('#1', width=50, stretch=NO)
table.column('#2', width=95, stretch=NO)
table.column('#3', width=150, stretch=NO)
