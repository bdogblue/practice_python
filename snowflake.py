import turtle



def koch_fract(turtle, divis, size):
    if(divis == 0):
        turtle.forward(7)
        print(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)               
            turtle.left(angle)

divis = 4
size = 1000

wn = turtle.Screen()
wn.setup(width=1500, height=900)
turtle.speed(5000)

turtle.penup()

turtle.left(180)
turtle.forward(500)
turtle.left(90)
#turtle.forward(400)
turtle.left(90)

turtle.pendown()

for i in range(0, 3):
    koch_fract(turtle, divis, size)
    turtle.left(-120)

