import sqlite3

#Contains all the processes that handle data in the tutors table of the database
class Tutor_Database:

    def __init__(self):
        self.database_name = 'Tuition centre database.db'    #Locates the name of the database - keep in the same file as the python programs
        self.open_db()
        self.cursor = self.thecursor    #Changes the name of the cursor so that it does not clash with the original name

    #Opens the database, allowing it to be edited
    def open_db(self):
        self.conn = sqlite3.connect( self.database_name )    #Establishes a link between the program and the database
        self.thecursor=self.conn.cursor()    #Defines the cursor, which is the position of the database the program is at

    #Closes the database, which ends the connection between the program and the database
    def close_db(self):
        self.conn.close()

    #Gets the position of the cursor at the current moment in time
    def get_cursor(self):
        return self.cursor

    #Adds a tutor record into the database
    def Insert_Tutor(self, Tutor_Detail):
        #Creates a SQL command to be used - this one in particular adds a tutor record to the database table
        SQL_Script = 'insert into Tutor_Details (First_Name, Last_Name, DOB, Age, Primary_Subject, Secondary_Subject, Phone_Number, Email_Address,Allergies, Medical_Conditions, Address1, Address2, Postcode, Username, Password, Status) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        self.cursor.execute(SQL_Script, Tutor_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Updates a tutor record in the database
    def Update_Tutor(self, Tutor_Detail, Tutor_ID):
        Tutor_Detail.append(Tutor_ID)    #Adds the tutor's ID at the end - this is the primary key used to search through the database
        #Creates a SQL command to be used - this one in particular replaces the record with the specified ID with new data
        SQL_Script = 'update {tn} set First_Name=? , Last_Name=? , DOB=?, Age=?, Primary_Subject=? , Secondary_Subject=? , Phone_Number=?, Email_Address=? , Allergies=? , Medical_Conditions=? , Address1=? , Address2=? , Postcode=? , Username=? , Password=?, Status = ? where ID=?'.format(tn='Tutor_Details')
        self.cursor.execute(SQL_Script, Tutor_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Deletes a tutor from the tutor database
    def Delete_Tutor(self, Tutor_ID):
        Tutor_Detail = [Tutor_ID]
        SQL_Script = 'delete from {tn} where ID = ?'.format(tn = "Tutor_Details")     #Creates a SQL command to be used - this one in particular deletes the tutor record with the specified ID
        self.cursor.execute(SQL_Script, Tutor_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Retrieves all the tutor records from the database
    def Select_Tutors(self):
        SQL_Script = 'select * from Tutor_Details'    #Creates a SQL command to select the entire table
        self.cursor.execute(SQL_Script)
        self.conn.commit()

        all_rows = self.cursor.fetchall()    #Retrieves all the selected data from the database - this will be the entire table

        Tutor_Info = []
        for row in all_rows:#
            #Creates a dictionary to store all the information about each student seperately
            Tutor_Detail = {"ID" : row[0],
                            "First_Name" : row[1],
                            "Last_Name" : row[2],
                            "DOB" : row[3],
                            "Age" : row[4],
                            "Primary_Subject" : row[5],
                            "Secondary_Subject" : row[6],
                            "Phone_Number" : row[7],
                            "Email_Address" : row[8],
                            "Allergies" : row[9],
                            "Medical_Conditions" : row[10],
                            "Address1" : row[11],
                            "Address2" : row[12],
                            "Postcode" : row[13],
                            "Username" : row[14],
                            "Password" : row[15],
                            "Status" : row[16]}
            Tutor_Info.append(Tutor_Detail)    #Adds the dictionary to the list
        return Tutor_Info    #Brings back the list to the program

td = Tutor_Database()
td.Select_Tutors()
