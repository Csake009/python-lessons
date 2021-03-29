import turtle
py = turtle.Pen()
colors = ["red", "blue", "yellow", "black"]
for i in range(4):
    py.color(colors[i])
    py.circle(90, 360)
    py.penup()
    py.fd(100)
    py.pendown()
turtle.done
