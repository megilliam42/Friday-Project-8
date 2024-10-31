# Friday-Project-8
Friday Project 8 for DS 3850

This program allows the user to enter feedback including name, email, and feedback using GUI and then allows the user to display the data base information

Friday Project 8: Customer Feedback
Application
Overview
For this assignment, you will create a simple customer feedback application
that combines a database with a graphical user interface (GUI). This
application will allow customers to submit their name, email, and feedback,
which will be stored in a database. Additionally, you'll implement a feature to
retrieve and display all feedback entries in the console, with an added layer
of password protection to ensure data privacy. This assignment will help you
practice database management, GUI design, and security principles in
application development.
Requirements
1. Database Creation for Customer Feedback
o Create a database file to store customer feedback.
o Each entry should include the customer’s name, email, and
feedback message.
2. GUI Design
o Design a graphical user interface (GUI) that customers can
interact with.
o The GUI should have input fields for the customer’s name, email,
and feedback.
o Add a Submit button that allows customers to submit their
information, which should then be stored in the database.
3. Password-Protected Data Retrieval
o Implement a button within the application that will print all
entries in the database to the console.
o For security, require a password before displaying the data (this
can be typed into the console).
o Prompt the user in the console for the password. If the password
is correct, print all data; if incorrect, deny access.
o Note that the password would be a great thing to include in the
readme file!
High-Level Instructions
1. Set Up the Database:
o Use a simple database file (like SQLite) to store the customer
data.
o Ensure that each entry includes fields for the name, email, and
feedback.
2. Create the GUI:
o Use a library (e.g., Tkinter for Python) to build a GUI with input
fields for the name, email, and feedback.
o Add a "Submit" button that, when clicked, stores the input data
into the database.
3. Data Retrieval with Security:
o Implement a "Retrieve Data" button within the GUI.
o When clicked, prompt the user in the console for a password. If
the password is correct, retrieve and print all data entries to the
console. If not, display an error message.
Additional Tips
 Database: SQLite is a good choice for a lightweight database and is
relatively easy to set up.
 GUI Library: Tkinter (Python) is recommended for creating the
interface.
 Password Prompt: You can keep the password hardcoded for
simplicity, or allow students to set it at runtime.