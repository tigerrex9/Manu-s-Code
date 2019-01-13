from tkinter import *
from random import *
import winsound

x = 1000
y = str(x)

master = Tk ()

def Check ():
    print("Timer = " + y + "ms")

def LowC ():
    print("Low C")
    winsound.Beep(262 , x)

def D ():
    print("D")
    winsound.Beep(294 , x)

def E ():
    print("E")
    winsound.Beep(330 , x)

def F ():
    print("F")
    winsound.Beep(349 , x)

def G ():
    print("G")
    winsound.Beep(392 , x)

def A ():
    print("A")
    winsound.Beep(440 , x)

def B ():
    print("B")
    winsound.Beep(494 , x)

def HighC ():
    print("C")
    winsound.Beep(523 , x)

b = Button(master, text = "Check", command = Check)
b.pack ()

b = Button(master, text = "Low C", command = LowC)
b.pack ()

b = Button(master, text = "D", command = D)
b.pack ()

b = Button(master, text = "E", command = E)
b.pack ()

b = Button(master, text = "F", command = F)
b.pack ()

b = Button(master, text = "G", command = G)
b.pack ()

b = Button(master, text = "A", command = A)
b.pack ()

b = Button(master, text = "B", command = B)
b.pack ()

b = Button(master, text = "High C", command = HighC)
b.pack ()

mainloop()
