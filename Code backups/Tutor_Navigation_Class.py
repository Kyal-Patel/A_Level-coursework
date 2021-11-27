from tkinter import *
from Helper_Class import *
#Imports other python files that have been created in order for this program to connect to each of the screens
from Tuition_Management_System_Class import *
from Tutor_Rota_Viewer_Class import *

#This class contains the code that handles the processing and functionaliy of the tutor main screen
class Tutor_Navigation:
    def __init__(self, master, Tutor_Name, Username_Entry, Password_Entry):
        self.master = master    #master refers to the login screen
        self.master.withdraw()    #Hides the login screen - the user cannot access it but the screen is still loaded
                                  #This method is needed instead of destroying the screens to fix a memory issue

        self.Username_Entry = Username_Entry
        self.Password_Entry = Password_Entry

        self.hp = Helper()
        self.Tutor_Name = Tutor_Name

        self.Tutor_Main = Tk()    #Creates a new Tkinter screen called tutor_Main
        self.Size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Tutor_Main)    #obtains screen dimensions
        self.Tutor_Main.geometry(self.Size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.Tutor_Main.title("Tutor Main Screen")    #Replaces the default title of the screen to "tutor Main Screen"
        self.Tutor_Main.config(bg = self.hp.Find_Colour("Light Blue"))    #changes the colour of the Tkinter screen to light blue
        self.Tutor_Main_Screen()    #calls the function below

    #Adds widgets to screen - if any new screens are added that need direct links from the tutor main screen follow the syntax of the buttons below
    def Tutor_Main_Screen(self):
        Title_Frame = self.hp.Create_Title_Frame(self.Tutor_Main, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Welcome, tutor")

        View_Daily_Rota_Button = Button(self.Tutor_Main, text = "View today's rota", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 28), wraplength = 190, command = lambda: self.Proceed("View daily rota"))
        View_Daily_Rota_Button.place(x = self.Screen_Width / 4, y = self.Screen_Height / 3, width = 250, height = 120)

        View_Weekly_Rota_Button = Button(self.Tutor_Main, text = "View weekly rota", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 28), wraplength = 190, command = lambda: self.Proceed("View weekly rota"))
        View_Weekly_Rota_Button.place(x = self.Screen_Width / 1.7, y = self.Screen_Height / 3, width = 250, height = 120)

        Logout_Button = Button(self.Tutor_Main, text = "Sign out", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 28), command = lambda: self.Proceed("Logout"))
        Logout_Button.place(x = self.Screen_Width / 2.2, y = self.Screen_Height / 1.33, width = 175, height = 75)

    #Takes the user to their screen of choice - if any new screens are added that need direct links from the admin main screen put the link here
    def Proceed(self, Choice):
        if Choice == "View daily rota" or Choice == "View weekly rota":
            trv = Tutor_Rota_Viewer(Choice, self.Tutor_Name)
            pass
        elif Choice == "Logout":
            self.Tutor_Main.destroy()    #Removes the screen and wipes its memeory from it
            self.master.update()    #Refreshes the login Tkinter screen
            self.master.deiconify()    #Redraws the login window so that it can be used by the user
            #Deletes username and password and replaces it with blank characters to overwrite old username and password entry variables
            self.Username_Entry.delete(0, END)
            self.Username_Entry.insert(0, "")
            self.Password_Entry.delete(0, END)
            self.Password_Entry.insert(0, "")
