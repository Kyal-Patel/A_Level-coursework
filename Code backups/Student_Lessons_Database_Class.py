import sqlite3

#Contains all the processes that handle data in the student lessons table of the database (thetable that links student ID and Class ID together)
class Student_Lesson_Database:
    def __init__(self):
        self.Database_Name = 'Tuition centre database.db'    #Locates the name of the database - keep in the same file as the python programs
        self.OpenDB()
        self.cursor = self.thecursor    #Changes the name of the cursor so that it does not clash with the original name

    #Opens the database, allowing it to be edited
    def OpenDB(self):
        self.conn = sqlite3.connect(self.Database_Name)   #Establishes a link between the program and the database
        self.thecursor = self.conn.cursor()    #Defines the cursor, which is the position of the database the program is at

    #Closes the database, which saves the data in the database
    def CloseDB(self):
        self.conn.close()

    #Gets the position of the cursor at the current moment in time
    def getcursor(self):
        return self.cursor()

    #Adds a StudentID-ClassID combination into the database table
    def Insert_Student_Lesson(self, Student_Lesson_Detail):
        #Creates a SQL command to be used - this one in particular adds a StudentID-ClassID combination to the database table
        SQL_Script = 'insert into Student_Lessons (Student_ID, Class_ID) values(?,?)'
        self.cursor.execute(SQL_Script, Student_Lesson_Detail)    #Loads the command to be executed
        self.conn.commit()   #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Deletes a StudentID-ClassID combination from the student database
    def Delete_Student_Lesson(self, Student_Lesson_ID):
        Student__Lesson_Detail = [Student_Lesson_ID]
        SQL_Script = 'delete from Student_Lessons where ID = ?'    #Creates a SQL command to be used - this one in particular deletes the record with the specified ID
        self.cursor.execute(SQL_Script, Student_Lesson_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Retrieves all the student records from the database
    def Select_Student_Lessons(self):
        SQL_Script = 'select* from Student_Lessons'    #Creates a SQL command to select the entire table
        self.cursor.execute(SQL_Script)
        self.conn.commit()
        All_Rows = self.cursor.fetchall()    #Retrieves all the selected data from the database - this will be the entire table

        Student_Lesson_Info = []
        for Row in All_Rows:
            #Creates a dictionary to store all the information about each StudentID-ClassID combination seperately
            Student_Lesson_Detail = {"ID" : Row[2],
                                     "Student_ID" : Row[0],
                                     "Class_ID" : Row[1]
                }

            Student_Lesson_Info.append(Student_Lesson_Detail)    #Adds the dictionary to the list

        return Student_Lesson_Info    #Brings back the list to the program
