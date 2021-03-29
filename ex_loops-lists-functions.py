import turtle
py = turtle.Pen()
colors = ["red", "blue", "yellow", "black"]

def circle(color, radius):
    py.color(color)
    py.circle(radius, 360)

for i in range(4):
    #circle(colors[i], (i + 1) * 10)
    circle(colors[i], 90)
    py.penup()
    py.fd(150)
    py.pendown()

turtle.done()
