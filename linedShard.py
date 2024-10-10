from tkinter import *
from random import randint, choice
#Import tkinter in order to use the graphics and random in order to make use of randint and choice


screen = Canvas(Tk(), height = 600, width = 800, background = "black")
screen.pack()
#Create a list of colors that we can use on our lines
colors = ["red", "blue", "green", "pink", "orange", "yellow", "white", "grey", "magenta", "maroon", "lawngreen", "hotpink", "skyblue", "purple", "black", "beige"]

#Take input for the three corners

x1, y1 = input("Enter the x and y coordinates of the left corner (in format x y seperated by space): ").split()

x2, y2 = input("Enter the x and y coordinates of the top corner (in format x y seperated by space): ").split()

x3, y3 = input("Enter the x and y coordinates of the right corner (in format x y seperated by space): ").split()

#Converting all values to integers

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)

#Creating the triangle
screen.create_polygon(x1, y1, x2, y2, x3, y3, outline = "white", width = "2")

#Calculate the three slopes
m1 = (y2 - y1) / (x2 - x1)
m2 = (y3 - y2) / (x3 - x2)
m3 = (y1 - y3) / (x1 - x3)


for i in range(1000):
    x = randint(x1, x2)
    if y1 > y2:
        y1, y2 = y2, y1
    y = randint(y1, y2)

    b = y - m1*x

    AB = m1 * x + b

    if y > AB:
        screen.create_line(x, y, x1, y1, fill = choice(colors))



screen.mainloop()
