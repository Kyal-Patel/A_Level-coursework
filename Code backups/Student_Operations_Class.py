from tkinter import *
from Helper_Class import *
from Student_Database_Class import *

#Handles any windows that occur after the admin presses "Manage student database" on the Admin_Main_Screen
class Student_Operations:
    def __init__(self):
        self.hp = Helper()
        self.sd = Student_Database()

        self.Manage_Student_Database_Navigation = Tk()    #Creates a new Tkinter screen called Manage_Student_Database_Navigation
        self.size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Manage_Student_Database_Navigation)    #obtains screen dimensions
        self.Manage_Student_Database_Navigation.geometry(self.size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.Manage_Student_Database_Navigation.title("Manage student database navigation")
        self.Manage_Student_Database_Navigation.config(background = self.hp.Find_Colour("Light Blue"))
        #Sets the position of the first and second columns - these will be used to place the entry boxes in some of the screens
        self.First_Column_Entry_Position = self.Screen_Width / 5
        self.Second_Column_Entry_Position = self.Screen_Width / 1.6

        self.Manage_Student_Database_Navigation_Screen()    #calls the function below
        self.Manage_Student_Database_Navigation.mainloop()    #Loops the code to create the screen, updaing the screen and keeping the widgets on the screen for as long as it is open

    #Adds widgets onto the first main screen created above
    def Manage_Student_Database_Navigation_Screen(self):
        Title_Frame = self.hp.Create_Title_Frame(self.Manage_Student_Database_Navigation, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Choose an option:")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.Manage_Student_Database_Navigation)

        Add_Student_Button = Button(self.Manage_Student_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Add a student", font = ("Helvetica",20), command = self.Student_Creation_Screen)
        Add_Student_Button.place(x = (self.Screen_Width / 8), y = (self.Screen_Height / 3), width = 250, height = 100)

        Edit_Student_Button = Button(self.Manage_Student_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Edit a student's data", font = ("Helvetica",20), wraplength = 200, command = self.Edit_Student_Data_Screen)
        Edit_Student_Button.place(x = (self.Screen_Width / 2.4), y = (self.Screen_Height / 3), width = 250, height = 100)

        Delete_Student_Button = Button(self.Manage_Student_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Delete a student", font = ("Helvetica",20), command = self.Delete_Student_Data_Screen)
        Delete_Student_Button.place(x = (self.Screen_Width / 1.4), y = (self.Screen_Height / 3), width = 250, height = 100)

    #Creates and adds widgets to a new Tkinter screen which will be used for adding a student record to the database
    def Student_Creation_Screen(self):
        #Creates the screen and sets general parameters for the screen
        Student_Creation = Tk()
        Student_Creation.title("Add an admin's data")
        Student_Creation.geometry(self.size)
        Student_Creation.config(bg = self.hp.Find_Colour("Light Blue"))

        Student_Creation_Title_Frame = self.hp.Create_Title_Frame(Student_Creation, self.Screen_Width, self.Screen_Height)
        Student_Creation_Title_Label = self.hp.Create_Title_Label(Student_Creation_Title_Frame, "Add a Student")

        Back_Button = self.hp.Create_Back_Button(Student_Creation_Title_Frame, Student_Creation)

        Down_Arrow = PhotoImage(master = Student_Creation, file = "Down_Arrow.gif")    #Creates an image widget to be used on the drop-down menus

        Name_Entry_Label = Label(Student_Creation, text = "Name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Name_Entry_Label.place(x = self.First_Column_Entry_Position - 100, y = (self.Screen_Height / 8), width = 90, height = 30)


        #Creates a drop-down menu for each day of the month

        #Creates a list of days to be used when the user selects their birth day
        Day_List = []
        for Day in range(1,32):
            if Day < 10:
                To_Add = "0" + str(Day)
            else:
                To_Add = Day
            Day_List.append(To_Add)
        self.Day_Of_Birth_Options_Label = StringVar(Student_Creation)    #Creates and configures a label to be used in the drop-down menus
        self.Day_Of_Birth_Options_Label.set("Choose one:")    #Sets a value for the label created on the line above
        self.Day_Of_Birth_Options = OptionMenu(Student_Creation, self.Day_Of_Birth_Options_Label,*Day_List)    #Creates a drop-down list with each day as a selectable option
        self.Day_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Day_Of_Birth_Options.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 5), width = 150, height = 30)
        Day_Of_Birth_Asterick = self.hp.Create_Asterick(Student_Creation)
        Day_Of_Birth_Asterick.place(x = self.First_Column_Entry_Position + 150, y = (self.Screen_Height / 5) - 25)
        Day_Of_Birth_Entry_Label = Label(Student_Creation, font = ("Helvetica", 12), bg = self.hp.Find_Colour("Light Blue"), text = "Day:")
        Day_Of_Birth_Entry_Label.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height /5) - 25)
        Options = self.Day_Of_Birth_Options.nametowidget(self.Day_Of_Birth_Options.menuname)    #Retrieves the drop-down menu widget from the screen - this allows the font to be edited
        Options.configure(font = ("Helvetica", 12))    #Changes the font style and size of the text in the drop-down list

        #Same as the Day_Of_Birth drop-down menu above, but for months instead
        Month_List = []
        for Month in range(1,13):
            if Month < 10:
                To_Add = "0" + str(Month)
            else:
                To_Add = Month
            Month_List.append(To_Add)
        self.Month_Of_Birth_Options_Label = StringVar(Student_Creation)
        self.Month_Of_Birth_Options_Label.set("Choose one:")
        self.Month_Of_Birth_Options = OptionMenu(Student_Creation, self.Month_Of_Birth_Options_Label,*Month_List)
        self.Month_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"),font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Month_Of_Birth_Options.place(x = self.First_Column_Entry_Position + 250, y = (self.Screen_Height / 5), width = 150, height = 30)
        Month_Of_Birth_Entry_Label = Label(Student_Creation, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12), text = "Month:")
        Month_Of_Birth_Entry_Label.place(x = self.First_Column_Entry_Position + 250, y = (self.Screen_Height / 5) - 25)
        Month_Of_Birth_Asterick = self.hp.Create_Asterick(Student_Creation)
        Month_Of_Birth_Asterick.place(x = self.First_Column_Entry_Position + 250 + 150, y = (self.Screen_Height / 5) - 25)
        Options = self.Month_Of_Birth_Options.nametowidget(self.Month_Of_Birth_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but for years instead
        Year_List = []
        for Year in range(2019,1900,-1):    #Change range to alter the years displayed on screen
            Year_List.append(Year)
        self.Year_Of_Birth_Options_Label = StringVar(Student_Creation)
        self.Year_Of_Birth_Options_Label.set("Choose one:")
        self.Year_Of_Birth_Options = OptionMenu(Student_Creation, self.Year_Of_Birth_Options_Label, *Year_List)
        self.Year_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Year_Of_Birth_Options.place(x = self.First_Column_Entry_Position + 250 + 150 + 100, y = (self.Screen_Height / 5), width = 150, height = 30)
        Year_Of_Birth_Entry_Label = Label(Student_Creation, text = "Year:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",12))
        Year_Of_Birth_Entry_Label.place(x = self.First_Column_Entry_Position + 250 + 150 + 100, y = (self.Screen_Height / 5) - 25)
        Year_Of_Birth_Asterick = self.hp.Create_Asterick(Student_Creation)
        Year_Of_Birth_Asterick.place(x = self.First_Column_Entry_Position + 250 + 150 + 100 + 150, y = (self.Screen_Height/5) - 25)
        Options = self.Year_Of_Birth_Options.nametowidget(self.Year_Of_Birth_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but uses a subject list created in the Helper_Class
        self.First_Subject_Options_Label = StringVar(Student_Creation)
        self.First_Subject_Options_Label.set("Choose one:")
        self.First_Subject_Options = OptionMenu(Student_Creation, self.First_Subject_Options_Label, *self.hp.Subject_List)
        self.First_Subject_Options.config(bg = "Light Blue", font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.First_Subject_Options.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 320, height = 30)
        Primary_Subject_Entry_Label = Label(Student_Creation, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16), text = "Primary Subject:")
        Primary_Subject_Entry_Label.place(x = self.First_Column_Entry_Position - 175, y = (self.Screen_Height / 3.8))
        Primary_Subject_Asterick = self.hp.Create_Asterick(Student_Creation)
        Primary_Subject_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 3.8) - 25)
        Options = self.First_Subject_Options.nametowidget(self.First_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but uses a subject list created in the Helper_Class
        self.Second_Subject_Options_Label = StringVar(Student_Creation)
        self.Second_Subject_Options_Label.set("Choose one:")
        self.Second_Subject_Options = OptionMenu(Student_Creation, self.Second_Subject_Options_Label, *self.hp.Subject_List)
        self.Second_Subject_Options.config(bg = "Light Blue", font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Second_Subject_Options.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 3.1), width = 320, height = 30)
        Secondary_Subject_Entry_Label = Label(Student_Creation, bg = self.hp.Find_Colour("Light Blue"), text = "Secondary Subject:", font = ("Helvetica", 16))
        Secondary_Subject_Entry_Label.place(x = self.First_Column_Entry_Position - 205, y = (self.Screen_Height / 3.1))
        Options = self.Second_Subject_Options.nametowidget(self.Second_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))


        #Most chuncks of code from now to the end of this function add an entry box, label and asterick to the screen for each data field - add your own if necessary
        #When placing anything on the screen, the variables self.First_Column_Entry_Position and self.Second_Column_Entry_Position will be used to align the widgets

        self.First_Name_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.First_Name_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 8), width = (self.Screen_Width/2) - (self.Screen_Width/4.5), height = 30)
        First_Name_Entry_Label = Label(Student_Creation, text = "First:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        First_Name_Entry_Label.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 8) - 25)
        First_Name_Asterick = self.hp.Create_Asterick(Student_Creation)
        First_Name_Asterick.place(x = self.First_Column_Entry_Position + ((self.Screen_Width/2) - (self.Screen_Width/4.5)), y = (self.Screen_Height / 8) - 25)

        self.Last_Name_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.Last_Name_Entry.place(x = self.Second_Column_Entry_Position - 150, y = (self.Screen_Height / 8), width = (self.Screen_Width/2) - (self.Screen_Width/4.5), height = 30)
        Last_Name_Entry_Label = Label(Student_Creation, text = "Last:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Last_Name_Entry_Label.place(x = self.Second_Column_Entry_Position - 150, y = (self.Screen_Height / 8) - 25)
        Last_Name_Asterick = self.hp.Create_Asterick(Student_Creation)
        Last_Name_Asterick.place(x = self.Second_Column_Entry_Position - 150 + (self.Screen_Width/2) - (self.Screen_Width/4.5), y = (self.Screen_Height / 8) - 25)

        DOB_Entry_Label = Label(Student_Creation, text = "D.O.B:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        DOB_Entry_Label.place(x = self.First_Column_Entry_Position - 100, y = (self.Screen_Height / 5), width = 90, height = 30)

        self.Year_Group_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.Year_Group_Entry.place(x = self.First_Column_Entry_Position , y = (self.Screen_Height / 2.6), height = 30, width = 320)
        Year_Group_Entry_Label = Label(Student_Creation, text = "Year Group:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Year_Group_Entry_Label.place(x = self.First_Column_Entry_Position - 140, y = (self.Screen_Height /2.6))
        Year_Group_Asterick = self.hp.Create_Asterick(Student_Creation)
        Year_Group_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.6) - 25)

        self.Main_Travel_Method_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.Main_Travel_Method_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 2.25), width = 320, height = 30)
        Main_Travel_Method_Entry_Label = Label(Student_Creation, text = "Main travel method:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Main_Travel_Method_Entry_Label.place(x = self.First_Column_Entry_Position - 210, y = (self.Screen_Height / 2.25))
        Main_Travel_Method_Asterick = self.hp.Create_Asterick(Student_Creation)
        Main_Travel_Method_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.25) - 25)

        self.Allergies_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.Allergies_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 320, height = 30)
        Allergies_Entry_Label = Label(Student_Creation, text = "Allergies:", font = ("Helvetica", 16), bg = self.hp.Find_Colour("Light Blue"))
        Allergies_Entry_Label.place(x = self.First_Column_Entry_Position - 115, y = (self.Screen_Height / 1.95))
        Allergies_Asterick = self.hp.Create_Asterick(Student_Creation)
        Allergies_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.95) - 25)

        self.Medical_Conditions_Entry = Entry(Student_Creation, font = ("Helvetica", 15))
        self.Medical_Conditions_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 320, height = 30)
        Medical_Conditions_Entry_Label = Label(Student_Creation, text = "Medical Conditions:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Medical_Conditions_Entry_Label.place(x = self.First_Column_Entry_Position - 215, y = (self.Screen_Height / 1.75))
        Medical_Conditions_Asterick = self.hp.Create_Asterick(Student_Creation)
        Medical_Conditions_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.75) - 25)

        #Creates a label for the address, then adds several entry boxes for each part of the address
        Address_Entry_Label = Label(Student_Creation, text = "Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Address_Entry_Label.place(x = self.Second_Column_Entry_Position - 100, y = (self.Screen_Height / 3.8))

        self.Home_Number_Entry= Entry(Student_Creation, font = ("Helvetica", 15))
        self.Home_Number_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 100, height = 30)
        Home_Number_Entry_Label = Label(Student_Creation, text = "House number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Home_Number_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3.8) - 25)
        Home_Number_Asterick = self.hp.Create_Asterick(Student_Creation)
        Home_Number_Asterick.place(x = self.Second_Column_Entry_Position + 110, y = (self.Screen_Height / 3.8) - 25)

        self.Road_Name_Entry= Entry(Student_Creation, font = ("Helvetica", 15))
        self.Road_Name_Entry.place(x = self.Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8), width = 220, height = 30)
        Road_Name_Entry_Label = Label(Student_Creation, text = "Road name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Road_Name_Entry_Label.place(x = self.Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8) - 25)
        Road_Name_Asterick = self.hp.Create_Asterick(Student_Creation)
        Road_Name_Asterick.place(x = self.Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3.8) - 25)

        self.Borough_Entry= Entry(Student_Creation, font = ("Helvetica", 15))
        self.Borough_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3), width = 160, height = 30)
        Borough_Entry_Label = Label(Student_Creation, text = "Borough:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Borough_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3) - 25)
        Borough_Asterick = self.hp.Create_Asterick(Student_Creation)
        Borough_Asterick.place(x = self.Second_Column_Entry_Position + 160, y = (self.Screen_Height / 3) - 25)

        self.County_Entry= Entry(Student_Creation, font = ("Helvetica", 15))
        self.County_Entry.place(x = self.Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3), width = 165, height = 30)
        County_Entry_Label = Label(Student_Creation, text = "County:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        County_Entry_Label.place(x = self.Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3) - 25)
        County_Asterick = self.hp.Create_Asterick(Student_Creation)
        County_Asterick.place(x = self.Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3) - 25)

        self.Postcode_Entry= Entry(Student_Creation, font = ("Helvetica", 15))
        self.Postcode_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 2.5), width = 100, height = 30)
        Postcode_Entry_Label = Label(Student_Creation, text = "Postcode:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Postcode_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 2.5) - 25)
        Postcode_Asterick = self.hp.Create_Asterick(Student_Creation)
        Postcode_Asterick.place(x = self.Second_Column_Entry_Position + 100, y = (self.Screen_Height / 2.5) - 25)

        #Creates a new box on the screen to seperate the parts where a student and parent's details are needed
        Parent_Details_Frame = Frame(Student_Creation, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= "black", highlightcolor="black", highlightthickness=1)
        Parent_Details_Frame.place(x = self.Second_Column_Entry_Position - 150, y = (self.Screen_Height / 2.1), width = 550, height = (self.Screen_Height / 1.6) - (self.Screen_Height / 2.55))
        Parent_Details_Frame_Label = Label(Parent_Details_Frame, bg = self.hp.Find_Colour("Light Blue"), text = "Parent Details:", font = ("Helvetica",16))
        Parent_Details_Frame_Label.pack(side = TOP)

        Parent_Name_Entry_Label = Label(Parent_Details_Frame, text = "Name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Parent_Name_Entry_Label.place(x = 5, y = 50, width = 90, height = 30)

        self.Parent_First_Name_Entry = Entry(Parent_Details_Frame, font = ("Helvetica", 15))
        self.Parent_First_Name_Entry.place(x = 100, y = 50, width = 200, height = 30)
        Parent_First_Name_Entry_Label = Label(Parent_Details_Frame, text = "First:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Parent_First_Name_Entry_Label.place(x = 100, y = 25)
        Parent_First_Name_Asterick = self.hp.Create_Asterick(Parent_Details_Frame)
        Parent_First_Name_Asterick.place(x = 100 + 200, y = 25)

        self.Parent_Last_Name_Entry = Entry(Parent_Details_Frame, font = ("Helvetica", 15))
        self.Parent_Last_Name_Entry.place(x = 340, y = 50, width = 200, height = 30)
        Parent_Last_Name_Entry_Label = Label(Parent_Details_Frame, text = "Last:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Parent_Last_Name_Entry_Label.place(x = 340, y = 25)
        Parent_Last_Name_Asterick = self.hp.Create_Asterick(Parent_Details_Frame)
        Parent_Last_Name_Asterick.place(x = 340 + 200, y = 25)

        self.Parent_Phone_Number_Entry = Entry(Parent_Details_Frame, font = ("Helvetica", 15))
        self.Parent_Phone_Number_Entry.place(x = 160, y = 110, width = 380, height = 30)
        Parent_Phone_Number_Entry_Label = Label(Parent_Details_Frame, font = ("Helvetica", 16), text = "Phone number:", bg = self.hp.Find_Colour("Light Blue"))
        Parent_Phone_Number_Entry_Label.place(x = 5, y = 110)
        Parent_Phone_Number_Asterick = self.hp.Create_Asterick(Parent_Details_Frame)
        Parent_Phone_Number_Asterick.place(x = 540, y = 85)

        self.Parent_Email_Address_Entry = Entry(Parent_Details_Frame, font = ("Helvetica", 15))
        self.Parent_Email_Address_Entry.place(x = 160, y = 170, width = 380, height = 30)
        Parent_Email_Address_Entry_Label = Label(Parent_Details_Frame, font = ("Helvetica", 16), text = "Email Address:", bg = self.hp.Find_Colour("Light Blue"))
        Parent_Email_Address_Entry_Label.place(x = 5, y = 170)
        Parent_Email_Address_Asterick = self.hp.Create_Asterick(Parent_Details_Frame)
        Parent_Email_Address_Asterick.place(x = 540, y = 145)

        #Adds a submit button - when pressed the details entered are checked by calling the Confirm_Student_Creation() function
        Submit_Button = Button(Student_Creation, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Student_Creation)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 1.4, width = 110)

        #Tells the user that all fields with astericks need to be filled in
        Asterick_Notice_Label = Label(Student_Creation, text = "* Required fields - enter 'None' if empty", bg = self.hp.Find_Colour("Light Blue"), fg = self.hp.Find_Colour("Dark Red"), font = ("Helvetica", 15), wraplength = 250)
        Asterick_Notice_Label.place(x = (self.Screen_Width / 1.3), y = self.Screen_Height / 1.4)

        Student_Creation.mainloop()

    #Creates and adds widgets to a new Tkinter screen which will be used for editing a student record already in the database
    def Edit_Student_Data_Screen(self):
        self.Edit_Student_Data = Tk()
        self.Edit_Student_Data.geometry(self.size)
        self.Edit_Student_Data.title("Edit a Student's data")
        self.Edit_Student_Data.config(bg = self.hp.Find_Colour("Light Blue"))

        Title_Frame = self.hp.Create_Title_Frame(self.Edit_Student_Data, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Edit a Student's data")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.Edit_Student_Data)

        self.Choosing_Name_Frame = Frame(self.Edit_Student_Data, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= self.hp.Find_Colour("Light Blue"), highlightcolor= self.hp.Find_Colour("Light Blue"), highlightthickness=1)
        self.Choosing_Name_Frame.place(x = self.Screen_Width / 2.5, y = self.Screen_Height / 9, width = 300, height = 30)

        #Gets all the student names from the database and organises it so it can be used in a drop-down list
        Students = self.sd.Select_Students()
        Name_List = []
        Student_Count = 0
        for Student in Students:
            Student_Detail = Students[Student_Count]
            First_Name = Student_Detail.get("First_Name", "none")
            Last_Name = Student_Detail.get("Last_Name", "none")
            Student_Name = First_Name + " " + Last_Name
            Name_List.append(Student_Name)
            Student_Count += 1

        #Creates a drop-down menu similar to the Day_Of_Birth drop-down menu, described in lines 65-72
        self.Choosing_Name_Options_Label = StringVar(self.Choosing_Name_Frame)
        self.Choosing_Name_Options_Label.set("Choose a person to edit the data of:")
        Down_Arrow = PhotoImage(master = self.Choosing_Name_Frame, file = "Down_Arrow.gif")
        self.Choosing_Name_Options = OptionMenu(self.Choosing_Name_Frame, self.Choosing_Name_Options_Label, *Name_List,  command = self.Change_Screen)
        self.Choosing_Name_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 13),indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Choosing_Name_Options.place(x = 0, y = 0, width = 300, height = 30)
        Options = self.Choosing_Name_Options.nametowidget(self.Choosing_Name_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        self.Edit_Student_Data.mainloop()

    #Changes the widgets on the screen when the user selects the name of the person they wish to edit the data of
    def Change_Screen(self, Name):
        self.Down_Arrow = PhotoImage(master = self.Edit_Student_Data, file = "Down_Arrow.gif")

        #Extracts the record with the name of the selected person - if extra data fields are added then follow the format below
        Students = self.sd.Select_Students()
        First_Subject = ""
        Second_Subject = ""
        Student_Count = 0
        for Student in Students:
            self.Student_Detail = Students[Student_Count]
            First_Name = self.Student_Detail.get("First_Name", "none")
            Last_Name = self.Student_Detail.get("Last_Name", "none")
            Student_Name = First_Name + " " + Last_Name
            if Student_Name == Name:
                Student_ID = self.Student_Detail.get("ID", "none")
                First_Subject = self.Student_Detail.get("First_Subject", "none")
                Second_Subject = self.Student_Detail.get("Second_Subject", "none")
                Allergies = self.Student_Detail.get("Allergies", "none")
                Year_Group = self.Student_Detail.get("School_Year", "none")
                Medical_Conditions = self.Student_Detail.get("Medical_Conditions", "none")
                Main_Travel_Method = self.Student_Detail.get("Main_Travel_Method", "none")
                Parent_Phone_Number = self.Student_Detail.get("Parent_Phone_Number", "none")
                Parent_Email_Address = self.Student_Detail.get("Parent_Email_Address", "none")
                Address1 = self.Student_Detail.get("Address1", "none")
                Address2 = self.Student_Detail.get("Address2", "none")
                Postcode = self.Student_Detail.get("Postcode", "none")
                Address1 = Address1.split(",")
                House_Number = Address1[0]
                Road_Name = Address1[1]
                Address2 = Address2.split(",")
                Borough = Address2[0]
                County = Address2[1]
                break
            Student_Count += 1

        #Creates a drop down menu for the student's first subject option choice - similar to lines 66-78
        self.First_Subject_Options_Label = StringVar(self.Edit_Student_Data)
        self.First_Subject_Options_Label.set(First_Subject)
        self.First_Subject_Options = OptionMenu(self.Edit_Student_Data, self.First_Subject_Options_Label,*self.hp.Subject_List)
        self.First_Subject_Options.config(bg = "Light Blue", font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = self.Down_Arrow)
        self.First_Subject_Options.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 320, height = 30)
        Primary_Subject_Entry_Label = Label(self.Edit_Student_Data, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16), text = "Primary Subject:")
        Primary_Subject_Entry_Label.place(x = self.First_Column_Entry_Position - 175, y = (self.Screen_Height / 3.8))
        Primary_Subject_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Primary_Subject_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 3.8) - 25)
        Options = self.First_Subject_Options.nametowidget(self.First_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Creates a drop down menu for the student's second subject option choice - similar to lines 66-78
        self.Second_Subject_Options_Label = StringVar(self.Edit_Student_Data)
        self.Second_Subject_Options_Label.set(Second_Subject)
        self.Second_Subject_Options = OptionMenu(self.Edit_Student_Data, self.Second_Subject_Options_Label, *self.hp.Subject_List)
        self.Second_Subject_Options.config(bg = "Light Blue", font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = self.Down_Arrow)
        self.Second_Subject_Options.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 3.1), width = 320, height = 30)
        Secondary_Subject_Entry_Label = Label(self.Edit_Student_Data, bg = self.hp.Find_Colour("Light Blue"), text = "Secondary Subject:", font = ("Helvetica", 16))
        Secondary_Subject_Entry_Label.place(x = self.First_Column_Entry_Position - 205, y = (self.Screen_Height / 3.1))
        Options = self.Second_Subject_Options.nametowidget(self.Second_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))


        #Most chuncks of code from now to the end of this function add an entry box, label and asterick to the screen for each data field - add your own if necessary
        #When placing anything on the screen, the variables self.First_Column_Entry_Position and self.Second_Column_Entry_Position will be used to align the widgets


        self.Year_Group_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Year_Group_Entry.insert(0, Year_Group)
        self.Year_Group_Entry.place(x = self.First_Column_Entry_Position , y = (self.Screen_Height / 2.6), height = 30, width = 320)
        Year_Group_Entry_Label = Label(self.Edit_Student_Data, text = "Year Group:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Year_Group_Entry_Label.place(x = self.First_Column_Entry_Position - 140, y = (self.Screen_Height /2.6))
        Year_Group_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Year_Group_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.6) - 25)

        self.Main_Travel_Method_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Main_Travel_Method_Entry.insert(0, Main_Travel_Method)
        self.Main_Travel_Method_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 2.25), width = 320, height = 30)
        Main_Travel_Method_Entry_Label = Label(self.Edit_Student_Data, text = "Main travel method:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Main_Travel_Method_Entry_Label.place(x = self.First_Column_Entry_Position - 210, y = (self.Screen_Height / 2.25))
        Main_Travel_Method_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Main_Travel_Method_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.25) - 25)

        self.Allergies_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Allergies_Entry.insert(0,Allergies)
        self.Allergies_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 320, height = 30)
        Allergies_Entry_Label = Label(self.Edit_Student_Data, text = "Allergies:", font = ("Helvetica", 16), bg = self.hp.Find_Colour("Light Blue"))
        Allergies_Entry_Label.place(x = self.First_Column_Entry_Position - 115, y = (self.Screen_Height / 1.95))
        Allergies_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Allergies_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.95) - 25)

        self.Medical_Conditions_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Medical_Conditions_Entry.insert(0,Medical_Conditions)
        self.Medical_Conditions_Entry.place(x = self.First_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 320, height = 30)
        Medical_Conditions_Entry_Label = Label(self.Edit_Student_Data, text = "Medical Conditions:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Medical_Conditions_Entry_Label.place(x = self.First_Column_Entry_Position - 215, y = (self.Screen_Height / 1.75))
        Medical_Conditions_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Medical_Conditions_Asterick.place(x = self.First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.75) - 25)


        #Creates a label for the address, then adds several entry boxes for each part of the address
        Address_Entry_Label = Label(self.Edit_Student_Data, text = "Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Address_Entry_Label.place(x = self.Second_Column_Entry_Position - 100, y = (self.Screen_Height / 3.8))

        self.Home_Number_Entry= Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Home_Number_Entry.insert(0,House_Number)
        self.Home_Number_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 100, height = 30)
        Home_Number_Entry_Label = Label(self.Edit_Student_Data, text = "House number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Home_Number_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3.8) - 25)
        Home_Number_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Home_Number_Asterick.place(x = self.Second_Column_Entry_Position + 110, y = (self.Screen_Height / 3.8) - 25)

        self.Road_Name_Entry= Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Road_Name_Entry.insert(0,Road_Name)
        self.Road_Name_Entry.place(x = self.Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8), width = 220, height = 30)
        Road_Name_Entry_Label = Label(self.Edit_Student_Data, text = "Road name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Road_Name_Entry_Label.place(x = self.Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8) - 25)
        Road_Name_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Road_Name_Asterick.place(x = self.Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3.8) - 25)

        self.Borough_Entry= Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Borough_Entry.insert(0,Borough)
        self.Borough_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3), width = 160, height = 30)
        Borough_Entry_Label = Label(self.Edit_Student_Data, text = "Borough:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Borough_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 3) - 25)
        Borough_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Borough_Asterick.place(x = self.Second_Column_Entry_Position + 160, y = (self.Screen_Height / 3) - 25)

        self.County_Entry= Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.County_Entry.insert(0,County)
        self.County_Entry.place(x = self.Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3), width = 165, height = 30)
        County_Entry_Label = Label(self.Edit_Student_Data, text = "County:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        County_Entry_Label.place(x = self.Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3) - 25)
        County_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        County_Asterick.place(x = self.Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3) - 25)

        self.Postcode_Entry= Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Postcode_Entry.insert(0,Postcode)
        self.Postcode_Entry.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 2.5), width = 100, height = 30)
        Postcode_Entry_Label = Label(self.Edit_Student_Data, text = "Postcode:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Postcode_Entry_Label.place(x = self.Second_Column_Entry_Position, y = (self.Screen_Height / 2.5) - 25)
        Postcode_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Postcode_Asterick.place(x = self.Second_Column_Entry_Position + 100, y = (self.Screen_Height / 2.5) - 25)

        self.Parent_Phone_Number_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Parent_Phone_Number_Entry.insert(0,Parent_Phone_Number)
        self.Parent_Phone_Number_Entry.place(x = self.Second_Column_Entry_Position + 50, y = self.Screen_Height / 2.2, width = 330, height = 30)
        Parent_Phone_Number_Entry_Label = Label(self.Edit_Student_Data, font = ("Helvetica", 16), text = "Parent's phone number:", bg = self.hp.Find_Colour("Light Blue"))
        Parent_Phone_Number_Entry_Label.place(x = self.Second_Column_Entry_Position - 195, y = self.Screen_Height / 2.2)
        Parent_Phone_Number_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Parent_Phone_Number_Asterick.place(x = self.Second_Column_Entry_Position + 390, y = (self.Screen_Height / 2.2) - 25)

        self.Parent_Email_Address_Entry = Entry(self.Edit_Student_Data, font = ("Helvetica", 15))
        self.Parent_Email_Address_Entry.insert(0,Parent_Email_Address)
        self.Parent_Email_Address_Entry.place(x = self.Second_Column_Entry_Position + 50, y = self.Screen_Height / 2, width = 330, height = 30)
        Parent_Email_Address_Entry_Label = Label(self.Edit_Student_Data, font = ("Helvetica", 16), text = "Parent's Email Address:", bg = self.hp.Find_Colour("Light Blue"))
        Parent_Email_Address_Entry_Label.place(x = self.Second_Column_Entry_Position - 195, y = self.Screen_Height / 2)
        Parent_Email_Address_Asterick = self.hp.Create_Asterick(self.Edit_Student_Data)
        Parent_Email_Address_Asterick.place(x = self.Second_Column_Entry_Position + 390, y = (self.Screen_Height / 2) - 25)

        Submit_Button = Button(self.Edit_Student_Data, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Edit_Student)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 1.4, width = 110)

    #Creates and adds widgets to a new Tkinter screen which will be used for deleting a student's data
    def Delete_Student_Data_Screen(self):
        Delete_Student_Data = Tk()
        Delete_Student_Data.geometry(self.size)
        Delete_Student_Data.title("Delete a Student's data")
        Delete_Student_Data.config(bg = self.hp.Find_Colour("Light Blue"))

        Title_Frame = self.hp.Create_Title_Frame(Delete_Student_Data, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Delete a Student's data")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, Delete_Student_Data)

        #Gets all the student names from the database and organises it so it can be used in a drop-down list
        Students = self.sd.Select_Students()
        Name_List = []
        Student_Count = 0
        for Student in Students:
            Student_Detail = Students[Student_Count]
            First_Name = Student_Detail.get("First_Name", "none")
            Last_Name = Student_Detail.get("Last_Name", "none")
            Student_Name = First_Name + " " + Last_Name
            Name_List.append(Student_Name)
            Student_Count += 1

        Submit_Button = Button(Delete_Student_Data, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Delete_Student_Screen)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 2, width = 110)

        self.Choosing_Name_Frame = Frame(Delete_Student_Data, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= self.hp.Find_Colour("Light Blue"), highlightcolor= self.hp.Find_Colour("Light Blue"), highlightthickness=1)
        self.Choosing_Name_Frame.place(x = self.Screen_Width / 2.5 - 25, y = self.Screen_Height / 9, width = 350, height = 30)

        #Creates a drop-down menu for the user to select a name
        self.Choosing_Name_Options_Label = StringVar(self.Choosing_Name_Frame)
        self.Choosing_Name_Options_Label.set("Choose a person to delete the data of:")
        Down_Arrow = PhotoImage(master = self.Choosing_Name_Frame, file = "Down_Arrow.gif")
        self.Choosing_Name_Options = OptionMenu(self.Choosing_Name_Frame, self.Choosing_Name_Options_Label, *Name_List)
        self.Choosing_Name_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 13),indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Choosing_Name_Options.place(x = 0, y = 0, width = 350, height = 30)
        Options = self.Choosing_Name_Options.nametowidget(self.Choosing_Name_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        Delete_Student_Data.mainloop()


    #Runs the validation process for adding a student record - this will run after the user presses "Submit" and will show a popup box for the result of the process
    def Confirm_Student_Creation(self):

        #Gets all the entries the user has provided, then sets their format depending on how they will be stored in the database (e.g: .upper for postcodes, .capitalise for names etc)
        #for each data field - add your own if necessary
        First_Name = str(self.First_Name_Entry.get().lower().capitalize())
        Last_Name = str(self.Last_Name_Entry.get().lower().capitalize())
        Day_Of_Birth = str(self.Day_Of_Birth_Options_Label.get())
        Month_Of_Birth = str(self.Month_Of_Birth_Options_Label.get())
        Year_Of_Birth = str(self.Year_Of_Birth_Options_Label.get())
        First_Subject = str(self.First_Subject_Options_Label.get())
        Second_Subject = str(self.Second_Subject_Options_Label.get())
        School_Year = str(self.Year_Group_Entry.get().lower().capitalize())
        Main_Travel_Method = str(self.Main_Travel_Method_Entry.get().lower().capitalize())
        Allergies = str(self.Allergies_Entry.get().lower().capitalize())
        Medical_Conditions = str(self.Medical_Conditions_Entry.get().lower().capitalize())
        House_Number = str(self.Home_Number_Entry.get())
        Road_Name = str(self.Road_Name_Entry.get().lower().capitalize())
        Borough = str(self.Borough_Entry.get().lower().capitalize())
        County = str(self.County_Entry.get().lower().capitalize())
        Postcode = str(self.Postcode_Entry.get().upper())
        Parent_First_Name = str(self.Parent_First_Name_Entry.get().lower().capitalize())
        Parent_Last_Name = str(self.Parent_Last_Name_Entry.get().lower().capitalize())
        Parent_Phone_Number = str(self.Parent_Phone_Number_Entry.get())
        Parent_Email_Address = str(self.Parent_Email_Address_Entry.get())

        #Organises certain aspects of the data to be stored into the database - add any other special conditions for formatting here
        DOB = Day_Of_Birth + "/" + Month_Of_Birth + "/" + Year_Of_Birth
        if Second_Subject == "Choose one:":
            Second_Subject = "N/A"
        Address1 = House_Number + "," + Road_Name
        Address2 = Borough + "," + County

        #Checks if each of the individual criteria is met - add your own criteria after the line marked with a +++
        Reject_Application = True   #Defaults a checking variable to (invalid) - Validation rejected until otherwise stated
        Message = "Registration sucessful!"    #Sets the message to be displayed at the end of the process - this is at default a pass so it can be used to see when an error has been picked up
        while Message == "Registration sucessful!":
            #Checks to make sure all necessary entry boxes have been filled in: +++ your extra entry boxes here if they have to be filled in
            if First_Name == "" or Last_Name == "" or Day_Of_Birth == "Choose one:" or Month_Of_Birth == "Choose one:" or Year_Of_Birth == "Choose one:" or First_Subject == "Choose one:" or School_Year == "" or Main_Travel_Method == "" or Allergies == "" or Medical_Conditions == "" or House_Number == "" or Road_Name == "" or Borough == "" or County == "" or Postcode == "" or Parent_First_Name == "" or Parent_Last_Name == "" or Parent_Phone_Number == "" or Parent_Email_Address == "":
                Message = "Please fill in all entry boxes marked with a *"  #Changes the message to reflect the error occurred
                break
            else:
                #Creates a blank list to be placed into the function on the line below.
                #+++ your own entry boxes if they need to be words only
                To_Confirm = [First_Name, Last_Name, Main_Travel_Method, Allergies, Medical_Conditions, Road_Name, Borough, County, Parent_First_Name, Parent_Last_Name]
                Failed = self.hp.Check_Strings(To_Confirm)    #Runs a function in the helper class that checks each of the entries in the list above, making sure they are all words with only spaces or commas inbetween
                Postcode_Failed = False
                for character in Postcode:
                    if character != " " and not(character.isalpha() or character.isnumeric()):    #Checks to make sure the postcode contains only letter, number and space characters
                        Postcode_Failed = True
                if Failed or not School_Year.isnumeric():    #Uses the checking function called above and a number check to make sure that the right characters are used in the entry boxes (letters or numbers)
                    Message = "Invalid characters used"    #Changes the message to reflect the error occurred
                    break
                elif First_Subject == Second_Subject:    #Checks to make sure that two seperate subjects are chosen
                    Message = "First and second subjects cannot be the same"    #Changes the message to reflect the error occurred
                    break
                elif len(Postcode) > 10 or Postcode_Failed:    #Checks to make sure the postcode contains the right characters (from above) and that the postcode is not beyond the postcode size limit
                    Message = "Postcode is invalid"    #Changes the message to reflect the error occurred
                    break
                else:
                    #Checks for an @ symbol, necessary for any email address
                    Necessary_Character_Found = False
                    for character in Parent_Email_Address:
                        if character == "@":
                            Necessary_Character_Found = True
                    if Necessary_Character_Found == False:
                        Message = "Email address needs a @ symbol"    #Changes the message to reflect the error occurred
                        break
                    else:
                        #Checks for any disallowed symbols in phone numbers (anything not a number or space)
                        Invalid_Character_Found = False
                        for character in Parent_Phone_Number:
                            if character.isnumeric() != True and character != " ":
                                Invalid_Character_Found = True
                        if Invalid_Character_Found == True:
                            Message = "Phone number cannot contain non-number characters"    #Changes the message to reflect the error occurred
                            break
                        else:
                            #Checks to make sure the birthday entered exists (i.e: Not February 31st)
                            Valid_Birthday = self.hp.Check_Birthday(Day_Of_Birth, Month_Of_Birth, Year_Of_Birth)    #Calls a function in the helper class to check the birthday
                            if Valid_Birthday:
                                #This is currently the last validation check in the process - add your own by:
                                #+++, then adjust line below so that it doesn't automatically set Reject_Application to False
                                Reject_Application = False    #After all checks have passed, the checking variable is changed to reflect that the user has passed the validation checks
                                break
                            else:
                                Message = "Invalid birthday"    #Changes the message to reflect the error occurred
                                break

        #Adds the student to the database if the validation has returned positive
        if Reject_Application == False:
            #Collects all the student's details into a list: if extra data fields are added make sure to add the entry ox representing their details in the right spot (presumably at the end)
            Student_Detail = [First_Name, Last_Name, DOB, First_Subject, Second_Subject, School_Year, Main_Travel_Method, Allergies, Medical_Conditions, Address1, Address2, Postcode, Parent_First_Name, Parent_Last_Name, Parent_Phone_Number, Parent_Email_Address]
            self.sd.Insert_Student(Student_Detail)    #Adds the student record into the database
            self.hp.Success_Window(Message)    #Displays a message box telling the user the student has been added
        else:
            self.hp.Error_Window(Message)    #Displays a message box telling the user the student has not been added, and describes what they have done wrong using the Message variable changed in the validation process

    #Runs the validation process for editing a student record - this will run after the user presses "Submit" and will show a popup box for the result of the process
    #Note that a lot of this function will be a repeat from Confirm_Student_Creation(), so the code for validating and retrieving any entry boxes you add that can be edited can be copied and pasted
    def Confirm_Edit_Student(self):
        #Gets all the entries the user has provided, then sets their format depending on how they will be stored in the database (e.g: .upper for postcodes, .capitalise for names etc)
        #for each data field - add your own if necessary
        First_Subject = str(self.First_Subject_Options_Label.get())
        Second_Subject = str(self.Second_Subject_Options_Label.get())
        School_Year = str(self.Year_Group_Entry.get().lower().capitalize())
        Main_Travel_Method = str(self.Main_Travel_Method_Entry.get().lower().capitalize())
        Allergies = str(self.Allergies_Entry.get().lower().capitalize())
        Medical_Conditions = str(self.Medical_Conditions_Entry.get().lower().capitalize())
        House_Number = str(self.Home_Number_Entry.get())
        Road_Name = str(self.Road_Name_Entry.get().lower().capitalize())
        Borough = str(self.Borough_Entry.get().lower().capitalize())
        County = str(self.County_Entry.get().lower().capitalize())
        Postcode = str(self.Postcode_Entry.get().upper())
        Parent_Phone_Number = str(self.Parent_Phone_Number_Entry.get())
        Parent_Email_Address = str(self.Parent_Email_Address_Entry.get())


        #Checks if each of the individual criteria is met - add your own criteria after the line marked with a +++

        Reject_Application = True   #Defaults a checking variable to (invalid) - Validation rejected until otherwise stated
        Message = "Changes sucessful"    #Sets the message to be displayed at the end of the process - this is at default a pass so it can be used to see when an error has been picked up
        #Checks to make sure all necessary entry boxes have been filled in: +++ your extra entry boxes here if they have to be filled in
        if School_Year == "" or Main_Travel_Method == "" or Allergies == "" or Medical_Conditions == "" or House_Number == "" or Road_Name == "" or Borough == "" or County == "" or Postcode == "" or Parent_Phone_Number == "" or Parent_Email_Address == "":
            Message = "Please make sure all boxes are filled in"    #Changes the message to reflect the error occurred
        elif First_Subject == Second_Subject:
            Message = "First and sceond subjects cannot be the same"    #Changes the message to reflect the error occurred
        else:
            #Creates a blank list to be placed into the function on the line below.
            #+++ your own entry boxes if they need to be words only
            To_Confirm = [Main_Travel_Method, Road_Name, Borough, County, Allergies, Medical_Conditions]
            Failed = self.hp.Check_Strings(To_Confirm)    #Runs a function in the helper class that checks each of the entries in the list above, making sure they are all words with only spaces or commas inbetween
            if Failed or not School_Year.isnumeric():    #Uses the checking function called above and a number check to make sure that the right characters are used in the entry boxes (letters or numbers)
                Message = "Invalid characters used"    #Changes the message to reflect the error occurred
            else:
                Postcode_Failed = False
                for character in Postcode:
                    if character != " " and not(character.isalpha() or character.isnumeric()):    #Checks to make sure the postcode contains only letter, number and space characters
                        Postcode_Failed = True
                if Postcode_Failed or len(Postcode) > 9:
                    Message = "Invalid postcode"    #Changes the message to reflect the error occurred
                else:
                    #Checks for an @ symbol, necessary for any email address
                    Necessary_Character_Found = False
                    for character in Parent_Email_Address:
                        if character == "@":
                            Necessary_Character_Found = True
                    if Necessary_Character_Found == False:
                        Message = "Email address needs a @ symbol"    #Changes the message to reflect the error occurred
                    else:
                        #Checks for any disallowed symbols in phone numbers (anything not a number or space)
                        Invalid_Character_Found = False
                        for character in Parent_Phone_Number:
                            if character.isnumeric() != True and character != " ":
                                Invalid_Character_Found = True
                        if Invalid_Character_Found == True:
                            Message = "Phone number cannot contain non-number characters"    #Changes the message to reflect the error occurred
                        else:
                            #This is currently the last validation check in the process - add your own by:
                            #+++, then adjust line below so that it doesn't automatically set Reject_Application to False
                            Reject_Application = False    #After all checks have passed, the checking variable is changed to reflect that the user has passed the validation checks

        #Edits the student's data if the checks have been passed
        if Reject_Application == False:
            #Retrieves any unchanges data fileds and organises certain data fields so that they can be placed into the database in the correct format
            #Add any extra special conditions here
            #-------------------------------
            Address1 = House_Number + "," + Road_Name
            Address2 = Borough + "," + County
            First_Name = self.Student_Detail.get("First_Name", "none")
            Last_Name = self.Student_Detail.get("Last_Name", "none")
            DOB = self.Student_Detail.get("DOB", "none")
            Parent_First_Name = self.Student_Detail.get("Parent_First_Name", "none")
            Parent_Last_Name = self.Student_Detail.get("Parent_Last_Name", "none")
            Student_ID = self.Student_Detail.get("ID", "none")
            #Collects all the student's details into a list: if extra data fields are added make sure to add the entry ox representing their details in the right spot (presumably at the end)
            Student_Detail = [First_Name, Last_Name, DOB, First_Subject, Second_Subject, School_Year, Main_Travel_Method, Allergies, Medical_Conditions, Address1, Address2, Postcode, Parent_First_Name, Parent_Last_Name, Parent_Phone_Number, Parent_Email_Address]
            self.sd.Update_Student(Student_Detail, Student_ID)    #Edits the data in the database by replacing the old data with the new data
            self.hp.Success_Window(Message)    #Displays a message box telling the user the data has been edited
        else:
            self.hp.Error_Window(Message)    #Displays a message box telling the user the data has not been edited, and describes what they have done wrong using the Message variable changed in the validation process

    #Provides the user with the option to cancel the removal of data before they do so, as the change is irreversible - no other validation is needed for this section
    def Confirm_Delete_Student_Screen(self):
        Name = str(self.Choosing_Name_Options_Label.get())    #Uses the name of the student record about to be deleted from the database
        #Checks to make sure a name has been selected
        if Name == "" or Name == "Choose a person to delete the data of:":
            self.hp.Error_Window("Please choose a name")
        else:
            #Creates a message box to display the confirmation message
            Confirm_Delete_Student = Tk()
            Confirm_Delete_Student.title("Are you sure?")
            Confirm_Delete_Student.config(bg = self.hp.Find_Colour("White"))
            Confirm_Delete_Student.geometry("350x100")

            Message = "Are you sure you want to delete the data of " + Name + "? This action cannot be undone."
            Confirm_Delete_Student_Icon = PhotoImage(master = Confirm_Delete_Student, file = "Error_Icon.gif")    #Adds a warning sign image to emphasise the nature of the decision
            Confirm_Delete_Student_Icon_Label = Label(Confirm_Delete_Student, image = Confirm_Delete_Student_Icon, bg = self.hp.Find_Colour("White"))
            Confirm_Delete_Student_Icon_Label.place(x = 5, y = 10)
            Confirm_Delete_Student_Message = Label(Confirm_Delete_Student, text = Message, bg = self.hp.Find_Colour("White"), font = ("Helvetica", 12), wraplength = 210)
            Confirm_Delete_Student_Message.place(x = 70, y = 15)

            #Creates the yes or no buttons - these will either delete the record or cancel the action respectively
            Yes_Button = Button(Confirm_Delete_Student, text = "Yes", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 12), command = lambda: self.Delete_Student(Confirm_Delete_Student, Name))
            Yes_Button.place(x = 280, y = 20, width = 50, height = 30)
            No_Button = Button(Confirm_Delete_Student, text = "No", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 12), command = lambda: self.Cancel_Action(Confirm_Delete_Student))
            No_Button.place(x = 280, y = 70, width = 50, height = 30)

            Confirm_Delete_Student.mainloop()

    #Removes the confirmation box and displays another box to tell the user their action was cancelled
    def Cancel_Action(self, Screen):
        Screen.destroy()
        self.hp.Error_Window("Action cancelled")

    #Deletes the student record from the database
    def Delete_Student(self, Screen, Name):
        Screen.destroy()    #Removes the confirmation screen
        Students = self.sd.Select_Students()    #Gathers all the student's data
        Student_Count = 0
        #Loops through each student record to find the right one
        for Student in Students:
            self.Student_Detail = Students[Student_Count]
            First_Name = self.Student_Detail.get("First_Name", "none")
            Last_Name = self.Student_Detail.get("Last_Name", "none")
            Student_Name = First_Name + " " + Last_Name
            if Student_Name == Name:    #Identifies which record has the name of the student to be deleted
                Student_ID = self.Student_Detail.get("ID", "none")
                self.sd.Delete_Student(Student_ID)    #Deletes the record with the correct student ID
                self.hp.Success_Window("Student deleted! Press 'Back' to continue.")    #Displays a message box telling the user the student record has been deleted
            Student_Count += 1

sd = Student_Operations()
