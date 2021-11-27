from tkinter import *
from Helper_Class import *
from Student_Database_Class import *

#Collects the data needed for the Helper_Class to create a visual table for the student data table in the database
class Student_Data_Viewer:
    def __init__(self):
        self.hp = Helper()
        self.sd = Student_Database()

        self.View_Student_Data = Tk()    #Creates a new Tkinter screen
        self.Size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.View_Student_Data)
        self.View_Student_Data.title("Viewing Student database")    #Gives the screen a title
        self.View_Student_Data.geometry(self.Size)    #Changes the size of the screen
        self.View_Student_Data.config(bg = self.hp.Find_Colour("Light Blue"))    #Changes the background colour of the screen
        Title_Frame = self.hp.Create_Title_Frame(self.View_Student_Data, self.Screen_Width, self.Screen_Height)    #Creates the title bar at the top of the screen
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Viewing Student database")    #Adds the title to the title bar
        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.View_Student_Data)    #Adds a back button to the screen

        self.Viewing_Student_Database()
        self.View_Student_Data.mainloop()

    #Collects the data in the database
    def Viewing_Student_Database(self):
        Student_List = self.sd.Select_Students()    #Collects all the data in the database table (This will be in the format of a list of dictionaries)

        #Creates blank lists for the data fields in the student table - if extra fields are added to the students table in the database then add a blank list for it below
        Name_List = []
        DOB_List = []
        School_Year_List = []
        First_Subject_List = []
        Second_Subject_List = []
        Main_Travel_Method_List = []
        Allergies_List = []
        Medical_Conditions_List = []
        Address_List = []
        Parent_Name_List = []
        Parent_Phone_Number_List = []
        Parent_Email_Address_List = []

        Rows = 0
        Columns = 0
        #Calculates the number of rows based on the number of students
        for Student in Student_List:
            Rows += 1


            #Takes each of the students' details and adds them to each of the lists created above - if extra fields are added to the students table in the database then add a section here like below

            #Collects first and last names together, then adds them to the lists
            First_Name = Student.get("First_Name","none")
            Last_Name = Student.get("Last_Name", "none")
            Name = First_Name + " " + Last_Name
            Name_List.append([Name])

            #General cases - if data field needs no modifications from the table to be used visually then each piece of data is extracted from the list of dictionaries and added to the lists created above
            DOB_List.append([Student.get("DOB", "none")])
            School_Year_List.append([Student.get("School_Year", "none")])
            First_Subject_List.append([Student.get("First_Subject", "none")])
            Second_Subject_List.append([Student.get("Second_Subject", "none")])
            Main_Travel_Method_List.append([Student.get("Main_Travel_Method", "none")])
            Allergies_List.append([Student.get("Allergies", "none")])
            Medical_Conditions_List.append([Student.get("Medical_Conditions", "none")])

            #Collects all parts of the address together to use in the visual table
            Address1 = Student.get("Address1", "none")
            Address2 = Student.get("Address2", "none")
            Postcode = Student.get("Postcode", "none")
            Address1 = Address1.split(",")
            House_Number = Address1[0]
            Road_Name = Address1[1]
            Address2 = Address2.split(",")
            Borough = Address2[0]
            County = Address2[1]
            Address = House_Number + " " + Road_Name + ", " + Borough + ", " + County + ", " + Postcode
            Address_List.append([Address])

            #A few more general cases
            Parent_First_Name = Student.get("Parent_First_Name", "none")
            Parent_Last_Name = Student.get("Parent_Last_Name", "none")
            Parent_Name = Parent_First_Name + " " + Parent_Last_Name
            Parent_Name_List.append([Parent_Name])
            Parent_Phone_Number_List.append([Student.get("Parent_Phone_Number", "none")])
            Parent_Email_Address_List.append([Student.get("Parent_Email_Address", "none")])
            

        #Creates a list of headings for the table to be created - if extra fields are added then add the heading for that data field here
        Headings = ["Student Name", "DOB", "School Year", "First Subject", "Second Subject", "Main Travel Method", "Allergies", "Medical Conditions", "Address", "Parent's Name", "Parent's Phone Number", "Parent's Email Address"]
        #Calculates the number of columns based on the number of headings
        for Heading in Headings:
            Columns += 1
        #Collects all the data extracted and organised into a single 2D list - if extra fields are added to the students table in the database then add the field at the end of the list
        Data = [Name_List, DOB_List, School_Year_List, First_Subject_List, Second_Subject_List, Main_Travel_Method_List, Allergies_List, Medical_Conditions_List, Address_List, Parent_Name_List, Parent_Phone_Number_List, Parent_Email_Address_List]
        #Calls the function that draws and adds data to the on-screen table - change the 200 (row spacing) if there is data overlapping
        self.hp.Draw_Canvas(self.View_Student_Data, self.Screen_Width, self.Screen_Height, Columns, Rows, 200, Headings, Data)

        print(Headings)
        print(Data)


sdv = Student_Data_Viewer()
