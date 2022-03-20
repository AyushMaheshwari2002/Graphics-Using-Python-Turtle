    # Designing NETFLIX LOGO


from turtle import *
import turtle

bgcolor('black')
right(90)                        # change the direction of turtle by 90 degrees to the right.
pos = [(-40,0), (40,0)]

for x,y in pos :
    up()
    goto(x,y)
    down()
    fillcolor('red')
    begin_fill()
    for i in range(2) :
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()
up()
goto(-40,0)
down()
left(22)
begin_fill()

for i in range(2) :
    forward(217)
    left(68)
    forward(40)
    left(112)

end_fill()
turtle.exitonclick()  # or mainloop() or done()



