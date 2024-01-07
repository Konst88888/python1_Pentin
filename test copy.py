from turtle import *

turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "red")
turtle.begin_fill()
for i in range(6):
    turtle.left(360/6)
    turtle.forward(100)
    turtle.end_fill()
   















# Необходимо, чтобы окно не закрывалось само, а только по клику
turtle.screen.exitonclick()
turtle.screen.mainloop()


