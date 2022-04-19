from tkinter import *
from Helper_Class import *
from Lesson_Database_Class import *
from Tutor_Database_Class import *
from Student_Database_Class import *
from Student_Lessons_Database_Class import *
from datetime import *

#Collects the data needed for the Helper_Class to create a visual table for the tutor rota - it uses the canvas from Helper_Class() to create a table with data for the tutor's lesson plan
class Tutor_Rota_Viewer:
    def __init__(self, Choice, Tutor_Name):
        self.hp = Helper()
        self.ld = Lesson_Database()
        self.td = Tutor_Database()
        self.sd = Student_Database()
        self.sld= Student_Lesson_Database()
        self.Tutor_Name = Tutor_Name
        self.Choice = Choice    #Choice will be used to decide whether the weekly or daily rota will be shown

        #Retreives the tutor's data from the database and extracts the ID of the tutor - this will be used to organise data later
        Tutor_List = self.td.Select_Tutors()
        for Tutor in Tutor_List:
                First_Name = str(Tutor.get("First_Name", "none"))
                Last_Name = str(Tutor.get("Last_Name", "none"))
                Name = First_Name + " " + Last_Name
                if Name == self.Tutor_Name:
                    Tutor_ID = str(Tutor.get("ID", "none"))
                    break

        Lesson_List = self.ld.Select_Lessons()    #Retrieves all the information from the lessons table in the database
        self.Tutor_Lessons = []
        #Searches through each lesson to find the lessons that have the matching tutor ID
        for Lesson in Lesson_List:
            Main_Tutor_ID = str(Lesson.get("Main_Tutor_ID", "none"))
            Backup_Tutor_ID = str(Lesson.get("Backup_Tutor_ID", "none"))

            #Collects the lessons that have the tutor as part of it, and seperates them based on whether the tutor is the main or backup for the lesson
            if Main_Tutor_ID == Tutor_ID:
                self.Tutor_Lessons.append([Lesson ,"Main tutor"])
            elif Backup_Tutor_ID == Tutor_ID:
                self.Tutor_Lessons.append([Lesson, "Backup tutor"])


        self.View_Rota = Tk()    #Creates a blank Tkinter screen called View_Lesson_Plan. The self. allows the screen to be called throughout the class
        self.Title = "Viewing " + Tutor_Name + "'s rota"    #Creates a title for the screen
        self.Size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.View_Rota)    #Finds the necessary dimensions of the screen by calling a function in the Helper_Class
        self.View_Rota.geometry(self.Size)    #Resizes the screen to have the correct dimensions
        self.View_Rota.title(self.Title)    #Adds the title to the screen
        self.View_Rota.config(bg = self.hp.Find_Colour("Light Blue"))    #Changes the background colour
        #Adds a large visible title and back button
        Title_Frame = self.hp.Create_Title_Frame(self.View_Rota, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, self.Title)
        self.hp.Create_Back_Button(Title_Frame, self.View_Rota)

        #Branches the program based on if the tutor wants to view a daily or weekly rota
        if Choice == "View daily rota":
            Day_Sorted_Lessons = self.Sort_To_Days()    #Calls a function to filter lessons by day - the returned list will be used instead of the list created above
            self.Viewing_Rota(Day_Sorted_Lessons,Choice)
        elif Choice == "View weekly rota":
            self.Viewing_Rota(self.Tutor_Lessons,Choice)
        self.View_Rota.mainloop()

    #Filters lessons by day (if on Tuesday this button is pressed , then only Tuesday's lessons are shown)
    def Sort_To_Days(self):
        Today_Lessons = []
        Day_Of_Week_Today = date.weekday(date.today())    #Uses the datetime library to figure out what day of the week it is - returns an integer value
        #Converts the integer value to a day of the week
        if Day_Of_Week_Today == 0:
            Day_Of_Week_Today = "Monday"
        elif Day_Of_Week_Today == 1:
            Day_Of_Week_Today = "Tuesday"
        elif Day_Of_Week_Today == 2:
            Day_Of_Week_Today = "Wednesday"
        elif Day_Of_Week_Today == 3:
            Day_Of_Week_Today = "Thursday"
        elif Day_Of_Week_Today == 4:
            Day_Of_Week_Today = "Friday"
        elif Day_Of_Week_Today == 5:
            Day_Of_Week_Today = "Saturday"
        else:
            Day_Of_Week_Today = "Sunday"

        #Loops through each of the current set of lessons to find only those who occur in the day of the week it currently is
        for Lesson in self.Tutor_Lessons:
            Lesson_To_Check = Lesson[0]
            Day_Of_Week = str(Lesson_To_Check.get("Day_Of_Week", "none"))
            if Day_Of_Week == Day_Of_Week_Today:
                Today_Lessons.append(Lesson)

        return Today_Lessons



    #Does a multitude of actions to sort data, replace ID's with names and then display the data
    def Viewing_Rota(self, Lessons, Choice):
        #Creates blank lists for each data field - if extra fields are added to the lessons table in the database then add a new blank list here as appropriate
        Day_Of_Week_List = []
        Time_Slot_List = []
        Education_Level_List = []
        Subject_List = []
        Student_Names_List = []
        Tutor_Status_List = []

        self.Student_Lessons = self.sld.Select_Student_Lessons()


        #This section will group the students by class using the IDs in the Student_Lessons table - these will be converted to names later
        self.Class_ID_Groups = []    #Creates a blank list that will link the class ID with all the student IDs in that group
        for Student_Lesson in self.Student_Lessons:    #Loops through each record in the Student_Lesson table
            Student_Class_ID = Student_Lesson.get("Class_ID", "none")    #Takes out one of the key-value combinations in the dictionary
            Student_ID = Student_Lesson.get("Student_ID", "none")
            if self.Class_ID_Groups == []:    #Checks if the list is blank
                #If so, then the program creates a new blank dictionary and adds the first student to the "Student_ID_Group" key
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
                        for key in To_Check.keys():    #Loops through each key in the dictionary so that the right key can be found -
                                                       #this method needs to be used due to the way python recognises keys
                            if key == "Student_ID_List":
                                To_Check[key] = Student_ID_List    #Replaces the old list of student IDs with the updated list
                if not Class_ID_Found:    #Checks if the ID of the class the student is in has not matched with any of the classes currently in the list
                    self.Class_ID_Groups.append({"Class_ID" : Student_Class_ID,    #Adds a new class to the list of classes, as the student must be in a class not in the current list
                                            "Student_ID_Group" : [Student_ID]
                                            })



        Students = self.sd.Select_Students()
        Tutors = self.td.Select_Tutors()
        #Collects all the data for each lesson one at a time, then adds it to to the blank lists created at the beginning odf the function
        for Class in Lessons:
            Lesson = Class[0]
            #Collects all the data for each lesson - if extra fields are added to the lessons table in the database then add it to this section as well in the same format as the other lines
            Tutor_Status = Class[1]
            Tutor_Status_List.append([Tutor_Status])
            Day_Of_Week = Lesson.get("Day_Of_Week","none")
            Day_Of_Week_List.append([Day_Of_Week])
            Time_Slot = Lesson.get("Time_Slot","none")
            Time_Slot_List.append([Time_Slot])
            Education_Level = Lesson.get("Education_Level","none")
            Education_Level_List.append([Education_Level])
            Subject = Lesson.get("Subject", "none")
            Subject_List.append([Subject])

            #This section will add the groups of students created earlier to the rest of the data about each class in the right order - it adds a list of ID numbers for students
            Lesson_ID = Lesson.get("ID", "none")    #Takes out the ID key from the lesson dictionary
            ID_Group_Found = False    #A checking variable to make sure that a matching pair of IDs are found
            for Class in self.Class_ID_Groups:    #Loops through each lesson in the list of lessons
                Class_ID = Class.get("Class_ID", "none")    #Gets the ID of the Class currently being checked throughy
                if Class_ID == Lesson_ID:    #Checks for a matching pair of ID numbers
                    Student_ID_Group = Class.get("Student_ID_Group", "none")    #Takes out the group of students from the class to be found to have the matching pair
                    Lesson["Student_ID_Group"] = Student_ID_Group    #Adds the group of students to the record
                    ID_Group_Found = True    #Confirms that a matching pair was found
            if ID_Group_Found == False:    #Occurs if there are no students currently that are booked for that lesson
                Lesson["Student_ID_Group"] = []    #Adds a blank list to signify that there are no students



            Student_ID_List = Lesson.get("Student_ID_Group", "none")
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
                Student_Names_List.append(["none"])    #Tells the program there are no students in the lesson currently being looked at, so adds a blank in that position in the list to keep the order
            else:
                Student_Names_List.append(Found_Students)    #Moves the list of students from the temporary list to the permanent list

        Rows = 0
        for Class in Lessons:    #Calculates the number of rows of data in the table (number of records)
            Rows += 1

        if Choice == "View daily rota":
            #Collects all the data extracted and organised into a single 2D list - - if extra fields are added to the lessons table in the database then add the field at the end of the list
            Data = [Subject_List, Time_Slot_List, Education_Level_List, Student_Names_List, Tutor_Status_List]
            Headings = ["Subject", "Time slot", "Education level", "Students in lesson", "Main or backup?"]    #Creates a list of headings - if extra fields are added to the lessons table in the database then add title here as appropriate
        else:
            #Collects all the data extracted and organised into a single 2D list - - if extra fields are added to the lessons table in the database then add the field at the end of the list
            Data = [Subject_List, Time_Slot_List, Day_Of_Week_List, Education_Level_List, Student_Names_List, Tutor_Status_List]
            Headings = ["Subject", "Time slot", "Day of week", "Education level", "Students in lesson", "Main or backup?"]    #Creates a list of headings - if extra fields are added to the lessons table in the database then add title here as appropriate

        Columns = 0
        for Heading in Headings:    #Calculates the number of headings in the table (number of data fields)
            Columns += 1

        #Calls the function that draws and adds data to the on-screen table - change the 70 (row spacing) if there is data overlapping
        self.hp.Draw_Canvas(self.View_Rota, self.Screen_Width, self.Screen_Height, Columns, Rows, 70, Headings, Data)






