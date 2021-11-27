from tkinter import *
from Helper_Class import *
#Imports other python files that have been created in order for this program to connect to each of the screens
from Tutor_Operations_Class import *
from Student_Operations_Class import *
from Manage_Payments_Class import *
from Lesson_Plan_Management_Class import *
from Tuition_Management_System_Class import *
from Tutor_Data_Viewer_Class import *
from Student_Data_Viewer_Class import *

#This class contains the code that handles the processing and functionaliy of the admin main screen
class Admin_Navigation:

    def __init__(self, master, Status, Username_Entry, Password_Entry):    #master refers to the login screen
        self.Username_Entry = Username_Entry
        self.Password_Entry = Password_Entry
        self.master = master
        self.master.withdraw()    #Hides the login screen - the user cannot access it but the screen is still loaded
                                  #This method is needed instead of destroying the screens to fix a memory issue
        self.hp = Helper()
        self.Status = Status

        self.Admin_Main = Tk()    #Creates a new Tkinter screen called Admin_Main
        self.size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Admin_Main)    #obtains screen dimensions
        self.Admin_Main.geometry(self.size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.Admin_Main.title("Admin Main Screen")    #Replaces the default title of the screen to "Admin Main Screen"
        self.Admin_Main.config(bg = self.hp.Find_Colour("Light Blue"))    #changes the colour of the Tkinter screen to light blue
        self.Admin_Main_Screen()    #calls the function below


    #Adds widgets to screen - if any new screens are added that need direct links from the admin main screen follow the syntax of the buttons below
    def Admin_Main_Screen(self):

        Title_Frame = self.hp.Create_Title_Frame(self.Admin_Main, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Welcome, admin")

        View_Tutors_Button = Button(self.Admin_Main, text = "View tutor database", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("View tutor database"))
        View_Tutors_Button.place(x = (self.Screen_Width / 6) - 50, y = self.Screen_Height / 2, width = 250, height = 120)

        View_Students_Button = Button(self.Admin_Main, text = "View student database", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("View student database"))
        View_Students_Button.place(x = (self.Screen_Width / 6) - 50, y = self.Screen_Height / 6, width = 250, height = 120)

        Manage_Students_Button = Button(self.Admin_Main, text = "Manage student database", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("Manage student database"))
        Manage_Students_Button.place(x = (self.Screen_Width / 2) - 125, y = self.Screen_Height / 6, width = 250, height = 120)

        Manage_Tutors_Button = Button(self.Admin_Main, text = "Manage tutor database", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("Manage tutor database"))
        Manage_Tutors_Button.place(x = (self.Screen_Width / 2) - 125, y = self.Screen_Height / 2, width = 250, height = 120)

        View_Lessons_Button = Button(self.Admin_Main, text = "Manage lesson plan", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("Manage lesson plan"))
        View_Lessons_Button.place(x = (self.Screen_Width / 1.33) - 50, y = self.Screen_Height / 6, width = 250, height = 120)

##        Manage_Payments_Button = Button(self.Admin_Main, text = "Manage student payments", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica",28), wraplength = 190, command = lambda: self.Proceed("Manage student payments"))
##        Manage_Payments_Button.place(x = (self.Screen_Width / 1.33) - 50, y = self.Screen_Height / 2, width = 250, height = 120)

        Sign_Out_Button = Button(self.Admin_Main, text = "Sign out", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 28), command = lambda: self.Proceed("Sign out"))
        Sign_Out_Button.place(x = (self.Screen_Width / 2) - 85, y = self.Screen_Height / 1.33, width = 175, height = 75)

    #Takes the user to their screen of choice - if any new screens are added that need direct links from the admin main screen put the link here
    def Proceed(self, choice):
        if choice == "Manage student database":
            so = Student_Operations()
        elif choice == "Manage lesson plan":
            lpm = Lesson_Plan_Management()
        elif choice == "Manage tutor database":
            to = Tutor_Operations(self.Status)
##        elif choice == "Manage student payments":   #Idea scrapped so code related to this has been greyed out - can replace name if another functionality is added
##            mp = Manage_Payments()
        elif choice == "View tutor database":
            tdv = Tutor_Data_Viewer()
        elif choice == "View student database":
            sdv = Student_Data_Viewer()
        elif choice == "Sign out":
            self.Admin_Main.destroy()    #Removes the screen and wipes its memeory from it
            self.master.update()    #Refreshes the login Tkinter screen
            self.master.deiconify()    #Redraws the login window so that it can be used by the user
            #Deletes username and password and replaces it with blank characters to overwrite old username and password entry variables
            self.Username_Entry.delete(0, END)
            self.Username_Entry.insert(0, "")
            self.Password_Entry.delete(0, END)
            self.Password_Entry.insert(0, "")


