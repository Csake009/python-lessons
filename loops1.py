import turtle
johny = turtle.Pen()
johny.width(10)
johny.color("red")
for i in range(2):
    johny.circle(50, 180)
    johny.right(90)
johny.left(90)
johny.fd(150)
johny.right(-115)
johny.fd(150)
johny.penup()
johny.right(180)
johny.fd(300)
johny.write("Mom I love u!", font=["Arial", 50])
turtle.done()
