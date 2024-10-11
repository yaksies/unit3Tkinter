from tkinter import*
from random import randint, choice

screen = Canvas( Tk(), width=805, height=805, background="black" )
screen.pack()

colors = ["red", "blue", "green", "pink", "orange", "yellow", "white", "grey", "magenta", "maroon", "lawngreen", "hotpink", "skyblue", "purple", "black", "beige"]


x1 = int(input("Enter the x coordinate of the left corner: "))

x2 = int(input("Enter the x coordinate of the middle corner: "))

x3 = int(input("Enter the x coordinate of the right corner: "))

y1 = int(input("Enter the y coordinate of the left corner: "))

y2 = int(input("Enter the y coordinate of the middle corner: "))

y3 = int(input("Enter the y coordinate of the right corner: "))



screen.create_polygon( x1, y1, x2, y2, x3, y3, outline="white", width=4)


#RIGHT HALF       
for k in range(1000):
    x = randint(x2, x3)
    if y1 > y2:
        y1, y2 = y2, y1
    y = randint(y2, y3)

    m1 = (y3 - y2) / (x3 - x2)

    b = y3 - m1*x3
   
    yLine = m1*x + b

    if y > yLine:
        screen.create_line(x, y, x, yLine, width = 2, fill = choice(colors))



#LEFT HALF
for k in range(1000):
    x = randint(x1, x2)

    if y1 > y2:
        y1, y2 = y2, y1
        

    y = randint(y1, y2)

    m = (y2 - y1) / (x2 - x1)
    
    b = y2 - m * x2

    yLine = m * x - b


    
    if y > yLine:
        screen.create_line(x, y, x, yLine, width = 2, fill = choice(colors))

screen.mainloop()
