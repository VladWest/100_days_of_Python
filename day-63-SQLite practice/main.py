import sqlite3

# Create a connection to a new database (if the database does not exist then it will be created).
db = sqlite3.connect("books-collection.db")
# Creating a cursor which will control our database.
cursor = db.cursor()
# Creating a table named 'books' insight early created DB
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE,"
               " author varchar(250) NOT NULL,"
               " rating FLOAT NOT NULL)")
# adding data to our table
# This will create a new entry in our books table for the Harry Potter book and commit the changes to our database
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()




