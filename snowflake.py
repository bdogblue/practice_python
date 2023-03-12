import turtle, time



def koch_fract(turtle, divis, size):
    if(divis == 0):
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)               
            turtle.left(angle)

divis = 4
size = 500

wn = turtle.Screen()
wn.setup(width=1500, height=900)
turtle.speed(20000)

turtle.hideturtle()

turtle.penup()

turtle.left(-120)

turtle.pendown()

turtle.color('black')
turtle.fillcolor('blue')
turtle.begin_fill()
for i in range(0, 3):
    koch_fract(turtle, divis, size)
    turtle.left(-120)
turtle.end_fill()

time.sleep(8)