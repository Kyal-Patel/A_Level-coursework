from tkinter import *
from tkinter import font

#Add any functions used multiple times throughout different python files in this class in the space provided
class Helper:
    def __init__(self):
	#Creates a dictionary of colours and their respective colour codes - add any custom colours to this
        self.Colour_List = {
            "Light Blue" : "#ADD8E6",
            "Green" : "#66CC00",
            "Grey" : "#E6E6E6",
            "Dark Red" : "#CC0000",
            "Red" : "#FF0000",
            "Dark Orange": "#FF8C00",
            "Gold" : "#FFD700",
            "Deep Sky Blue" : "#00BFFF",
            "Black" : "#000000",
            "Blue" : "#007FFF",
            "White" : "#FFFFFF",
            "Dark Grey" : "#696969"
            }
        #A list of subjects in the tuition centre - add any other/new subjects to this list
        self.Subject_List = ["Maths", "Computer Science", "English", "Triple Sciences", "Double Sciences"]

    #Use this function to retrieve the colour from the dictionary you need
    def Find_Colour(self, Colour):
        found = self.Colour_List.get(Colour, "none")
        return found

    #Finds and returns the dimensions of the monitor you are using
    def Resize(self, window):
        m = window.maxsize()    #Gets the maximum possible size of the Tkinter window - this will be the size of the monitor screen
        width, height = m
        size = str(width)+"x"+str(height)     #Creates a phrase for Tkinter to use to change the screen size
        return size, width, height

    #Adds an asterick to the screen
    def Create_Asterick(self, Screen):
        Asterick = Label(Screen, text = "*", font = ("Helvetica", 15), bg = self.Find_Colour("Light Blue"), fg = self.Find_Colour("Dark Red"))
        return Asterick

    #Adds a frame to put a visible title into
    def Create_Title_Frame(self, Screen, Width, Height):
        Title_Frame = Frame(Screen, bg = self.Find_Colour("Green"))
        Title_Frame.place(x = 0, y = 0, width = Width, height = 65)
        return Title_Frame

    #Adds a visible title to the screen in the frame created above
    def Create_Title_Label(self, Back_Frame, text):
        Title_Label = Label(Back_Frame, text = text, font = ("Helvetica", 36, "bold"), bg = self.Find_Colour("Green"))
        Title_Label.pack(fill = X)
        return Title_Label

    #Adds a back button to the screen
    def Create_Back_Button(self, Back_Frame, Screen):
        Back_Button = Button(Back_Frame, text = "Back", bg = self.Find_Colour("Green"), font = ("Helvetica", 24), command = Screen.destroy)
        Back_Button.place(x = 0, y = 0, width = 125, height = 65)
        return Back_Button

    #Used for validating some of the user's inputs: checks to make sure the input is a letter-only word or has spaces/commas for adding multiple values in the same input
    def Check_Strings(self, words):
        Failed = False
        for word in words:
            for character in word:
                if character.isalpha() == False and character != " " and character != ",":
                    Failed = True
        return Failed

    #Used to make sure that a valid birthday is used (e.g: 31st February will not be valid)
    def Check_Birthday(self, Day, Month, Year):
        Long_Months = ["January", "March", "May", "July", "August", "October", "December"]
        Less_Long_Months = ["September", "April", "June", "November"]
        Is_Leap_Year = False
        Day = int(Day)
        Year = int(Year)
        if Month in Long_Months:
            Valid_Birthday = True
        elif Month in Less_Long_Months:
            if Day == 31:
                Valid_Birthday = False
            else:
                Valid_Birthday = True
        else:
	    #Takes into account leap years
            if Year % 4 == 0 and not(Year % 100 == 0 and Year % 400 != 0):
                Is_Leap_Year = True

            if Is_Leap_Year and Day <= 29:
                Valid_Birthday = True
            elif not Is_Leap_Year and Day < 29:
                Valid_Birthday = True
            else:
                Valid_Birthday = False

        return Valid_Birthday

    #Used to create an error message popup
    def Error_Window(self, Error_Text):
        Error_Message_Window = Tk()
        self.Error_Icon= PhotoImage(master = Error_Message_Window, file = "Error_Icon.gif")
        Error_Message_Window.title(" ")
        Error_Message_Window.config(bg = self.Find_Colour("White"))
        Error_Message_Window.geometry("350x100")

        Error_Message = Label(Error_Message_Window, text = Error_Text, bg = self.Find_Colour("White"), font = ("Helvetica", 12), wraplength = 210)
        Error_Message.place(x = 70, y = 15)
        Error_Message_Image = Label(Error_Message_Window, image = self.Error_Icon, bg = self.Find_Colour("White"))
        Error_Message_Image.place(x = 5, y = 10)

        OK_Button = Button(Error_Message_Window, text = "Ok", bg = self.Find_Colour("Grey"), font = ("Helvetica", 12), command = Error_Message_Window.destroy)
        OK_Button.place(x = 250, y = 60, width = 50, height = 30)

        Error_Message_Window.mainloop()

    #Used to create a success message popup
    def Success_Window(self, Success_Text):
        Success_Message_Window = Tk()
        Success_Message_Window.title(" ")
        Success_Message_Window.config(bg = self.Find_Colour("White"))
        Success_Message_Window.geometry("350x100")

        self.Information_Icon = PhotoImage(master = Success_Message_Window, file = "Information_Icon.gif")

        Success_Message = Label(Success_Message_Window, text = Success_Text, bg = self.Find_Colour("White"), font = ("Helvetica", 12), wraplength = 210)
        Success_Message.place(x = 70, y = 15)
        Success_Message_Image = Label(Success_Message_Window, image = self.Information_Icon, bg = self.Find_Colour("White"))
        Success_Message_Image.place(x = 5, y = 10)

        OK_Button = Button(Success_Message_Window, text = "Ok", bg = self.Find_Colour("Grey"), font = ("Helvetica", 12), command = Success_Message_Window.destroy)
        OK_Button.place(x = 250, y = 60, width = 50, height = 30)

        Success_Message_Window.mainloop()


