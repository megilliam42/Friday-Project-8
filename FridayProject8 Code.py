from tkinter import *
from tkinter import ttk

import sqlite3

connection = sqlite3.connect('feedbackDB.db')
cursor = connection.cursor()

cursor.execute('''  CREATE TABLE IF NOT EXISTS Feedback
               (Name TEXT, Email TEXT, Feedback TEXT)''')

def feedbackBtpress():
    nameinput = nameEntry.get()
    emailinput = emailEntry.get()
    feedbackinput = feedbackEntry.get()
    cursor.execute('''INSERT INTO Feedback 
                   (Name, Email,Feedback) VALUES (?,?,?)
                   ''',(nameinput, emailinput, feedbackinput))
    connection.commit()


def dataBtpress():
    password = input ("Please enter password:")
    if password == "password":  
        cursor.execute('SELECT * FROM Feedback')
       
        values = cursor.fetchall()

        for row in values:
                print("Name:", row[0], "Email:", row[1], "Feedback:", row[2])
            

root = Tk()
root.title ("Friday Prject 8")
root.geometry('500x500')

root.tk.call('tk','scaling', 2)


#labels
nameLabel= Label(root, text ="Name:")
nameLabel.grid(column=0, row= 0)

emailLabel = Label(root, text = "Email:")
emailLabel.grid(column= 0, row=1)

feedbackLabel = Label(root,text = "Feedback:")
feedbackLabel.grid(column=0, row=2)


#entries
nameEntry = Entry(root)
nameEntry.grid(column=1, row=0)

emailEntry = Entry(root)
emailEntry.grid(column=1, row= 1)

feedbackEntry = Entry(root)
feedbackEntry.grid(column= 1, row= 2)


#buttons
feedbackBt= Button(root, text= "Submit Feedback", command= feedbackBtpress)
feedbackBt.grid(column=1, row=3)

dataBt= Button(root, text= "Print Current Data", command= dataBtpress)
dataBt.grid(column=1, row=4)

root.mainloop()

