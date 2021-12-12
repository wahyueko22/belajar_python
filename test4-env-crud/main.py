from config.db_config import con
from config.db_connection import *
from query_db import *

def main():
    print ("hello world")

def choice():
    print ("1. Create Table")
    print ("2. Insert Data")
    print ("3. Read Data")
    print ("4. Update Data")
    print ("5. Delete Data")
    print ("6. Quit")

    ch = input("Enter Your Choice : ")
    if ch == '1':
        createTable(con)
        choice()
    elif ch == '2':
        insertTable(con)
        choice()
    elif ch == '3':
        retrieveTable(con)
        choice()
    elif ch == 4:
        updateRow(con)
        choice()
    elif ch == 5:
        deleteRow(con)
        choice()
    elif ch == 6:
        exit()
        pass
    else:
        print ("Please Enter Valid Input")

if __name__ == "__main__":
    choice()

