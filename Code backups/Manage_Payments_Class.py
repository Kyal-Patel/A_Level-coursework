

###########NO LONGER IMPLEMENTED###########


from tkinter import *
from Helper_Class import *

class Manage_Payments:
    def __init__(self):
        self.hp = Helper()
        self.Manage_Payments_Navigation = Tk()
        self.size, self.Screen_Width, self.Screen_Height = self.hp.Resize(self.Manage_Payments_Navigation)
        self.Manage_Payments_Navigation.geometry(self.size)
        self.Manage_Payments_Navigation.title("Manage payments navigation")
        self.Manage_Payments_Navigation.config(background = self.hp.Find_Colour("Light Blue"))
        self.Manage_Payments_Navigation_Screen()
        self.Manage_Payments_Navigation.mainloop()

    def Manage_Payments_Navigation_Screen(self):
        Title_Frame = self.hp.Create_Title_Frame(self.Manage_Payments_Navigation, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(Title_Frame, "Choose an option:")

        Back_Button = self.hp.Create_Back_Button(Title_Frame, self.Manage_Payments_Navigation)

        View_Outstanding_Payments_Button = Button(self.Manage_Payments_Navigation, bg = self.hp.Find_Colour("Grey"), text = "View outstanding payments", font = ("Helvetica",20), wraplength = 200, command = self.View_Outstanding_Payments_Screen)
        View_Outstanding_Payments_Button.place(x = self.Screen_Width / 6, y = self.Screen_Height / 3, width = 250, height = 100)

        Modify_Payments_Button = Button(self.Manage_Payments_Navigation, bg = self.hp.Find_Colour("Grey"), text = "Modify someone's payments", font = ("Helvetica",20), wraplength = 200)
        Modify_Payments_Button.place(x = self.Screen_Width / 1.6, y = self.Screen_Height / 3, width = 250, height = 100)

    def View_Outstanding_Payments_Screen(self):
        View_Outstanding_Payments = Tk()
        View_Outstanding_Payments.geometry(self.size)
        View_Outstanding_Payments.title("View outstanding payments")
        View_Outstanding_Payments.config(bg = self.hp.Find_Colour("Light Blue"))

        Title_Frame = self.hp.Create_Title_Frame(View_Outstanding_Payments, self.Screen_Width, self.Screen_Height)
        Title_Label = self.hp.Create_Title_Label(View_Outstanding_Payments, "The currently outstanding payments are:")
        Back_Button = self.hp.Create_Back_Button(Title_Frame, View_Outstanding_Payments)


        View_Outstanding_Payments.mainloop()

