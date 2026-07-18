# 🏦 Demo Banking Enterprise

A simple command-line banking system built using Python. It tries to simulate basic banking features like creating accounts, depositing/withdrawing money, and keeping simple transaction records.

This project was mainly done while learning Python, especially OOP, file handling, and how data can be stored using CSV files with Pandas.

It’s not a real banking system or anything production level, just a learning project to understand how things work.



## Features

* Create a new bank account
* Auto-generated User ID
* Password confirmation during signup
* Basic login system (User ID + password)
* Deposit money
* Withdraw money (with balance check)
* Simple receipt generation after transactions
* Data saved using CSV files

## Technologies Used

* Python
* Pandas
* OOP (classes, basic encapsulation)
* CSV file handling

## Project Structure

Banking_soft/

├── Main.py              # main program  
├── User.txt             # stores user IDs  
├── Password.csv         # stores passwords  
├── everyuser_data.csv   # stores user info + balance  
├── Recipt.csv           # stores transaction history  
└── README.md  

---

## How It Works

### Account Creation

User enters name and location.  
Then system generates a random 4-digit user ID.

User has to set a password (with confirmation).

Account starts with a default balance of 100 (just for testing).

All data is saved into CSV files.


### Login

User logs in using:
* User ID
* Password

If both match, user can access banking options.


### Banking Operations

After login:
* Deposit money into account
* Withdraw money (checks balance first)
* View updated balance

Each transaction updates CSV files and also creates a receipt entry.


## Receipt Details

Each transaction record includes:

* Receipt number
* User ID
* Type (deposit/withdraw)
* Amount
* Previous balance
* New balance
* Date and time


## What I Learned

This project helped me understand:

* How classes actually work in real programs
* Basic file handling in Python
* How CSV files can act like a simple database
* Simple authentication logic
* How to structure a small project
* How messy real data handling can get lol


## Limitations

This is obviously not secure or production ready.

Some limitations:

* Passwords are stored as plain text (no hashing)
* No encryption at all
* No database used (only CSV files)
* No multi-user / concurrency handling
* Input validation is pretty basic


## Future Improvements (if I continue this)

* Add password hashing (bcrypt or hashlib)
* Move from CSV to SQLite or PostgreSQL
* Add better login session handling
* Add transaction history viewer
* Maybe add admin/user roles
* Improve error handling (lots of edge cases still missing)

## How to Run

Run this command:

python Main.py

Make sure these files are in the same folder:
* User.txt
* Password.csv
* everyuser_data.csv
* Recipt.csv


## Author

Dino Ranjit

Made while learning Python and trying to understand how basic systems like banking apps actually work behind the scenes.



## Note

This is just a learning project. If you see mistakes or bad design choices, feel free to suggest improvements.
