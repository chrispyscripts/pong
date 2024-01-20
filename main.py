from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
# screen.onkey(paddle1.up, "Up")
# screen.onkey(paddle1.down, "Down")
# screen.onkey(paddle2.up, "W")
# screen.onkey(paddle2.up, "S")
screen.exitonclick()

paddle1 = Paddle()