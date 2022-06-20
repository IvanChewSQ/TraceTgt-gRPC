
import mysql.connector as connector

class DBHelper:

    """
    Creation of database and schema
        nric varchar(9)
        name varchar(50)
        location varchar(50)
        time varchar(20)
        status Boolean
    """
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='Mobile@97701',
                                    database='python_test',
                                    auth_plugin= 'mysql_native_password')  
        query = 'create table if not exists new_users (nric varchar(9) check (^[STFG]\d{7}[A-Z]$) primary key, name varchar(50), location varchar(50), time varchar(50), status boolean)'
        cur = self.con.cursor()
        if (cur.execute(query) == True):
            print('Database connect Sucessfully')
        else:
            print('Wrong input details, please try again')


    """
    Insert Users Record to database
        nric, name, location, time
    """
    def insert_user(self, nric, name, location, time):
        query = "insert into new_users(nric, name, location, time) values('{}','{}','{}', '{}')".format(
            nric, name, location, time)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        if (self.con.commit() == True):
            print("Your data is saved on db sucessfully")
        else:
            print('Wrong input details, please try again')

    """
    Update Users Record to database
        nric, name, location, time
    """
    def update_user(self, userId, newName, newPassword):
        query = "update new_users set userName='{}',phone='{}' where userId={}".format(
            newName, newPassword, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    
    # Fetch History based on NRIC
    def fetch_history(self, nric):
        query = "select location from new_users where nric= {}".format(nric)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name :", row[1])
            print("User Password : ", row[2])
            print()
            print()

    # Fetch All Users based on Location
    def fetch_history(self):
        query = "select * from new_users"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name :", row[1])
            print("User Password : ", row[2])
            print()
            print()
