import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
import pymysql
win = tk.Tk()
win.geometry("1920x1080+0+0")
win.title("Student Manager")
#win.wm_iconbitmap('python.ico')

tittle_label = tk.Label(win, text = "Student Manager",font=("JetBrains Mono",25),border = 12,relief = tk.GROOVE)
tittle_label.pack(side = tk.TOP, fill = tk.X)

detail_frame = tk.LabelFrame(win,text = "Enter Details", font = ("JetBrains Mono",25))
detail_frame.place(x = 20, y = 70,width = 470, height = 650,bordermode="inside")

data_frame = tk.Frame(win,bd=1,relief = tk.RIDGE)
data_frame.place(x = 500 , y = 65 ,width=1000,height=650)

# - - - - - - - Variables - - - - - - -
Id = tk.StringVar()
Name = tk.StringVar()
Major = tk.StringVar()
Class = tk.StringVar()
GPA = tk.StringVar()
Birth = tk.StringVar()
Gender = tk.StringVar()
Birth = tk.StringVar()
Gender = tk.StringVar()
Hometown = tk.StringVar()
Address = tk.StringVar()
search_by = tk.StringVar()
search_text = tk.StringVar()
# - - - - - - - - - - - - - - - - - - - 


# - - - INPUT - - -
id_lbl = tk.Label(detail_frame, text = "ID: ",font = ("JetBrains Mono", 17))
id_lbl.grid(row = 0, column = 0, padx = 2 ,pady = 2)

id_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17), textvariable = Id)
id_ent.grid(row = 0, column = 1, padx = 1, pady = 1) 

name_lbl = tk.Label(detail_frame, text = "Name: ",font = ("JetBrains Mono", 17))
name_lbl.grid(row = 1, column = 0, padx = 2 ,pady = 2)

name_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17), textvariable = Name)
name_ent.grid(row = 1, column = 1, padx = 2, pady = 2) 

major_lbl = tk.Label(detail_frame, text = "Major: ",font = ("JetBrains Mono", 17))
major_lbl.grid(row = 2, column = 0, padx = 2 ,pady = 2)

major_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17), textvariable = Major)
major_ent.grid(row = 2, column = 1, padx = 2, pady = 2) 

class_lbl = tk.Label(detail_frame, text = "Class: ",font = ("JetBrains Mono", 17))
class_lbl.grid(row = 3, column = 0, padx = 2 ,pady = 2)

class_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17), textvariable = Class)
class_ent.grid(row = 3, column = 1, padx = 2, pady = 2) 

gpa_lbl = tk.Label(detail_frame, text = "GPA: ",font = ("JetBrains Mono", 17))
gpa_lbl.grid(row = 4, column = 0, padx = 2 ,pady = 2)

gpa_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17),textvariable = GPA)
gpa_ent.grid(row = 4, column = 1, padx = 2, pady = 2) 

birth_lbl = tk.Label(detail_frame, text = "Birth: ",font = ("JetBrains Mono", 17))
birth_lbl.grid(row = 5, column = 0, padx = 2 ,pady = 2)

birth_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17),textvariable=Birth)
birth_ent.grid(row = 5, column = 1, padx = 2, pady = 2) 

gender_lbl = tk.Label(detail_frame,text = "Gender: " ,bd = 7, font = ("JetBrains Mono",17))
gender_lbl.grid(row = 6, column = 0, padx = 2, pady = 2)

gender_ent = ttk.Combobox(detail_frame, font = ("JetBrains Mono",17),textvariable=Gender)
gender_ent['value'] = ("Male", "Female", "Others")
gender_ent.grid(row = 6, column = 1, padx = 2, pady = 2)

hometown_lbl = tk.Label(detail_frame, text = "Hometown: ",font = ("JetBrains Mono", 17))
hometown_lbl.grid(row = 7, column = 0, padx = 2 ,pady = 2)

hometown_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17),textvariable=Hometown)
hometown_ent.grid(row = 7, column = 1, padx = 2, pady = 2) 

address_lbl = tk.Label(detail_frame, text = "Address: ",font = ("JetBrains Mono", 17))
address_lbl.grid(row = 8, column = 0, padx = 2 ,pady = 2)

address_ent = tk.Entry(detail_frame, bd = 7, font = ("JetBrains Mono", 17),textvariable= Address)
address_ent.grid(row = 8, column = 1, padx = 2, pady = 2) 

# - - - - - - - - -

# - - - - - - Functions - - - - - -
def fetch_data():
    connect = pymysql.connect(host = "172.17.0.2", user="root",password = "28122003",database="student_manager")
    curr = connect.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
            connect.commit()
    connect.close()

