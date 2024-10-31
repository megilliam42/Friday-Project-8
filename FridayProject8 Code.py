
#imports for gui
from tkinter import *
from tkinter import ttk

#import for database
import sqlite3

#connects program to database called feedbackDB.db
connection = sqlite3.connect('feedbackDB.db')
cursor = connection.cursor()

#creates the table so it can take user input 
cursor.execute('''  CREATE TABLE IF NOT EXISTS Feedback
               (Name TEXT, Email TEXT, Feedback TEXT)''')

#adds userinput to the database
def feedbackBtpress():
    #gets information from gui after user presses the Submit Feedback button call feedbackBt
    nameinput = nameEntry.get()
    emailinput = emailEntry.get()
    feedbackinput = feedbackEntry.get()

    #inputs the variable inputs into the data base 
    cursor.execute('''INSERT INTO Feedback 
                   (Name, Email,Feedback) VALUES (?,?,?)
                   ''',(nameinput, emailinput, feedbackinput))
    #commits the new inserts to the database
    connection.commit()

#allows user to see the data base results provided the user knows the password which is call passwork
def dataBtpress():
    #asks for user password in termainal
    password = input ("Please enter password:")
    #checks if password is right
    if password == "password":  
        #selects everything from the database to be printed
        cursor.execute('SELECT * FROM Feedback')
        values = cursor.fetchall()
        #prints the database information while labeling what each type of information is 
        for row in values:
                print("Name:", row[0], "Email:", row[1], "Feedback:", row[2])
    else:
         print("Incorrect Password")
            
#creates the window, title, size and scaling 
root = Tk()
root.title ("Friday Prject 8")
root.geometry('400x250')
root.tk.call('tk','scaling', 2)

#########
#labels
#########

#creates the name label and selects the grid location of the label
nameLabel= Label(root, text ="Name:")
nameLabel.grid(column=0, row= 0)

#creates the email label and selects the grid location of the label which is right below the name label
emailLabel = Label(root, text = "Email:")
emailLabel.grid(column= 0, row=1)

#creates the feedback label and selects the grid location of the label which is right below the email label
feedbackLabel = Label(root,text = "Feedback:")
feedbackLabel.grid(column=0, row=2)

#########
#entries
#########

#creates the name entry box which is next to the name label and is sent to feedbackBtpress to be added to the database
nameEntry = Entry(root)
nameEntry.grid(column=1, row=0)

#creates the email entry box which is next to the email label and is sent to feedbackBtpress to be added to the database
emailEntry = Entry(root)
emailEntry.grid(column=1, row= 1)

#creates the feedback entry box which is next to the feedback label and is sent to feedbackBtpress to be added to the database
feedbackEntry = Entry(root)
feedbackEntry.grid(column= 1, row= 2)

#########
#buttons
#########

#creates submit feedback put that when it is pressed sends everything to be inserted and downloaded to the database
feedbackBt= Button(root, text= "Submit Feedback", command= feedbackBtpress)
feedbackBt.grid(column=1, row=3)

#allows user to attempt to view the data base provided that they know the password
dataBt= Button(root, text= "Print Current Data", command= dataBtpress)
dataBt.grid(column=1, row=4)

root.mainloop()

