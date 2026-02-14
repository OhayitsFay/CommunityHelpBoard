# Overview

I built this software to strengthen my understanding of how real applications interact with relational databases. As a software engineer, it is important for me to know not just how to write SQL queries, but how to connect a database to a working program, send commands to it, and use the returned data meaningfully.

This project is a command line application called Community Help Board. It allows users to create, view, update, delete, and filter community posts that are stored in a SQL relational database. When the program runs, users interact with a menu, and their choices determine what data is written to or read from the database. All data is stored persistently using SQLite, so information is saved even after the program is closed.

# Purpose
My purpose for writing this software was to gain hands on experience with SQL relational databases and understand how database operations work in a real program. I wanted to practice building SQL commands in code, executing them, and handling the results properly instead of working with SQL in isolation.

[\[Software Demo Video\]](https://youtu.be/6Sxf8DrreYw)

# Relational Database

This project uses SQLite, a lightweight relational database that stores data in a local file. SQLite is well suited for small applications and learning purposes because it does not require a separate server setup.

The relational database contains one main table called posts.
The structure of the table includes:

id – an integer primary key that uniquely identifies each post

title – text field for the post title

description – text field for the post content

category – text field describing the type of post

date_posted – text field storing the date the post was created

This table supports inserting new records, updating existing records, deleting records, and querying data, including filtering posts by a date range.

# Development Environment

This software was developed using Visual Studio Code as the code editor and a terminal for running and testing the program. GitHub was used for version control and publishing the project.

The programming language used is Python, along with the built in sqlite3 library to interact with the SQLite database. This library was used to create the database, execute SQL commands, and retrieve results directly within the Python program.

# Useful Websites

SQLite Documentation - https://www.sqlite.org/docs.html
Python sqlite3 Library - https://docs.python.org/3/library/sqlite3.html
W3Schools SQL Tutorial - https://www.w3schools.com/sql/
Python Official Documentation - https://docs.python.org/3/

# Future Work

- Add user authentication so posts can be tied to specific users

- Improve input validation and error handling

- Add more tables and relationships to expand the database