def add_data():
    if Id.get() == "" or Name.get() == "" or Major.get() == "" or Class.get() == "" or GPA.get() == "" or Birth =="" or Gender.get() == "" or Hometown.get() == "" or Address.get() == "":
        messagebox.showerror("Error!","Please fill all the fields!")
    else:
        connect = pymysql.connect(host="localhost",user="root",password="",database="student_manager")
        curr = connect.cursor()
        curr.execute("INSERT INTO DATA VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Id.get(),Name.get(),Major.get(),Class.get(),GPA.get(),Birth.get(),Gender.get(),Hometown.get(),Address.get()))
        connect.commit()
        connect.close()
def get_cursor(event):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    
    Id.set(row[0])
    Name.set(row[1])
    Major.set(row[2])
    Class.set(row[3])
    GPA.set(row[4])
    Birth.set(row[5])
    Gender.set(row[6])
    Hometown.set(row[7])
    Address.set(row[8])

def clear():
    Id.set("")
    Name.set("")
    Major.set("")
    Class.set("")
    GPA.set("")
    Birth.set("")
    Gender.set("")
    Hometown.set("")
    Address.set("")

def update_data():
    connect = pymysql.connect(host="localhost", user="root",password="",database="student_manager")
    curr = connect.cursor()
    curr.execute("update data set Name = %s, Major = %s, Class = %s, GPA = %s, Birth = %s, Gender = %s, Hometown = %s, Address = %s where Id = %s",(Name.get(),Major.get(),Class.get(),GPA.get(),Birth.get(),Gender.get(),Hometown.get(),Address.get(),Id.get()))
    connect.commit()
    connect.close()
    fetch_data()
    clear()

def delete():
    connect = pymysql.connect(host="localhost", user="root",password="",database="student_manager")
    cc = student_table.focus()
    content = student_table.item(cc)
    pp = content['values'][0]
    strr = 'delete from data where id=%s'
    curr = connect.cursor()
    curr.execute(strr,(pp))
    connect.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))


def search():
    connect = pymysql.connect(host = "localhost", user="root",password = "",database="student_manager")
    curr = connect.cursor()
    sql = "SELECT * FROM  data WHERE {} LIKE %s".format(str(search_by.get()))
    curr.execute(sql,('%' + str(search_text.get()) + '%',))
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',END,values=row)
        connect.commit()

    # sql = "SELECT * FROM  data WHERE {} LIKE %s".format(str(search_by.get()))
    # curr.execute(sql,('%' + str(search_text.get()) + '%',))
    # connect.commit()
    # print(curr._executed)
    connect.close()

# - - - - - - - - - - - - - - - - - 


# - - Button - - -
btn_frame = tk.Frame(detail_frame,bd = 10)
btn_frame.place(x = 30, y = 480, width = 400, height = 450)

add_btn = tk.Button(btn_frame, bd = 7, text = "Add", font = ("JetBrains Mono",17), width = 10,relief = "flat",command=add_data)
add_btn.grid(row = 0, column = 0, padx = 2, pady = 2)

delete_btn = tk.Button(btn_frame, bd = 7, text = "Delete", font = ("JetBrains Mono",17), width = 10,relief = "flat",command=delete)
delete_btn.grid(row = 0, column = 1, padx = 2, pady = 2)

update_btn = tk.Button(btn_frame, bd = 7, text = "Update", font = ("JetBrains Mono",17), width = 10,relief = "flat",command=update_data)
update_btn.grid(row = 1, column = 0, padx = 2, pady = 2)

clear_btn = tk.Button(btn_frame, bd = 7, text = "Clear", font = ("JetBrains Mono",17), width = 10,relief = "flat",command=clear)
clear_btn.grid(row = 1, column = 1, padx = 2, pady = 2)

# - - - - - - - - -

#- - - - - Search - - - - -
search_frame = tk.Frame(data_frame,bd = 10)
search_frame.pack(side = tk.TOP, fill=tk.X)

search_label = tk.Label(search_frame, text="Search ", font = ("JetBrains Mono",15))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("JetBrains Mono",17),state="readonly",textvariable=search_by)
search_in['value'] = ("ID","Name","Major","Class","GPA")
search_in.grid(row = 0, column = 1, padx = 2, pady = 2)

search_entry = tk.Entry(search_frame, bd = 7, font = ("JetBrains Mono", 17),textvariable=search_text)
search_entry.grid(row = 0, column = 2, padx = 2, pady = 2) 

search_btn = tk.Button(search_frame,text = "Search", font = ("JetBrains Mono", 15 ),command=search)
search_btn.grid(row=0,column=3,padx=2,pady=2)
show_all_btn = tk.Button(search_frame,text = "Show all", font = ("JetBrains Mono", 15 ),command=fetch_data)
show_all_btn.grid(row=0,column=4,padx=2,pady=2)
#- - - - - - - - - - - - - -

#- - - - - Data Frame - - - - - -
main_frame = tk.Frame(data_frame,bd = 11,relief=("groove"))
main_frame.pack(fill=tk.BOTH,expand=True)

x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)
y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)

'''ID, Name, Major, Class, GPA, Birth, Gender, Hometown, Address'''
student_table = ttk.Treeview(main_frame,columns=("ID","Name","Major","Class", "GPA", "Birth", "Gender", "Hometown", "Address"),
yscrollcommand = y_scroll,xscrollcommand= x_scroll)

x_scroll.config(command=student_table.xview)
y_scroll.config(command=student_table.yview)

x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

student_table.heading("ID",text="ID")
student_table.heading("Name",text="Name")
student_table.heading("Major",text="Major")
student_table.heading("Class",text="Class")
student_table.heading("GPA",text="GPA")
student_table.heading("Birth",text="Birth")
student_table.heading("Gender",text="Gender")
student_table.heading("Hometown",text="Hometown")
student_table.heading("Address",text="Address")

student_table['show'] = 'headings'

student_table.column("ID",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Major",width = 100)
student_table.column("GPA",width=100)
student_table.column("Birth",width=100)
student_table.column("Gender",width=100)
student_table.column("Hometown",width=100)
student_table.column("Address",width=100)
student_table.pack(fill = tk.BOTH, expand=True)
fetch_data()
student_table.bind("<ButtonRelease-1>",get_cursor)
#- - - - - - - - - - - - - - - - -

win.mainloop()