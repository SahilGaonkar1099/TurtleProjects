import turtle as t
pen=t.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def Message():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('white')
    pen.write("Happy Coding!!!",font=("Arial",15,"bold"))
heart()
Message()
t.exitonclick()
