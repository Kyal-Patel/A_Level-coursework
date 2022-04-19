from tkinter import *
#imports other python files needed for program to work: adjust names accordingly and keep all files in the same folder
from Helper_Class import *
from Lesson_Database_Class import *
from Student_Lessons_Database_Class import *
from Student_Database_Class import *
from Tutor_Database_Class import *

#Class currently uses the canvas from Helper_Class() to create a table with data for the overall lesson plan in the tuition centre
class Lesson_Plan_Management:
    def __init__(self):
        self.hp = Helper()
        self.ld = Lesson_Database()
        self.sld = Student_Lesson_Database()
        self.sd = Student_Database()
        self.td= Tutor_Database()

        self.View_Lesson_Plan = Tk()    #Creates a blank Tkinter screen called View_Lesson_Plan. The self. allows the screen to be called throughout the class
        self.View_Lesson_Plan.title("Lesson Plan")    #Replaces the default title of the screen to "Login"
        self.Size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.View_Lesson_Plan)    #obtains screen dimensions
        self.View_Lesson_Plan.geometry(self.Size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.View_Lesson_Plan.config(bg = self.hp.Find_Colour("Light Blue"))    #changes the colour of the Tkinter screen to light blue
        self.Collect_Data()    #Runs a function below
        self.View_Lesson_Plan_Screen()    #^
        self.View_Lesson_Plan.mainloop()    #Loops the code to create the screen, updaing the screen and keeping the widgets on the screen for as long as it is open

    #Collects the data from the lesson and student_lessons tables and formats it so it can be used later
    def Collect_Data(self):
        self.Lesson_List = self.ld.Select_Lessons()    #Retrieves all the data from the Lessons table
        self.Student_Lessons = self.sld.Select_Student_Lessons()    #Retreives all the data from the Student_Lessons table

        #This section will group the students by class using the IDs in the Student_Lessons table
        self.Class_ID_Groups = []    #Creates a blank list that will link the class ID with all the student IDs in that group
        for Student_Lesson in self.Student_Lessons:    #Loops through each record in the Student_Lesson table
            Student_Class_ID = Student_Lesson.get("Class_ID", "none")    #Takes out one of the key-value combinations in the dictionary
            Student_ID = Student_Lesson.get("Student_ID", "none")
            if self.Class_ID_Groups == []:    #Checks if the list is blank
                #Creates a new blank dictionary and adds the first student to the "Student_ID_Group" key
                self.Class_ID_Groups = [{"Class_ID" : Student_Class_ID,
                                    "Student_ID_Group" : [Student_ID]
                                    }]
            else:
                Class_ID_Found = False    #A checking variable to make sure that a matching pair of ID's are found
                for ID in range(len(self.Class_ID_Groups)):    #Loops through each class is the list
                    To_Check = self.Class_ID_Groups[ID]    #Takes out the individual class dictionary from the list of dictionaries
                    Class_ID = To_Check.get("Class_ID", "none")    #Takes out one of the key-value combinations in the dictionary
                    if Student_Class_ID == Class_ID:    #Checks if the ID of the class the student is in matches the ID of the class being looked at
                        Class_ID_Found = True    #As a matching pair has been found this reverts to true
                        Student_ID_List = To_Check.get("Student_ID_Group", "none")    #Takes out the list of students inside the dictionary
                        Student_ID_List.append(Student_ID)    #Adds the student's ID to the list
                        for key in To_Check.keys():    #Loops through each key in the dictionary so that the right key can be found
                            if key == "Student_ID_List":
                                To_Check[key] = Student_ID_List    #Replaces the old list of student IDs with the updated list
                if not Class_ID_Found:    #Checks if the ID of the class the student is in has not matched with any of the classes currently in the list
                    self.Class_ID_Groups.append({"Class_ID" : Student_Class_ID,    #Adds a new class to the list of classes
                                            "Student_ID_Group" : [Student_ID]
                                            })

        #This section will add the groups of students above to the rest of the data about each class in the right order
        for Lesson in self.Lesson_List:    #Loops through each lesson in the list of lessons
            Lesson_ID = Lesson.get("ID", "none")    #Takes out the ID key from the lesson dictionary
            ID_Group_Found = False    #A checking variable to make sure that a matching pair of IDs are found
            for Class in self.Class_ID_Groups:
                Class_ID = Class.get("Class_ID", "none")    #Gets the ID of the Class currently being checked through
                if Class_ID == Lesson_ID:    #Checks for a matching pair of ID numbers
                    Student_ID_Group = Class.get("Student_ID_Group", "none")    #Takes out the group of students from the class to be found to have the matching pair
                    Lesson["Student_ID_Group"] = Student_ID_Group    #Adds the group of students to the record
                    ID_Group_Found = True    #Confirms that a matching pair was found
            if ID_Group_Found == False:    #Occurs if there are no students currently that are booked for that lesson
                Lesson["Student_ID_Group"] = []    #Adds a blank list to signify that there are no students


    #Breaks up all the data so that it can be slotted into the table that will show up on the screen
    def View_Lesson_Plan_Screen(self):
        Title_Frame = self.hp.Create_Title_Frame(self.View_Lesson_Plan, self.Screen_Width, self.Screen_Height)    #Gives the Screen with the table in it a title
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "The weekly lesson plan")    #^

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.View_Lesson_Plan)    #Adds a back button onto the screen

        Headings = ["Subject", "Education level", "Student Names", "Day Of Week", "Time Slot", "Main Tutor Name", "Backup Tutor_Name"]    #Creates a list of headings - if extra fields are added to the lessons table in the database then add title here as appropriate
        Rows = 0
        Columns = 7    #If extra data fields are added increase this number as well

        for Lesson in self.Lesson_List:
            Rows += 1   #Calculates the number of rows of data in the table (number of records)

        #Creates blank lists for each data field - if extra fields are added to the lessons table in the database then add a new blank list here as appropriate
        Subjects= []
        Education_Levels = []
        Student_Names = []
        Day_Of_Weeks = []
        Time_Slots = []
        Main_Tutor_Names = []
        Backup_Tutor_Names = []

        Students = self.sd.Select_Students()    #Collects all the data from the students table
        Tutors = self.td.Select_Tutors()    #Collects all the data from the tutors table

        #Collects all the data for each lesson one at a time, then adds it to to the blank lists above

        for Lesson in self.Lesson_List:
            #Collects all the data for each lesson - if extra fields are added to the lessons table in the database then add it to this section as well in the same format as the other lines
            Subject = Lesson.get("Subject", "none")
            Education_Level = Lesson.get("Education_Level", "none")
            Student_ID_List = Lesson.get("Student_ID_Group", "none")
            Day_Of_Week = Lesson.get("Day_Of_Week", "none")
            Time_Slot = Lesson.get("Time_Slot", "none")
            Main_Tutor_ID_List = [Lesson.get("Main_Tutor_ID", "none")]
            Backup_Tutor_ID_List = [Lesson.get("Backup_Tutor_ID","none")]

            #Goes over any special conditions for data in the database (e.g: If data needs to be converted in order for it to be understandable and readable by the user) - add your own if necessary

            #Converts student IDs to names
            Found_Students = []    #Creates a temporary list for students
            ID_Match_Found = False    #A checking variable to make sure that there is at least one student in the lesson
            for Student in Students:
                Student_ID = Student.get("ID", "none")    #Gets each student ID in the students table
                for ID in Student_ID_List:
                    if Student_ID == ID:    #Compares the ID of the student currently being checked to each ID in the list of IDs created in the previous function: if True it means a match has been found
                        Student_First_Name = Student.get("First_Name", "none")
                        Student_Last_Name = Student.get("Last_Name", "none")
                        Student_Name = Student_First_Name + " " + Student_Last_Name
                        Found_Students.append(Student_Name)    #Adds the students' full name to the temporary list
                        ID_Match_Found = True    #Signifies a match has been made
            if ID_Match_Found == False:
                Student_Names.append(["none"])    #Tells the program there are no students in the lesson currently being looked at, so adds a blank in that position in the list to keep the order
            else:
                Student_Names.append(Found_Students)    #Moves the list of students from the temporary list to the permanent list
                

            #Converts tutor IDs to names
            Main_ID_Match_Found = False
            Backup_ID_Match_Found = False
            for Tutor in Tutors:
                #Gets items from two seperate lists: The main tutor and backup tutor list
                Main_Tutor_ID = Lesson.get("Main_Tutor_ID","none")
                Backup_Tutor_ID = Lesson.get("Backup_Tutor_ID","none")

                #Checks for main tutors in the lesson
                for ID in Main_Tutor_ID_List:
                    if Main_ID_Match_Found == False:
                        if Main_Tutor_ID == ID:
                            for Tutor in Tutors:
                                ID = Tutor.get("ID", "none")    #Gets each tutor ID from the tutors table
                                if ID == Main_Tutor_ID:    #Compares the ID of the tutor currently being checked to the list of main tutor IDs: if a match is found then this returns true
                                    Main_Tutor_First_Name = Tutor.get("First_Name", "none")
                                    Main_Tutor_Last_Name = Tutor.get("Last_Name", "none")
                                    Main_Tutor_Name = Main_Tutor_First_Name + " " + Main_Tutor_Last_Name
                                    Main_Tutor_Names.append([Main_Tutor_Name])    #Adds the tutors' full name to the Main_Tutor_Names list
                                    Main_ID_Match_Found = True    #Signifies a match has been found
                                    break    #Ends this particular loop as a match has been found

                #Checks for backup tutors in the lesson
                for ID in Backup_Tutor_ID_List:
                    if Backup_ID_Match_Found == False:
                        if Backup_Tutor_ID == ID:
                            for Tutor in Tutors:
                                ID = Tutor.get("ID", "none")    #Gets each tutor ID from the tutors table
                                if ID == Backup_Tutor_ID:    #Compares the ID of the tutor currently being checked to the list of main tutor IDs: if a match is found then this returns true
                                    Backup_Tutor_First_Name = Tutor.get("First_Name", "none")
                                    Backup_Tutor_Last_Name = Tutor.get("Last_Name", "none")
                                    Backup_Tutor_Name = Backup_Tutor_First_Name + " " + Backup_Tutor_Last_Name
                                    Backup_Tutor_Names.append([Backup_Tutor_Name])    #Adds the tutors' full name to the Backup_Tutor_Names list
                                    Backup_ID_Match_Found = True    #Signifies a match has been found
                                    break    #Ends this particular loop as a match has been found

            #Checks if either of the lists has ended up blank, if so then a blank is added in that position so that the order is kept consistent
            if Main_ID_Match_Found == False:
                Main_Tutor_Names.append(["none"])
            if Backup_ID_Match_Found == False:
                Backup_Tutor_Names.append(["none"])

            #Adds the rest of the data collected from that lesson to the new lists - if extra fields are added to the lessons table in the database that have no special conditions then follow the format of the lines below
            Subjects.append([Subject])
            Education_Levels.append([Education_Level])
            Day_Of_Weeks.append([Day_Of_Week])
            Time_Slots.append([Time_Slot])
            #Moves onto the next lesson in the table

        #Collects all the data extracted and organised into a single 2D list - - if extra fields are added to the lessons table in the database then add the field at the end of the list
        Data = [Subjects, Education_Levels, Student_Names, Day_Of_Weeks, Time_Slots, Main_Tutor_Names, Backup_Tutor_Names]
        #Calls the function that draws and adds data to the on-screen table - change the 70 (row spacing) if there is data overlapping
        Drawing_Canvas = self.hp.Draw_Canvas(self.View_Lesson_Plan, self.Screen_Width, self.Screen_Height, Columns ,Rows, 70, Headings, Data)
        
##lpm = Lesson_Plan_Management()
