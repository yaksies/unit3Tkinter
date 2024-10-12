from tkinter import*
from random import randint, choice
from time import sleep

screen = Canvas(Tk(), width=805, height=805, background="black" )
screen.pack()

colors = ["red", "blue", "green", "pink", "orange", "yellow", "white", "grey", "magenta", "maroon", "lawngreen", "hotpink", "skyblue", "purple", "black", "beige"]
'''
def randomrgb():
    return rgb_to_hex((randint(0, 255), randint(0, 255), randint(0, 255)))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)
'''

x1 = int(input("Enter the x coordinate of the left corner: "))

x2 = int(input("Enter the x coordinate of the middle corner: "))
while x2 < x1:
    x2 = int(input("Enter the x coordinate of the middle corner: "))

x3 = int(input("Enter the x coordinate of the right corner: "))
while x3 < x2:
    x3 = int(input("Enter the x coordinate of the right corner: "))

y1 = int(input("Enter the y coordinate of the left corner: "))

y2 = int(input("Enter the y coordinate of the middle corner: "))

y3 = int(input("Enter the y coordinate of the right corner: "))

#x1, x2, x3, y1, y2, y3 = 200, 400, 600, 500, 200, 500 # testing purposes only

screen.create_polygon( x1, y1, x2, y2, x3, y3, outline="white", width=4)

#RIGHT HALF       
for _ in range(1000): # number of lines on one side of triangle
    #sleep(0.01)
    x = randint(x2, x3)
    y = randint(y2, y3)

    m1 = (y3 - y2) / (x3 - x2)

    b = y3 - m1*x3
    #print(m1)
   
    yLine = m1*x + b

    if y > yLine:
        screen.create_line(x, y, x, yLine, width = 2, fill = choice(colors))
    
    #screen.update()


#LEFT HALF
for _ in range(1000): # number of lines on one side of triangle
    #sleep(0.01)
    x = randint(x1, x2)
    y = randint(min(y1, y2), max(y1, y2))

    m1 = (y1 - y2) / (x1 - x2)

    b = y1 - m1*x1
    #print(m1)
   
    yLine = m1*x + b

    if y > yLine:
        screen.create_line(x, y, x, yLine, width = 2, fill = choice(colors))


screen.mainloop()
