#imports key libraries
from tkinter import *
from sqlite3 import *
#imports other python files needed for program to work: adjust names accordingly and keep all files in the same folder
from Tutor_Database_Class import *
from Helper_Class import *
from Admin_Navigation_Class import *
from Tutor_Navigation_Class import *


#Handles the login screen and functionality
class Logging_In:

    #initialises the class and creates variables that can be used throughout the class
    def __init__(self):
        self.hp = Helper()   #creates an instance of the helper class as self.hp, allowing all the functions in the class to be used
        self.td = Tutor_Database()    #^
        self.Login = Tk()    #Creates a blank Tkinter screen called Login. The self. allows the screen to be called throughout the class
        self.size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Login)    #obtains screen dimensions
        self.Login.geometry(self.size)    #Changes the size of the Login screen to be the size of the entire monitor
        self.Login.title("Login")    #Replaces the default title of the screen to "Login"
        self.Login.config(bg = self.hp.Find_Colour("Light Blue"))    #changes the colour of the Tkinter screen to light blue
        self.Book_Image = PhotoImage(file = "Books.gif")    #creates an variable to store an image
        self.Login_Screen()    #calls the function below
        self.Login.mainloop()	#Loops the code to create the screen, updaing the screen and keeping the widgets on the screen for as long as it is open

    #Adds the widgets to the screen (widgets are anything added to the screen)
    def Login_Screen(self):

        Login_Title_Label = Label(self.Login, text = "Tuition Management System", font = ("Helvetica", 48), bg = self.hp.Find_Colour("Light Blue"), wraplength = 700)
        Login_Title_Label.place(x = (self.Screen_Width / 3), y = (self.Screen_Height / 2.6))

        Login_Frame = Frame(self.Login, bg = self.hp.Find_Colour("Blue"))
        Login_Frame.place(x = (self.Screen_Width / 2) - 125, y = self.Screen_Height/1.6, width = 300, height = 150)

        Login_Frame_Title_Frame = Frame(Login_Frame, bg = self.hp.Find_Colour("Green"))
        Login_Frame_Title_Frame.place(x = 0, y = 0, width = 300, height = 35)
        Login_Frame_Title_Label = Label(Login_Frame_Title_Frame, bg = self.hp.Find_Colour("Green"), text = "Login:", font = ("Helvetica", 20, "bold"))
        Login_Frame_Title_Label.place(x = 5, y = 0)

        Username_Label = Label(Login_Frame, text = "Username:", bg = self.hp.Find_Colour("Blue"), font = ("Helvetica", 16))
        Username_Label.place(x = 15, y = 55)
        self.Username_Entry = Entry(Login_Frame, font = ("Helvetica", 15))
        self.Username_Entry.place(x = 130, y = 55, width = 150, height = 25)

        Password_Label = Label(Login_Frame, text = "Password:", bg = self.hp.Find_Colour("Blue"), font = ("Helvetica", 16))
        Password_Label.place(x = 15, y = 100)
        self.Password_Entry = Entry(Login_Frame, font = ("Helvetica", 15), show="*")
        self.Password_Entry.place(x = 130, y = 100, width = 150, height = 25)

        Submit_Button = Button(self.Login, text = "Submit", bg = self.hp.Find_Colour("Grey"), font = ("Helvetica", 12), command = self.Login_Validation)
        Submit_Button.place(x = (self.Screen_Width / 2) + 100, y = (self.Screen_Height/1.6) + 150 ,width = 75, height = 35)

        Book_Image_Label = Label(self.Login, image = self.Book_Image)
        Book_Image_Label.place(x = (self.Screen_Width / 2.25), y = (self.Screen_Height / 12), width = 217, height = 222)

    #Runs a check on the login details entered by the user, making sure the username and corresponding password is in the database belonging to the same person
    def Login_Validation(self):
	#Retrieves username and password entered by the user
        Entered_Username = str(self.Username_Entry.get())
        Entered_Password = str(self.Password_Entry.get())
        Tutors = self.td.Select_Tutors()    #Gets a list of all the tutors in the database
        Passed = False    #A check variable, which will only return true if the details are valid
        for Tutor in Tutors:
            Username = str(Tutor.get("Username", "none"))
            Password = str(Tutor.get("Password", "none"))
            if Username == Entered_Username and Password == Entered_Password:	#checks if both entered values correspond to the same user
                Passed = True	#Validates the login attempt
                Status = str(Tutor.get("Status", "none"))    #gets the status of the user: this will be used later
                First_Name = str(Tutor.get("First_Name", "none"))
                Last_Name = str(Tutor.get("Last_Name", "none"))
                Tutor_Name = First_Name + " " + Last_Name
                break

        if Passed == True:
	    #The following if statement decides the path the user will take to enter the system depending on if they are a tutor or admin
            if Status == "Admin":
                anc = Admin_Navigation(self.Login, Status, self.Username_Entry, self.Password_Entry)
            else:
                tnc = Tutor_Navigation(self.Login, Tutor_Name, self.Username_Entry, self.Password_Entry)
        else:
            self.hp.Error_Window("Invalid Username or Password")    #brings up a popup box with the corresponding error message


#Runs the class above
def Login_main():
        log = Logging_In()

#Runs the function above - this method is needed to fix a memory loss error in the system
if __name__ == "__main__":
    Login_main()

