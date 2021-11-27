import sqlite3

#Contains all the processes that handle data in the lessons table of the database
class Lesson_Database:
    def __init__(self):
        self.Database_Name = 'Tuition centre database.db'    #Locates the name of the database - keep in the same file as the python programs
        self.OpenDB()
        self.cursor = self.thecursor    #Changes the name of the cursor so that it does not clash with the original name

    #Opens the database, allowing it to be edited
    def OpenDB(self):
        self.conn = sqlite3.connect(self.Database_Name)    #Establishes a link between the program and the database
        self.thecursor = self.conn.cursor()    #Defines the cursor, which is the position of the database the program is at

    #Closes the database, which saves the data in the database
    def CloseDB(self):
        self.conn.close()

    #Gets the position of the cursor at the current moment in time
    def Get_Cursor(self):
        return self.cursor

    #Changes the contents of one of the lessons in the database
    def Update_Lesson(self, Lesson_Detail, Lesson_ID):
        Lesson_Detail.append(Lesson_ID)
        #Creates a SQL command to be used - this one in particular changes the data in a table
        SQL_Script = 'update {tn} set Subject = ?, Education_Level = ?, Day_Of_Week = ?, Time_Slot = ?, Status = ?, Student_Count = ?, Main_Tutor_ID = ?, Backup_Tutor_ID = ? where ID = ?'.format(tn = 'Lesson_Details')
        self.cursor.execute(SQL_Script, Student_Detail)    #Loads the command to be executed
        self.conn.commit()    #Confirms the command can be executed and hence executes the command - this change is irreversible

    #Selects all the data from the database and organises it into a list of dictionaries - this makes it much easier to handle data
    def Select_Lessons(self):
        SQL_Script = 'select * from Lesson_Details'    #Creates a SQL command that Selects all the data from the database table
        self.cursor.execute(SQL_Script)    #Loads up command to execute
        self.conn.commit()    #Executes command

        All_Rows = self.cursor.fetchall()     #Brings all the selected data (should be all the data in the table) into the program itself
        Lesson_Info = []
        for Row in All_Rows:
            #Creates a dictionary to store all the information about each lesson seperately
            Lesson_Detail = {"ID" : Row[0],
                             "Subject" : Row[1],
                             "Education_Level" : Row[2],
                             "Day_Of_Week" : Row[3],
                             "Time_Slot" : Row[4],
                             "Status" : Row[5],
                             "Student_Count" : Row[6],
                             "Main_Tutor_ID" : Row[7],
                             "Backup_Tutor_ID" : Row[8]
                }
            Lesson_Info.append(Lesson_Detail)    #Adds the dictionary to the list

        return Lesson_Info    #Brings back the list to the program

