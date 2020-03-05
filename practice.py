import turtle                   #allows us to use turtles
window = turtle.Screen()        #creates a playground for turtles
alex = turtle.Turtle()          #gives the turtle a name
alex.color("red")
window.bgcolor("peach puff")
window.title("Hello, Tess & Alex!")

alex.width(3)
alex.forward(50)  #tells alex to forward 50 units
alex.left(90)     #tells alex to turn left with 90 degrees
alex.forward(30)  #complete the second side of a rectangle

tess = turtle.Turtle()      #create tess

tess.color("green")
tess.width(5)
tess.forward(80)
tess.left(120)
tess.forward(80)

window.mainloop()


