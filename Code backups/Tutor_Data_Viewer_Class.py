from tkinter import *
from Helper_Class import *
from Tutor_Database_Class import *

#Collects the data needed for the Helper_Class to create a visual table for the tutors data table in the database
class Tutor_Data_Viewer:
    def __init__(self):
        self.hp = Helper()
        self.td = Tutor_Database()

        self.View_Tutor_Data = Tk()
        self.Size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.View_Tutor_Data)
        self.View_Tutor_Data.title("Viewing tutor database")
        self.View_Tutor_Data.geometry(self.Size)
        self.View_Tutor_Data.config(bg = self.hp.Find_Colour("Light Blue"))
        Title_Frame = self.hp.Create_Title_Frame(self.View_Tutor_Data, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Viewing tutor database")
        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.View_Tutor_Data)

        self.Viewing_Tutor_Database()
        self.View_Tutor_Data.mainloop()

    #Collects the data in the database
    def Viewing_Tutor_Database(self):
        Tutor_List = self.td.Select_Tutors()    #Collects all the data in the database table (This will be in the format of a list of dictionaries)

        #Creates blank lists for the data fields in the student table - if extra fields are added to the students table in the database then add a blank list for it below
        Name_List = []
        DOB_List = []
        Status_List = []
        Primary_Subject_List = []
        Secondary_Subject_List = []
        Phone_Number_List = []
        Email_Address_List = []
        Allergies_List = []
        Medical_Conditions_List = []
        Address_List = []
        Username_List = []
        Password_List = []

        Rows = 0
        Columns = 0
        #Calculates the number of rows based on the number of students
        for Tutor in Tutor_List:
            Rows += 1

            #Takes each of the students' details and adds them to each of the lists created above - if extra fields are added to the students table in the database then add a section here like below

            #Collects first and last names together, then adds them to the lists
            First_Name = Tutor.get("First_Name", "none")
            Last_Name = Tutor.get("Last_Name", "none")
            Name = First_Name + " " + Last_Name
            Name_List.append([Name])

            #General cases - if data field needs no modifications from the table to be used visually then each piece of data is extracted from the list of dictionaries and added to the lists created above
            DOB_List.append([Tutor.get("DOB", "none")])
            Status_List.append([Tutor.get("Status", "none")])
            Primary_Subject_List.append([Tutor.get("Primary_Subject", "none")])
            Secondary_Subject_List.append([Tutor.get("Secondary_Subject", "none")])
            Phone_Number_List.append([Tutor.get("Phone_Number", "none")])
            Email_Address_List.append([Tutor.get("Email_Address", "none")])
            Allergies_List.append([Tutor.get("Allergies", "none")])
            Medical_Conditions_List.append([Tutor.get("Medical_Conditions", "none")])

            #Collects all parts of the address together to use in the visual table
            Address1 = Tutor.get("Address1", "none")
            Address2 = Tutor.get("Address2", "none")
            Postcode = Tutor.get("Postcode", "none")
            Address1 = Address1.split(",")
            House_Number = Address1[0]
            Road_Name = Address1[1]
            Address2 = Address2.split(",")
            Borough = Address2[0]
            County = Address2[1]
            Address = House_Number + " " + Road_Name + ", " + Borough + ", " + County + ", " + Postcode
            Address_List.append([Address])

            #A couple more general cases
            Username_List.append([Tutor.get("Username", "none")])
            Password_List.append([Tutor.get("Password", "none")])


        #Collects all the data extracted and organised into a single 2D list - if extra fields are added to the students table in the database then add the field at the end of the list
        Data = [Name_List, DOB_List, Status_List, Primary_Subject_List, Secondary_Subject_List, Phone_Number_List, Email_Address_List, Allergies_List, Medical_Conditions_List, Address_List, Username_List, Password_List]
        #Creates a list of headings for the table to be created - if extra fields are added then add the heading for that data field here
        Headings = ["Name", "DOB", "Status", "Primary Subject", "Secondary Subject", "Phone Number", "Email Address", "Allergies", "Medical Conditions", "Address", "Username", "Password"]
        #Calculates the number of columns based on the number of headings
        for Heading in Headings:
            Columns += 1
        #Calls the function that draws and adds data to the on-screen table - change the 200 (row spacing) if there is data overlapping when the table has loaded
        self.hp.Draw_Canvas(self.View_Tutor_Data, self.Screen_Width, self.Screen_Height, Columns, Rows, 200, Headings, Data)
        
tdv = Tutor_Data_Viewer()
