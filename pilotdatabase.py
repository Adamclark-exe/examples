import json
import firebase
from tkinter import *
from firebase import firebase as fb
from random import randint
class Pilot:
    name = ""
    Plane = ""
    Fictional = False
    def loadFromdict (self, d):
        self.name = d["name"]
        self.plane = d["plane"]
        self.fictional = d["fictional"]

    def getDict (self) :
        d = {"name": self.name,
               "plane": self.plane,
               "fictional": self.fictional}
        return d
class FirebaseManager:
    app = fb.FirebaseApplication("https://database-42119.firebaseio.com/",None)

    def WriteNewObject(self, id, value):
        result = self.app.put("", id, value)

def addNew():
    x=0
    p = Pilot()
    p.name = nameBox.get()
    p.plane =AircraftBox.get()
    p.fictional = optionString.get()
    nameBox.delete (0, "end")
    AircraftBox.delete (0,"end")
    d= p.getDict()
    fm = FirebaseManager()
    ID = randint (10000,99999)
    fm.WriteNewObject(ID,d)

root = Tk ()
root.title ("Pilot Database")
title = Label(root, text = "Pilot Database", font = "arial 25 bold", pady = 15)
title.grid(row = 0, column = 0, columnspan=3)


NameLabel  = Label(root, text = "Pilot Name(first ""callsign"") last:", font = "arial 14")
nameBox = Entry(root, font = "arial 14")
AircraftLabel  = Label(root, text = "Aircraft:", font = "arial 14")
AircraftBox = Entry(root, font = "arial 14")
RealLabel  = Label(root, text = "Fictional or Real", font = "arial 14")
RealBox = Entry(root, font = "arial 14")
saveB = Button(root, text = "Save Entry", font = "arial 14", width = "21", command=addNew)

NameLabel.grid(row = 2, column = 0)
nameBox.grid( row = 2, column = 1)
AircraftLabel.grid(row = 3, column = 0)
AircraftBox.grid( row = 3, column = 1)
RealLabel.grid(row = 4,column = 0)
saveB.grid(row = 5, column = 0, columnspan = 2)

optionString = StringVar (root)
optionString.set("Real")
dropdown = OptionMenu (root, optionString, "Real", "Fake")
dropdown.config(font="Arial", width = "10")
dropdown.nametowidget(dropdown.menuname) . config (font= "Arial 12")
dropdown.grid (row=4, column=1, sticky = "w")
root.mainloop

