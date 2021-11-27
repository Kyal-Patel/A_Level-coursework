import sqlite3

#Contains all the processes that handle data in the students table of the database
class Student_Database:

    def __init__(self):
        self.database_name = 'Tuition centre database.db'    #Locates the name of the database - keep in the same file as the python programs
        self.opendb()
        self.cursor = self.thecursor    #Changes the name of the cursor so that it does not clash with the original name

    #Opens the database, allowing it to be edited
    def opendb(self):
        self.conn = sqlite3.connect(self.database_name)    #Establishes a link between the program and the database
        self.thecursor = self.conn.cursor()    #Defines the cursor, which is the position of the database the program is at

    #Closes the database, which ends the connection between the program and the database
    def closedb(self):
        self.conn.close()

    #Gets the position of the cursor at the current moment in time
    def getcursor(self):
        return self.cursor()

    #Adds a student record into the database
    def Insert_Student(self, Student_Detail):
        #Creates a SQL command to be used - this one in particular adds a student record to the database table
        sql_script = 'insert into Student_Details (First_Name, Last_Name, DOB, First_Subject, Second_Subject, School_Year, Main_Travel_Method, Allergies, Medical_Conditions, Address1, Address2, Postcode, Parent_First_Name, Parent_Last_Name, Parent_Phone_Number, Parent_Email_Address) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        self.cursor.execute(sql_script, Student_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Updates a student record in the database
    def Update_Student(self, Student_Detail, Student_ID):
        Student_Detail.append(Student_ID)    #Adds the student's ID at the end - this is the primary key used to search through the database
        #Creates a SQL command to be used - this one in particular replaces the record with the specified ID with new data
        sql_script = 'update {tn} set First_Name = ?, Last_Name = ?, DOB = ?, First_Subject = ?, Second_Subject = ?, School_Year = ?, Main_travel_Method = ?, Allergies = ?, Medical_Conditions = ?, Address1 = ?, Address2 = ?, Postcode = ?, Parent_First_Name = ?, Parent_Last_Name = ?, Parent_Phone_Number = ?, Parent_Email_Address = ? where ID = ?'.format(tn = 'Student_Details')
        self.cursor.execute(sql_script, Student_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Deletes a student from the student database
    def Delete_Student(self, Student_ID):
        Student_Detail = [Student_ID]
        SQL_Script = 'delete from {tn} where ID = ?'.format(tn = "Student_Details")    #Creates a SQL command to be used - this one in particular deletes the student record with the specified ID
        self.cursor.execute(SQL_Script, Student_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Retrieves all the student records from the database
    def Select_Students(self):
        sql_script = 'select * from Student_Details'    #Creates a SQL command to select the entire table
        self.cursor.execute(sql_script)
        self.conn.commit()
        All_Rows = self.cursor.fetchall()    #Retrieves all the selected data from the database - this will be the entire table

        Student_Info = []
        for Row in All_Rows:
            #Creates a dictionary to store all the information about each student seperately
            Student_Detail = {"ID" : Row[0],
                              "First_Name" : Row[1],
                              "Last_Name" : Row[2],
                              "DOB" : Row[3],
                              "First_Subject" : Row[4],
                              "Second_Subject" : Row[5],
                              "School_Year" : Row[6],
                              "Main_Travel_Method" : Row[7],
                              "Allergies" : Row[8],
                              "Medical_Conditions" : Row[9],
                              "Address1" : Row[10],
                              "Address2" : Row[11],
                              "Postcode" : Row[12],
                              "Parent_First_Name" : Row[13],
                              "Parent_Last_Name" : Row[14],
                              "Parent_Phone_Number" : Row[15],
                              "Parent_Email_Address" : Row[16]
                }
            Student_Info.append(Student_Detail)    #Adds the dictionary to the list

        print(Student_Info)
        return Student_Info    #Brings back the list to the program

sd = Student_Database()
sd.Select_Students()