#######ADD EXTRA FUNCTIONS HERE#######





#The following section creates a canvas on the Tkinter screen - this can be used for drawing tables in Tkinter

    #Enables the canvas to be scrolled through
    def Configure_Canvas(self, event):
        self.Drawing_Canvas.configure(scrollregion=self.Drawing_Canvas.bbox("all"),width= self.Screen_Width ,height=self.Screen_Height)

    #Enables the mousewheel to be used to scroll
    def On_MouseWheel(self, event):
        self.Drawing_Canvas.yview_scroll(-1*int((event.delta/120)), "units")

##    #Enables the down key to be used to scroll
##    def On_Down_Key(self, event):
##	     self.Drawing_Canvas.yview_Scroll(1,"units")
##
##    #Enables the up key to be used to scroll
##    def On_Up_Key(self, event):
##	     self.Drawing_Canvas.yview_Scroll(-1,"units")

    #Draws the canvas and adds the gridlines & text to the table
    def Draw_Canvas(self, window, Screen_Width, Screen_Height, Columns, Rows, Row_Spacing, Headings, Data):
        self.Screen_Width = Screen_Width
        Canvas_Height = (Row_Spacing * Rows) + 100    #+100 leeway so that the end of the grid does not look so rigid: Can be removed if you want
        self.Screen_Height = Screen_Height
        Canvas_Frame = Frame(window, bg = self.Find_Colour("Light Blue"))    #Creates a frame to place the canvas on
        Canvas_Frame.place(x = 0, y = 65, width = Screen_Width, height = Canvas_Height)    #Places the frame onto the screen

        self.Drawing_Canvas = Canvas(Canvas_Frame, width = Screen_Width, height = Screen_Height, bg = self.Find_Colour("Light Blue"))    #Adds the canvas to the screen in the frame above
        Scrolling_Frame = Frame(self.Drawing_Canvas, bg = self.Find_Colour("Light Blue"), width = 10, height = Canvas_Height - 65)    #Adds a frame to contain the scrollbar
        Scroll_Bar = Scrollbar(Canvas_Frame, orient = "vertical", command = self.Drawing_Canvas.yview)    #Adds the scrollbar to the screen
        self.Drawing_Canvas.configure(yscrollcommand = Scroll_Bar.set)    #Allows the scrollbar to scroll vertically

        self.Drawing_Canvas.place(x = 0, y = 0)    #Adds the canvas to the frame on the screen
        Scroll_Bar.pack(side = RIGHT, fill = "y")    #Adds the scrollbar to the screen
        self.Drawing_Canvas.create_window( (0,0), window = Scrolling_Frame, anchor = "nw")    #Makes the canvas window scrollable

	    #Binds keys and mousewheel to the scrollbar
        Scrolling_Frame.bind("<Configure>", self.Configure_Canvas)
        Scrolling_Frame.bind_all("<MouseWheel>", self.On_MouseWheel)

    	#Creates the top line of the grid that has the titles for the columns above it
        self.Drawing_Canvas.create_line(0,65,Screen_Width,65, fill = self.Find_Colour("Dark Grey"), width = 3)

    	#Adds the rest of the horizontal lines to the screen
        Column_Spacing = Screen_Width / Columns
        for Row in range(0,Rows+1):
            self.Drawing_Canvas.create_line(0,(Row*Row_Spacing) + 65, Screen_Width,(Row*Row_Spacing) + 65, fill = self.Find_Colour("Dark Grey"), width = 3)

	   #Adds the vertical lines to the screen
        Max_Height = (Rows*Row_Spacing) + 65
        for Column in range(0,Columns):
            self.Drawing_Canvas.create_line(Column_Spacing*Column,0, Column_Spacing*Column,Max_Height, fill = self.Find_Colour("Dark Grey"), width = 3)

	   #Adds the titles to the top of the grid - they should fit in the boxes created by the lines, but if not reduce the size of the font [font = ("Helvetica",16)]
        for Column in range(0,Columns):
            self.Drawing_Canvas.create_text((Column_Spacing*Column) + (Column_Spacing/2),10, text = Headings[Column], font = ("Helvetica",16), anchor = N, width = Column_Spacing-20)

	   #Identifies the text that needs to be placed in each column and row (each box created by the grid)
        for Column in range(0,Columns):
            for Row in range(0,Rows):
                Text = Data[Column][Row]
                length = len(Text)
                if length > 1:
                    count = 0
                    for element in Text:
                        count += 1
                        if count > 1:
                            To_Add = To_Add + "," + element
                        else:
                            To_Add = element
                else:
                    To_Add = Text[0]

		        #Adds the rest of the text to the table - if they do not fit in the boxes reduce the font size [font = ("Helvetica", 13)]
                self.Drawing_Canvas.create_text((Column_Spacing*Column)+10, (Row*Row_Spacing)+75, text = To_Add, font = ("Helvetica", 13), anchor = NW, width = Column_Spacing-20)

        return self.Drawing_Canvas
