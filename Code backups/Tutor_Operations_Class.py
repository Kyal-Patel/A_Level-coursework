from tkinter import *
from Helper_Class import *
from Tutor_Database_Class import *

#Handles any windows that occur after the admin presses "Manage tutor database" on the Admin_Main_Screen
class Tutor_Operations:
    def __init__(self, Status):
        self.hp = Helper()
        self.td = Tutor_Database()
        self.Status = Status

        self.Manage_Tutor_Database_Navigation = Tk()    #Creates a new Tkinter screen called Manage_tutor_Database_Navigation
        self.size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Manage_Tutor_Database_Navigation)    #obtains screen dimensions
        self.Manage_Tutor_Database_Navigation.geometry(self.size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.Manage_Tutor_Database_Navigation.title("Manage tutor database navigation")
        self.Manage_Tutor_Database_Navigation.config(background = self.hp.Find_Colour("Light Blue"))
        self.Manage_Tutor_Database_Navigation_Screen()
        self.Manage_Tutor_Database_Navigation.mainloop()

    #Adds widgets onto the first main screen created above
    def Manage_Tutor_Database_Navigation_Screen(self):
        Title_Frame = self.hp.Create_Title_Frame(self.Manage_Tutor_Database_Navigation, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Choose an option:")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.Manage_Tutor_Database_Navigation)

        Add_Tutor_Button = Button(self.Manage_Tutor_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Add a Tutor", font = ("Helvetica",20), command = self.Tutor_Creation_Screen)
        Add_Tutor_Button.place(x = (self.Screen_Width / 8), y = (self.Screen_Height / 3), width = 250, height = 100)

        Edit_Tutor_Button = Button(self.Manage_Tutor_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Edit a Tutor's data", font = ("Helvetica",20), wraplength = 200, command = self.Edit_Tutor_Data_Screen)
        Edit_Tutor_Button.place(x = (self.Screen_Width / 2.4), y = (self.Screen_Height / 3), width = 250, height = 100)

        Delete_Tutor_Button = Button(self.Manage_Tutor_Database_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Delete a Tutor", font = ("Helvetica",20), command = self.Delete_Tutor_Data_Screen)
        Delete_Tutor_Button.place(x = (self.Screen_Width / 1.4), y = (self.Screen_Height / 3), width = 250, height = 100)

    #Creates and adds widgets to a new Tkinter screen which will be used for adding a tutor record to the database
    def Tutor_Creation_Screen(self):
        #Creates the screen and sets general parameters for the screen
        Tutor_Creation = Tk()
        Tutor_Creation.title("Add an admin's data")
        Tutor_Creation.geometry(self.size)
        Tutor_Creation.config(bg = self.hp.Find_Colour("Light Blue"))

        Tutor_Creation_Title_Frame = self.hp.Create_Title_Frame(Tutor_Creation, self.Screen_Width, self.Screen_Height)
        Tutor_Creation_Title_Label = self.hp.Create_Title_Label(Tutor_Creation_Title_Frame, "Add a tutor")

        Back_Button = self.hp.Create_Back_Button(Tutor_Creation_Title_Frame, Tutor_Creation)

        #Sets the position of the first and second columns - these will be used to place the entry boxes in some of the screens
        First_Column_Entry_Position = self.Screen_Width / 5
        Second_Column_Entry_Position = self.Screen_Width / 1.6

        Down_Arrow = PhotoImage(master = Tutor_Creation, file = "Down_Arrow.gif")    #Creates an image widget to be used on the drop-down menus

        Name_Entry_Label = Label(Tutor_Creation, text = "Name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Name_Entry_Label.place(x = First_Column_Entry_Position - 100, y = (self.Screen_Height / 8), width = 90, height = 30)

        self.First_Name_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.First_Name_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 8), width = (self.Screen_Width/2) - (self.Screen_Width/4.5), height = 30)
        First_Name_Entry_Label = Label(Tutor_Creation, text = "First:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        First_Name_Entry_Label.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 8) - 25)
        First_Name_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        First_Name_Asterick.place(x = First_Column_Entry_Position + ((self.Screen_Width/2) - (self.Screen_Width/4.5)), y = (self.Screen_Height / 8) - 25)

        self.Last_Name_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Last_Name_Entry.place(x = Second_Column_Entry_Position - 150, y = (self.Screen_Height / 8), width = (self.Screen_Width/2) - (self.Screen_Width/4.5), height = 30)
        Last_Name_Entry_Label = Label(Tutor_Creation, text = "Last:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Last_Name_Entry_Label.place(x = Second_Column_Entry_Position - 150, y = (self.Screen_Height / 8) - 25)
        Last_Name_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Last_Name_Asterick.place(x = Second_Column_Entry_Position - 150 + (self.Screen_Width/2) - (self.Screen_Width/4.5), y = (self.Screen_Height / 8) - 25)

        DOB_Entry_Label = Label(Tutor_Creation, text = "D.O.B:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        DOB_Entry_Label.place(x = First_Column_Entry_Position - 100, y = (self.Screen_Height / 5), width = 90, height = 30)

        #Creates a drop-down menu for each day of the month

        #Creates a list of days to be used when the user selects their birth day
        Day_List = []
        for Day in range(1,32):
            Day_List.append(Day)
        self.Day_Of_Birth_Options_Label = StringVar(Tutor_Creation)    #Creates and configures a label to be used in the drop-down menus
        self.Day_Of_Birth_Options_Label.set("Choose one:")    #Sets a value for the label created on the line above
        self.Day_Of_Birth_Options = OptionMenu(Tutor_Creation, self.Day_Of_Birth_Options_Label,*Day_List)   #Creates a drop-down list with each day as a selectable option
        self.Day_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Day_Of_Birth_Options.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 5), width = 150, height = 30)
        Day_Of_Birth_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Day_Of_Birth_Asterick.place(x = First_Column_Entry_Position + 150, y = (self.Screen_Height / 5) - 25)
        Day_Of_Birth_Entry_Label = Label(Tutor_Creation, font = ("Helvetica", 12), bg = self.hp.Find_Colour("Light Blue"), text = "Day:")
        Day_Of_Birth_Entry_Label.place(x = First_Column_Entry_Position, y = (self.Screen_Height /5) - 25)
        Options = self.Day_Of_Birth_Options.nametowidget(self.Day_Of_Birth_Options.menuname)   #Retrieves the drop-down menu widget from the screen - this allows the font to be edited
        Options.configure(font = ("Helvetica", 12))    #Changes the font style and size of the text in the drop-down list

        #Same as the Day_Of_Birth drop-down menu above, but for months instead
        Month_List = []
        for Month in range(1,13):
            Month_List.append(Month)
        self.Month_Of_Birth_Options_Label = StringVar(Tutor_Creation)
        self.Month_Of_Birth_Options_Label.set("Choose one:")
        self.Month_Of_Birth_Options = OptionMenu(Tutor_Creation, self.Month_Of_Birth_Options_Label, *Month_List)
        self.Month_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"),font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Month_Of_Birth_Options.place(x = First_Column_Entry_Position + 250, y = (self.Screen_Height / 5), width = 150, height = 30)
        Month_Of_Birth_Entry_Label = Label(Tutor_Creation, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12), text = "Month:")
        Month_Of_Birth_Entry_Label.place(x = First_Column_Entry_Position + 250, y = (self.Screen_Height / 5) - 25)
        Month_Of_Birth_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Month_Of_Birth_Asterick.place(x = First_Column_Entry_Position + 250 + 150, y = (self.Screen_Height / 5) - 25)
        Options = self.Month_Of_Birth_Options.nametowidget(self.Month_Of_Birth_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but for years instead
        Year_List = []
        for Year in range(2019,1950, -1):    #Change range to alter the years displayed on screen
            Year_List.append(Year)
        self.Year_Of_Birth_Options_Label = StringVar(Tutor_Creation)
        self.Year_Of_Birth_Options_Label.set("Choose one:")
        self.Year_Of_Birth_Options = OptionMenu(Tutor_Creation, self.Year_Of_Birth_Options_Label, *Year_List)
        self.Year_Of_Birth_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Year_Of_Birth_Options.place(x = First_Column_Entry_Position + 250 + 150 + 100, y = (self.Screen_Height / 5), width = 150, height = 30)
        Year_Of_Birth_Entry_Label = Label(Tutor_Creation, text = "Year:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",12))
        Year_Of_Birth_Entry_Label.place(x = First_Column_Entry_Position + 250 + 150 + 100, y = (self.Screen_Height / 5) - 25)
        Year_Of_Birth_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Year_Of_Birth_Asterick.place(x = First_Column_Entry_Position + 250 + 150 + 100 + 150, y = (self.Screen_Height/5) - 25)
        Options = self.Year_Of_Birth_Options.nametowidget(self.Year_Of_Birth_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but uses a subject list created in the Helper_Class
        Primary_Subject_Entry_Label = Label(Tutor_Creation, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16), text = "Primary Subject:")
        Primary_Subject_Entry_Label.place(x = First_Column_Entry_Position - 175, y = (self.Screen_Height / 3.8))
        self.Primary_Subject_Options_Label = StringVar(Tutor_Creation)
        self.Primary_Subject_Options_Label.set("Choose one:")
        self.Primary_Subject_Options = OptionMenu(Tutor_Creation, self.Primary_Subject_Options_Label, *self.hp.Subject_List)
        self.Primary_Subject_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Primary_Subject_Options.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 320, height = 30)
        Primary_Subject_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Primary_Subject_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 3.8) - 25)
        Options = self.Primary_Subject_Options.nametowidget(self.Primary_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Same as the Day_Of_Birth drop-down menu above, but uses a subject list created in the Helper_Class
        Secondary_Subject_Entry_Label = Label(Tutor_Creation, bg = self.hp.Find_Colour("Light Blue"), text = "Secondary Subject:", font = ("Helvetica", 16))
        Secondary_Subject_Entry_Label.place(x = First_Column_Entry_Position - 205, y = (self.Screen_Height / 3.1))
        self.Secondary_Subject_Options_Label = StringVar(Tutor_Creation)
        self.Secondary_Subject_Options_Label.set("Choose one:")
        self.Secondary_Subject_Options = OptionMenu(Tutor_Creation, self.Secondary_Subject_Options_Label, *self.hp.Subject_List)
        self.Secondary_Subject_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = Down_Arrow)
        self.Secondary_Subject_Options.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 3.1), width = 320, height = 30)
        Options = self.Secondary_Subject_Options.nametowidget(self.Secondary_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))


        #Most chuncks of code from now to the end of this function add an entry box, label and asterick to the screen for each data field - add your own if necessary
        #When placing anything on the screen, the variables self.First_Column_Entry_Position and self.Second_Column_Entry_Position will be used to align the widgets


        self.Phone_Number_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Phone_Number_Entry.place(x = First_Column_Entry_Position , y = (self.Screen_Height / 2.6), height = 30, width = 320)
        Phone_Number_Entry_Label = Label(Tutor_Creation, text = "Phone Number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Phone_Number_Entry_Label.place(x = First_Column_Entry_Position - 170, y = (self.Screen_Height /2.6))
        Phone_Number_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Phone_Number_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.6) - 25)

        self.Email_Address_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Email_Address_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 2.25), width = 320, height = 30)
        Email_Address_Entry_Label = Label(Tutor_Creation, text = "Email Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Email_Address_Entry_Label.place(x = First_Column_Entry_Position - 165, y = (self.Screen_Height / 2.25))
        Email_Address_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Email_Address_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.25) - 25)

        self.Allergies_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Allergies_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 320, height = 30)
        Allergies_Entry_Label = Label(Tutor_Creation, text = "Allergies:", font = ("Helvetica", 16), bg = self.hp.Find_Colour("Light Blue"))
        Allergies_Entry_Label.place(x = First_Column_Entry_Position - 115, y = (self.Screen_Height / 1.95))
        Allergies_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Allergies_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.95) - 25)

        self.Medical_Conditions_Entry = Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Medical_Conditions_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 320, height = 30)
        Medical_Conditions_Entry_Label = Label(Tutor_Creation, text = "Medical Conditions:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Medical_Conditions_Entry_Label.place(x = First_Column_Entry_Position - 215, y = (self.Screen_Height / 1.75))
        Medical_Conditions_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Medical_Conditions_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.75) - 25)

        #Creates a label for the address, then adds several entry boxes for each part of the address
        self.Address_Entry_Label = Label(Tutor_Creation, text = "Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        self.Address_Entry_Label.place(x = Second_Column_Entry_Position - 100, y = (self.Screen_Height / 3.8))

        self.Home_Number_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Home_Number_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 100, height = 30)
        Home_Number_Entry_Label = Label(Tutor_Creation, text = "House number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Home_Number_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3.8) - 25)
        Home_Number_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Home_Number_Asterick.place(x = Second_Column_Entry_Position + 110, y = (self.Screen_Height / 3.8) - 25)

        self.Road_Name_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Road_Name_Entry.place(x = Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8), width = 220, height = 30)
        Road_Name_Entry_Label = Label(Tutor_Creation, text = "Road name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Road_Name_Entry_Label.place(x = Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8) - 25)
        Road_Name_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Road_Name_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3.8) - 25)

        self.Borough_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Borough_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3), width = 160, height = 30)
        Borough_Entry_Label = Label(Tutor_Creation, text = "Borough:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Borough_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3) - 25)
        Borough_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Borough_Asterick.place(x = Second_Column_Entry_Position + 160, y = (self.Screen_Height / 3) - 25)

        self.County_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.County_Entry.place(x = Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3), width = 165, height = 30)
        County_Entry_Label = Label(Tutor_Creation, text = "County:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        County_Entry_Label.place(x = Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3) - 25)
        County_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        County_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3) - 25)

        self.Postcode_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Postcode_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.5), width = 100, height = 30)
        Postcode_Entry_Label = Label(Tutor_Creation, text = "Postcode:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Postcode_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.5) - 25)
        Postcode_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Postcode_Asterick.place(x = Second_Column_Entry_Position + 100, y = (self.Screen_Height / 2.5) - 25)

        self.Username_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15))
        self.Username_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.2), width = 345, height = 30)
        Username_Entry_Label = Label(Tutor_Creation, text = "Username:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Username_Entry_Label.place(x = Second_Column_Entry_Position - 120, y = (self.Screen_Height / 2.2))
        Username_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Username_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 2.2) - 25)

        self.Password_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15), show="*")
        self.Password_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 345, height = 30)
        Password_Entry_Label = Label(Tutor_Creation, text = "Password:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Password_Entry_Label.place(x = Second_Column_Entry_Position - 120, y = (self.Screen_Height / 1.95))
        Password_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Password_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 1.95) - 25)

        self.Confirm_Password_Entry= Entry(Tutor_Creation, font = ("Helvetica", 15), show="*")
        self.Confirm_Password_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 345, height = 30)
        Confirm_Password_Entry_Label = Label(Tutor_Creation, text = "Confirm Password:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Confirm_Password_Entry_Label.place(x = Second_Column_Entry_Position - 195, y = (self.Screen_Height / 1.75))
        Confirm_Password_Asterick = self.hp.Create_Asterick(Tutor_Creation)
        Confirm_Password_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 1.75) - 25)

        #Adds a submit button - when pressed the details entered are checked by calling the Confirm_Tutor_Creation() function
        Submit_Button = Button(Tutor_Creation, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Tutor_Creation)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 1.4, width = 110)

        #Tells the user that all fields with astericks need to be filled in
        Asterick_Notice_Label = Label(Tutor_Creation, text = "* Required fields", bg = self.hp.Find_Colour("Light Blue"), fg = self.hp.Find_Colour("Dark Red"), font = ("Helvetica", 15))
        Asterick_Notice_Label.place(x = (self.Screen_Width / 1.3), y = self.Screen_Height / 1.4)

        Tutor_Creation.mainloop()

    #Creates and adds widgets to a new Tkinter screen which will be used for editing a tutor record already in the database
    def Edit_Tutor_Data_Screen(self):
        self.Edit_Tutor_Data = Tk()
        self.Edit_Tutor_Data.geometry(self.size)
        self.Edit_Tutor_Data.title("Edit a tutor's data")
        self.Edit_Tutor_Data.config(bg = self.hp.Find_Colour("Light Blue"))

        Title_Frame = self.hp.Create_Title_Frame(self.Edit_Tutor_Data, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Edit a tutor's data")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.Edit_Tutor_Data)

        self.Choosing_Name_Frame = Frame(self.Edit_Tutor_Data, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= self.hp.Find_Colour("Light Blue"), highlightcolor= self.hp.Find_Colour("Light Blue"), highlightthickness=1)
        self.Choosing_Name_Frame.place(x = self.Screen_Width / 2.5, y = self.Screen_Height / 9, width = 300, height = 30)

        #Gets all the tutor names from the database and organises it so it can be used in a drop-down list
        Tutors = self.td.Select_Tutors()
        Name_List = []
        Tutor_Count = 0
        for Tutor in Tutors:
            Tutor_Detail = Tutors[Tutor_Count]
            First_Name = Tutor_Detail.get("First_Name", "none")
            Last_Name = Tutor_Detail.get("Last_Name", "none")
            Tutor_Name = First_Name + " " + Last_Name
            Name_List.append(Tutor_Name)
            Tutor_Count += 1

        #Creates a drop-down menu similar to the Day_Of_Birth drop-down menu, described in lines 65-72
        self.Choosing_Name_Options_Label = StringVar(self.Choosing_Name_Frame)
        self.Choosing_Name_Options_Label.set("Choose a person to edit the data of:")
        self.Down_Arrow = PhotoImage(master = self.Choosing_Name_Frame, file = "Down_Arrow.gif")
        self.Choosing_Name_Options = OptionMenu(self.Choosing_Name_Frame, self.Choosing_Name_Options_Label, *Name_List,  command = self.Change_Screen)
        self.Choosing_Name_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 13),indicatoron = 0, compound = "right", image = self.Down_Arrow)
        self.Choosing_Name_Options.place(x = 0, y = 0, width = 300, height = 30)
        Options = self.Choosing_Name_Options.nametowidget(self.Choosing_Name_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        self.Edit_Tutor_Data.mainloop()

    #Changes the widgets on the screen when the user selects the name of the person they wish to edit the data of
    def Change_Screen(self, Name):
        self.Down_Arrow = PhotoImage(master = self.Edit_Tutor_Data, file = "Down_Arrow.gif")
        First_Column_Entry_Position = self.Screen_Width / 5
        Second_Column_Entry_Position = self.Screen_Width / 1.6

        #Extracts the record with the name of the selected person - if extra data fields are added then follow the format below
        Tutors = self.td.Select_Tutors()
        First_Subject = ""
        Second_Subject = ""
        Tutor_Count = 0
        for Tutor in Tutors:
            self.Tutor_Detail = Tutors[Tutor_Count]
            First_Name = self.Tutor_Detail.get("First_Name", "none")
            Last_Name = self.Tutor_Detail.get("Last_Name", "none")
            Tutor_Name = First_Name + " " + Last_Name
            if Tutor_Name == Name:
                Primary_Subject = self.Tutor_Detail.get("Primary_Subject", "none")
                Secondary_Subject = self.Tutor_Detail.get("Secondary_Subject", "none")
                Allergies = self.Tutor_Detail.get("Allergies", "none")
                Year_Group = self.Tutor_Detail.get("Year_Group", "none")
                Medical_Conditions = self.Tutor_Detail.get("Medical_Conditions", "none")
                Phone_Number = self.Tutor_Detail.get("Phone_Number", "none")
                Email_Address = self.Tutor_Detail.get("Email_Address", "none")
                Address1 = self.Tutor_Detail.get("Address1", "none")
                Address2 = self.Tutor_Detail.get("Address2", "none")
                Postcode = self.Tutor_Detail.get("Postcode", "none")
                Age = self.Tutor_Detail.get("Age", "none")
                Username = self.Tutor_Detail.get("Username", "none")
                Password = self.Tutor_Detail.get("Password", "none")
                Address1 = Address1.split(",")
                House_Number = Address1[0]
                Road_Name = Address1[1]
                Address2 = Address2.split(",")
                Borough = Address2[0]
                County = Address2[1]
                break
            Tutor_Count += 1

        #Creates a drop down menu for the tutor's first subject option choice - similar to lines 66-78
        Primary_Subject_Entry_Label = Label(self.Edit_Tutor_Data, bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16), text = "Primary Subject:")
        Primary_Subject_Entry_Label.place(x = First_Column_Entry_Position - 175, y = (self.Screen_Height / 3.8))
        self.Primary_Subject_Options_Label = StringVar(self.Edit_Tutor_Data)
        self.Primary_Subject_Options_Label.set(Primary_Subject)
        self.Primary_Subject_Options = OptionMenu(self.Edit_Tutor_Data, self.Primary_Subject_Options_Label, *self.hp.Subject_List)
        self.Primary_Subject_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = self.Down_Arrow)
        self.Primary_Subject_Options.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 320, height = 30)
        Primary_Subject_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Primary_Subject_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 3.8) - 25)
        Options = self.Primary_Subject_Options.nametowidget(self.Primary_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))

        #Creates a drop down menu for the tutor's first subject option choice - similar to lines 66-78
        Secondary_Subject_Entry_Label = Label(self.Edit_Tutor_Data, bg = self.hp.Find_Colour("Light Blue"), text = "Secondary Subject:", font = ("Helvetica", 16))
        Secondary_Subject_Entry_Label.place(x = First_Column_Entry_Position - 205, y = (self.Screen_Height / 3.1))
        self.Secondary_Subject_Options_Label = StringVar(self.Edit_Tutor_Data)
        self.Secondary_Subject_Options_Label.set(Secondary_Subject)
        Secondary_Subject_List = self.hp.Subject_List
        Secondary_Subject_List.append("None")
        self.Secondary_Subject_Options = OptionMenu(self.Edit_Tutor_Data, self.Secondary_Subject_Options_Label, *Secondary_Subject_List)
        self.Secondary_Subject_Options.config(bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica",13), indicatoron = 0, compound = "right", image = self.Down_Arrow)
        self.Secondary_Subject_Options.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 3.1), width = 320, height = 30)
        Options = self.Secondary_Subject_Options.nametowidget(self.Secondary_Subject_Options.menuname)
        Options.configure(font = ("Helvetica", 12))


        #Most chuncks of code from now to the end of this function add an entry box, label and asterick to the screen for each data field - add your own if necessary
        #When placing anything on the screen, the variables self.First_Column_Entry_Position and self.Second_Column_Entry_Position will be used to align the widgets


        self.Phone_Number_Entry = Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Phone_Number_Entry.insert(0,Phone_Number)
        self.Phone_Number_Entry.place(x = First_Column_Entry_Position , y = (self.Screen_Height / 2.6), height = 30, width = 320)
        Phone_Number_Entry_Label = Label(self.Edit_Tutor_Data, text = "Phone Number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Phone_Number_Entry_Label.place(x = First_Column_Entry_Position - 170, y = (self.Screen_Height /2.6))
        Phone_Number_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Phone_Number_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.6) - 25)

        self.Email_Address_Entry = Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Email_Address_Entry.insert(0, Email_Address)
        self.Email_Address_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 2.25), width = 320, height = 30)
        Email_Address_Entry_Label = Label(self.Edit_Tutor_Data, text = "Email Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Email_Address_Entry_Label.place(x = First_Column_Entry_Position - 165, y = (self.Screen_Height / 2.25))
        Email_Address_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Email_Address_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 2.25) - 25)

        self.Allergies_Entry = Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Allergies_Entry.insert(0,Allergies)
        self.Allergies_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 320, height = 30)
        Allergies_Entry_Label = Label(self.Edit_Tutor_Data, text = "Allergies:", font = ("Helvetica", 16), bg = self.hp.Find_Colour("Light Blue"))
        Allergies_Entry_Label.place(x = First_Column_Entry_Position - 115, y = (self.Screen_Height / 1.95))
        Allergies_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Allergies_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.95) - 25)

        self.Medical_Conditions_Entry = Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Medical_Conditions_Entry.insert(0, Medical_Conditions)
        self.Medical_Conditions_Entry.place(x = First_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 320, height = 30)
        Medical_Conditions_Entry_Label = Label(self.Edit_Tutor_Data, text = "Medical Conditions:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Medical_Conditions_Entry_Label.place(x = First_Column_Entry_Position - 215, y = (self.Screen_Height / 1.75))
        Medical_Conditions_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Medical_Conditions_Asterick.place(x = First_Column_Entry_Position + 320, y = (self.Screen_Height / 1.75) - 25)

        #Creates a label for the address, then adds several entry boxes for each part of the address
        self.Address_Entry_Label = Label(self.Edit_Tutor_Data, text = "Address:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        self.Address_Entry_Label.place(x = Second_Column_Entry_Position - 100, y = (self.Screen_Height / 3.8))

        self.Home_Number_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Home_Number_Entry.insert(0,House_Number)
        self.Home_Number_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3.8), width = 100, height = 30)
        Home_Number_Entry_Label = Label(self.Edit_Tutor_Data, text = "House number:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Home_Number_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3.8) - 25)
        Home_Number_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Home_Number_Asterick.place(x = Second_Column_Entry_Position + 110, y = (self.Screen_Height / 3.8) - 25)

        self.Road_Name_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Road_Name_Entry.insert(0,Road_Name)
        self.Road_Name_Entry.place(x = Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8), width = 220, height = 30)
        Road_Name_Entry_Label = Label(self.Edit_Tutor_Data, text = "Road name:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Road_Name_Entry_Label.place(x = Second_Column_Entry_Position + 125, y = (self.Screen_Height / 3.8) - 25)
        Road_Name_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Road_Name_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3.8) - 25)

        self.Borough_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Borough_Entry.insert(0,Borough)
        self.Borough_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3), width = 160, height = 30)
        Borough_Entry_Label = Label(self.Edit_Tutor_Data, text = "Borough:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Borough_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 3) - 25)
        Borough_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Borough_Asterick.place(x = Second_Column_Entry_Position + 160, y = (self.Screen_Height / 3) - 25)

        self.County_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.County_Entry.insert(0,County)
        self.County_Entry.place(x = Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3), width = 165, height = 30)
        County_Entry_Label = Label(self.Edit_Tutor_Data, text = "County:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        County_Entry_Label.place(x = Second_Column_Entry_Position + 180, y = (self.Screen_Height / 3) - 25)
        County_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        County_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 3) - 25)

        self.Postcode_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Postcode_Entry.insert(0,Postcode)
        self.Postcode_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.5), width = 100, height = 30)
        Postcode_Entry_Label = Label(self.Edit_Tutor_Data, text = "Postcode:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 12))
        Postcode_Entry_Label.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.5) - 25)
        Postcode_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Postcode_Asterick.place(x = Second_Column_Entry_Position + 100, y = (self.Screen_Height / 2.5) - 25)

        self.Username_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15))
        self.Username_Entry.insert(0,Username)
        self.Username_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 2.2), width = 345, height = 30)
        Username_Entry_Label = Label(self.Edit_Tutor_Data, text = "Username:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Username_Entry_Label.place(x = Second_Column_Entry_Position - 120, y = (self.Screen_Height / 2.2))
        Username_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Username_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 2.2) - 25)

        self.Password_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15), show="*")
        self.Password_Entry.insert(0,Password)
        self.Password_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 1.95), width = 345, height = 30)
        Password_Entry_Label = Label(self.Edit_Tutor_Data, text = "Password:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Password_Entry_Label.place(x = Second_Column_Entry_Position - 120, y = (self.Screen_Height / 1.95))
        Password_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Password_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 1.95) - 25)

        self.Confirm_Password_Entry= Entry(self.Edit_Tutor_Data, font = ("Helvetica", 15), show="*")
        self.Confirm_Password_Entry.insert(0,Password)
        self.Confirm_Password_Entry.place(x = Second_Column_Entry_Position, y = (self.Screen_Height / 1.75), width = 345, height = 30)
        Confirm_Password_Entry_Label = Label(self.Edit_Tutor_Data, text = "Confirm Password:", bg = self.hp.Find_Colour("Light Blue"), font = ("Helvetica", 16))
        Confirm_Password_Entry_Label.place(x = Second_Column_Entry_Position - 195, y = (self.Screen_Height / 1.75))
        Confirm_Password_Asterick = self.hp.Create_Asterick(self.Edit_Tutor_Data)
        Confirm_Password_Asterick.place(x = Second_Column_Entry_Position + 345, y = (self.Screen_Height / 1.75) - 25)

        Submit_Button = Button(self.Edit_Tutor_Data, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Edit_Tutor)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 1.4, width = 110)

    #Creates and adds widgets to a new Tkinter screen which will be used for deleting a tutor's data
    def Delete_Tutor_Data_Screen(self):
        Delete_Tutor_Data = Tk()
        Delete_Tutor_Data.geometry(self.size)
        Delete_Tutor_Data.title("Delete a tutor's data")
        Delete_Tutor_Data.config(bg = self.hp.Find_Colour("Light Blue"))

        Title_Frame = self.hp.Create_Title_Frame(Delete_Tutor_Data, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Delete a tutor's data")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, Delete_Tutor_Data)

        First_Column_Entry_Position = self.Screen_Width / 5
        Second_Column_Entry_Position = self.Screen_Width / 1.6

        self.Choosing_Name_Frame = Frame(Delete_Tutor_Data, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= self.hp.Find_Colour("Light Blue"), highlightcolor= self.hp.Find_Colour("Light Blue"), highlightthickness=1)
        self.Choosing_Name_Frame.place(x = self.Screen_Width / 2.5, y = self.Screen_Height / 9, width = 300, height = 30)

        #Gets all the tutor names from the database and organises it so it can be used in a drop-down list
        Tutors = self.td.Select_Tutors()
        Name_List = []
        Tutor_Count = 0
        for Tutor in Tutors:
            Tutor_Detail = Tutors[Tutor_Count]
            First_Name = Tutor_Detail.get("First_Name", "none")
            Last_Name = Tutor_Detail.get("Last_Name", "none")
            Tutor_Name = First_Name + " " + Last_Name
            Name_List.append(Tutor_Name)
            Tutor_Count += 1

        self.Choosing_Name_Frame = Frame(Delete_Tutor_Data, bg = self.hp.Find_Colour("Light Blue"), highlightbackground= self.hp.Find_Colour("Light Blue"), highlightcolor= self.hp.Find_Colour("Light Blue"), highlightthickness=1)
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

        Submit_Button = Button(Delete_Tutor_Data, bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 20), text = "Submit", command = self.Confirm_Delete_Tutor_Screen)
        Submit_Button.place(x = (self.Screen_Width / 2) - 55 , y = self.Screen_Height / 2, width = 110)

        Delete_Tutor_Data.mainloop()

    #Runs the validation process for adding a student record - this will run after the user presses "Submit" and will show a popup box for the result of the process
    def Confirm_Tutor_Creation(self):
        #Gets all the entries the user has provided, then sets their format depending on how they will be stored in the database (e.g: .upper for postcodes, .capitalise for names etc)
        #for each data field - add your own if necessary
        First_Name = str(self.First_Name_Entry.get().lower().capitalize())
        Last_Name = str(self.Last_Name_Entry.get().lower().capitalize())
        Day_Of_Birth = str(self.Day_Of_Birth_Options_Label.get())
        Month_Of_Birth = str(self.Month_Of_Birth_Options_Label.get())
        Year_Of_Birth = str(self.Year_Of_Birth_Options_Label.get())
        Primary_Subject = str(self.Primary_Subject_Options_Label.get())
        Secondary_Subject = str(self.Secondary_Subject_Options_Label.get())
        Phone_Number = str(self.Phone_Number_Entry.get()).lower().capitalize()
        Email_Address = str(self.Email_Address_Entry.get()).lower().capitalize()
        Allergies = str(self.Allergies_Entry.get()).lower().capitalize()
        Medical_Conditions = str(self.Medical_Conditions_Entry.get()).lower().capitalize()
        House_Number = str(self.Home_Number_Entry.get())
        Road_Name = str(self.Road_Name_Entry.get().lower().capitalize())
        Borough = str(self.Borough_Entry.get().lower().capitalize())
        County = str(self.County_Entry.get().lower().capitalize())
        Postcode = str(self.Postcode_Entry.get().upper())
        Username = str(self.Username_Entry.get())
        Password = str(self.Password_Entry.get())
        Confirm_Password = str(self.Confirm_Password_Entry.get())
        DOB = Day_Of_Birth + "/" + Month_Of_Birth + "/" + Year_Of_Birth

        #Organises certain aspects of the data to be stored into the database - add any other special conditions for formatting here
        if Secondary_Subject == "Choose one:":
            Secondary_Subject = "N/A"
        Address1 = House_Number + "," + Road_Name
        Address2 = Borough + "," + County
        Age = "N/A"

        #Checks if each of the individual criteria is met - add your own criteria after the line marked with a +++
        Reject_Application = True    #Defaults a checking variable to (invalid) - Validation rejected until otherwise stated
        Message = "Application sucessful"    #Sets the message to be displayed at the end of the process - this is at default a pass so it can be used to see when an error has been picked up
        while Message == "Application sucessful":
             #Checks to make sure all necessary entry boxes have been filled in: +++ your extra entry boxes here if they have to be filled in
             if First_Name == "" or Last_Name == "" or Day_Of_Birth == "Choose one:" or Month_Of_Birth == "Choose one:" or Year_Of_Birth == "Choose one:" or Primary_Subject == "Choose one:" or Phone_Number == "" or Email_Address == "" or Allergies == "" or Medical_Conditions == "" or House_Number == "" or Road_Name == "" or Borough == "" or County == "" or Postcode == "" or Username == "" or Password == "" or Confirm_Password == "":
                Message = "Please fill in all entry boxes"    #Changes the message to reflect the error occurred
             else:
                #Creates a blank list to be placed into the function on the line below.
                #+++ your own entry boxes if they need to be words only
                To_Confirm = [First_Name, Last_Name, Primary_Subject, Secondary_Subject, Allergies, Medical_Conditions, Road_Name, Borough, County]
                Failed = self.hp.Check_Strings(To_Confirm)    #Runs a function in the helper class that checks each of the entries in the list above, making sure they are all words with only spaces or commas inbetween
                if Failed:    #Uses the checking function called above to make sure that the right characters are used in the entry boxes (letters or numbers)
                    Message = "Invalid characters used"    #Changes the message to reflect the error occurred
                else:
                    if Primary_Subject == Secondary_Subject:    #Checks to make sure that two seperate subjects are chosen
                        Message = "Primary and secondary subjects cannot be the same"    #Changes the message to reflect the error occurred
                    elif Password != Confirm_Password:
                        Message = "Please make sure your password is correct"    #Changes the message to reflect the error occurred
                    else:
                        Postcode_Failed = False
                        for character in Postcode:
                            if character != " " and not(character.isalpha() or character.isnumeric()):    #Checks to make sure the postcode contains only letter, number and space characters
                                Postcode_Failed = True
                        if len(Postcode) > 10 or Postcode_Failed:    #Checks to make sure the postcode contains the right characters (from above) and that the postcode is not beyond the postcode size limit
                            Message = "Postcode is invalid"    #Changes the message to reflect the error occurred
                        else:
                            #Checks for an @ symbol, necessary for any email address
                            Necessary_Character_Found = False
                            for character in Email_Address:
                                if character == "@":
                                    Necessary_Character_Found = True
                            if Necessary_Character_Found == False:
                                Message = "Email address needs a @ symbol"    #Changes the message to reflect the error occurred
                            else:
                                #Checks for any disallowed symbols in phone numbers (anything not a number or space)
                                Invalid_Character_Found = False
                                for character in Phone_Number:
                                    if character.isnumeric() != True and character != " ":
                                        Invalid_Character_Found = False
                                if Invalid_Character_Found == True:
                                    Message = "Phone number cannot contain non-number characters"    #Changes the message to reflect the error occurred
                                else:
                                    #Checks to make sure the birthday entered exists (i.e: Not February 31st)
                                    Valid_Birthday = self.hp.Check_Birthday(Day_Of_Birth, Month_Of_Birth, Year_Of_Birth)    #Calls a function in the helper class to check the birthday
                                    if Valid_Birthday:
                                        #This is currently the last validation check in the process - add your own by:
                                        #+++, then adjust line below so that it doesn't automatically set Reject_Application to False
                                        Reject_Application = False    #After all checks have passed, the checking variable is changed to reflect that the user has passed the validation checks
                                    else:
                                        Message = "Invalid date of birth"    #Changes the message to reflect the error occurred
             break

        #Adds the student to the database if the validation has returned positive
        if Reject_Application == False:
            #Collects all the tutor's details into a list: if extra data fields are added make sure to add the entry ox representing their details in the right spot (presumably at the end)
            Tutor_Detail = [First_Name, Last_Name, DOB, Age, Primary_Subject, Secondary_Subject, Phone_Number, Email_Address, Allergies, Medical_Conditions, Address1, Address2, Postcode, Username, Password, "Tutor"]
            self.td.Insert_Tutor(Tutor_Detail)    #Adds the tutor record into the database
            self.hp.Success_Window("Tutor added!")    #Displays a message box telling the user the tutor has been added
        else:
            self.hp.Error_Window(Message)    #Displays a message box telling the user the tutor has not been added, and describes what they have done wrong using the Message variable changed in the validation process


    #Runs the validation process for editing a tutor record - this will run after the user presses "Submit" and will show a popup box for the result of the process
    #Note that a lot of this function will be a repeat from Confirm_Tutor_Creation(), so the code for validating and retrieving any entry boxes you add that can be edited can be copied and pasted
    def Confirm_Edit_Tutor(self):
        #Gets all the entries the user has provided, then sets their format depending on how they will be stored in the database (e.g: .upper for postcodes, .capitalise for names etc)
        #for each data field - add your own if necessary
        Primary_Subject = str(self.Primary_Subject_Options_Label.get())
        Secondary_Subject = str(self.Secondary_Subject_Options_Label.get())
        Phone_Number = str(self.Phone_Number_Entry.get()).lower().capitalize()
        Email_Address = str(self.Email_Address_Entry.get())
        Allergies = str(self.Allergies_Entry.get()).lower().capitalize()
        Medical_Conditions = str(self.Medical_Conditions_Entry.get()).lower().capitalize()
        House_Number = str(self.Home_Number_Entry.get())
        Road_Name = str(self.Road_Name_Entry.get().lower().capitalize())
        Borough = str(self.Borough_Entry.get().lower().capitalize())
        County = str(self.County_Entry.get().lower().capitalize())
        Postcode = str(self.Postcode_Entry.get().upper())
        Username = str(self.Username_Entry.get())
        Password = str(self.Password_Entry.get())
        Confirm_Password = str(self.Confirm_Password_Entry.get())

        #Checks if each of the individual criteria is met - add your own criteria after the line marked with a +++

        Reject_Application = True    #Defaults a checking variable to (invalid) - Validation rejected until otherwise stated
        Message = "Changes sucessful"    #Sets the message to be displayed at the end of the process - this is at default a pass so it can be used to see when an error has been picked up
        #Checks to make sure all necessary entry boxes have been filled in: +++ your extra entry boxes here if they have to be filled in
        if Primary_Subject == "" or Phone_Number == "" or Email_Address == "" or Allergies == "" or Medical_Conditions == "" or House_Number == "" or Road_Name == "" or Borough == "" or County == "" or Postcode == "" or Username == "" or Password == "" or Confirm_Password == "":
            Message = "Please fill in all boxes marked with a *"    #Changes the message to reflect the error occurred
        elif Password != Confirm_Password:
            Message = "Please confirm your password"    #Changes the message to reflect the error occurred
        elif Primary_Subject == Secondary_Subject:
            Message = "Primary and secondary subjects cannot be the same"    #Changes the message to reflect the error occurred
        else:
            Postcode_Failed = False
            for character in Postcode:
                if character != " " and not(character.isalpha() or character.isnumeric()):    #Checks to make sure the postcode contains only letter, number and space characters
                    Postcode_Failed = True
            if len(Postcode) > 8 or Postcode_Failed:
                Message = "Postcode is invalid"    #Changes the message to reflect the error occurred
            else:
                #Checks for an @ symbol, necessary for any email address
                Necessary_Character_Found = False
                for character in Email_Address:
                    if character == "@":
                        Necessary_Character_Found = True
                if Necessary_Character_Found == False:
                    Message = "Email address needs a @ symbol"    #Changes the message to reflect the error occurred
                else:
                    #Checks for any disallowed symbols in phone numbers (anything not a number or space)
                    Invalid_Character_Found = False
                    for character in Phone_Number:
                        if character.isnumeric() != True and character != " ":
                            Invalid_Character_Found = False
                    if Invalid_Character_Found == True:
                        Message = "Phone number cannot contain non-number characters"    #Changes the message to reflect the error occurred
                    else:
                        #Creates a blank list to be placed into the function on the line below.
                        #+++ your own entry boxes if they need to be words only
                        To_Confirm = [Allergies, Medical_Conditions, Road_Name, Borough, County]
                        Failed = self.hp.Check_Strings(To_Confirm)    #Runs a function in the helper class that checks each of the entries in the list above, making sure they are all words with only spaces or commas inbetween
                        if Failed or House_Number.isnumeric() == False:
                            Message = "Invalid characters used"    #Changes the message to reflect the error occurred
                        else:
                            #This is currently the last validation check in the process - add your own by:
                            #+++, then adjust line below so that it doesn't automatically set Reject_Application to False
                            Reject_Application = False    #After all checks have passed, the checking variable is changed to reflect that the user has passed the validation checks

        #Edits the tutor's data if the checks have been passed
        if Reject_Application == False:
            #Retrieves any unchanges data fileds and organises certain data fields so that they can be placed into the database in the correct format
            #Add any extra special conditions here
            #-------------------------------
            Address1 = House_Number + "," + Road_Name
            Address2 = Borough + "," + County
            Age = "N/A"
            First_Name = self.Tutor_Detail.get("First_Name", "none")
            Last_Name = self.Tutor_Detail.get("Last_Name", "none")
            DOB = self.Tutor_Detail.get("DOB", "none")
            Status = self.Tutor_Detail.get("Status", "none")
            Tutor_ID = self.Tutor_Detail.get("ID", "none")
            #Collects all the student's details into a list: if extra data fields are added make sure to add the entry ox representing their details in the right spot (presumably at the end)
            Tutor_Detail = [First_Name, Last_Name, DOB, Age, Primary_Subject, Secondary_Subject, Phone_Number, Email_Address, Allergies, Medical_Conditions, Address1, Address2, Postcode, Username, Password, Status]
            self.td.Update_Tutor(Tutor_Detail, Tutor_ID)    #Edits the data in the database by replacing the old data with the new data
            self.hp.Success_Window(Message)    #Displays a message box telling the user the data has been edited
        else:
            self.hp.Error_Window(Message)    #Displays a message box telling the user the data has not been edited, and describes what they have done wrong using the Message variable changed in the validation process

    #Provides the user with the option to cancel the removal of data before they do so, as the change is irreversible - no other validation is needed for this section
    def Confirm_Delete_Tutor_Screen(self):
        Name = str(self.Choosing_Name_Options_Label.get())    #Uses the name of the tutor record about to be deleted from the database

        if Name == "" or Name == "Choose a person to delete the data of:":
            self.hp.Error_Window("Please choose a name")
        else:
        
            #Creates a message box to display the confirmation message
            Confirm_Delete_Tutor = Tk()
            Confirm_Delete_Tutor.title("Are you sure?")
            Confirm_Delete_Tutor.config(bg = self.hp.Find_Colour("White"))
            Confirm_Delete_Tutor.geometry("350x100")

            Message = "Are you sure you want to delete the data of " + Name + "? This action cannot be undone."
            Confirm_Delete_Tutor_Icon = PhotoImage(master = Confirm_Delete_Tutor, file = "Error_Icon.gif")    #Adds a warning sign image to emphasise the nature of the decision
            Confirm_Delete_Tutor_Icon_Label = Label(Confirm_Delete_Tutor, image = Confirm_Delete_Tutor_Icon, bg = self.hp.Find_Colour("White"))
            Confirm_Delete_Tutor_Icon_Label.place(x = 5, y = 10)
            Confirm_Delete_Tutor_Message = Label(Confirm_Delete_Tutor, text = Message, bg = self.hp.Find_Colour("White"), font = ("Helvetica", 12), wraplength = 210)
            Confirm_Delete_Tutor_Message.place(x = 70, y = 15)

            #Creates the yes or no buttons - these will either delete the record or cancel the action respectively
            Yes_Button = Button(Confirm_Delete_Tutor, text = "Yes", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 12), command = lambda: self.Delete_Tutor(Confirm_Delete_Tutor, Name))
            Yes_Button.place(x = 280, y = 20, width = 50, height = 30)
            No_Button = Button(Confirm_Delete_Tutor, text = "No", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 12), command = lambda: self.Cancel_Action(Confirm_Delete_Tutor))
            No_Button.place(x = 280, y = 70, width = 50, height = 30)


            Confirm_Delete_Tutor.mainloop()

    #Removes the confirmation box and displays another box to tell the user their action was cancelled
    def Cancel_Action(self, Screen):
        Screen.destroy()
        self.hp.Error_Window("Action cancelled")

    #Deletes the tutor record from the database
    def Delete_Tutor(self, Screen, Name):
        Screen.destroy()    #Removes the confirmation screen
        Tutors = self.td.Select_Tutors()    #Gathers all the tutor's data
        Tutor_Count = 0
        for Tutor in Tutors:    #Loops through each student record to find the right one
            self.Tutor_Detail = Tutors[Tutor_Count]
            First_Name = self.Tutor_Detail.get("First_Name", "none")
            Last_Name = self.Tutor_Detail.get("Last_Name", "none")
            Tutor_Name = First_Name + " " + Last_Name
            if Tutor_Name == Name:    #Identifies which record has the name of the student to be deleted
                Tutor_ID = self.Tutor_Detail.get("ID", "none")
                self.td.Delete_Tutor(Tutor_ID)    #Deletes the record with the correct student ID
                self.hp.Success_Window("Tutor deleted! Press 'Back' to continue.")    #Displays a message box telling the user the student record has been deleted
            Tutor_Count += 1

to = Tutor_Operations("Admin")
