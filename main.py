from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()



paddle1 = Paddle(1)
paddle2 = Paddle(-1)
ball = Ball()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_on = True
ball_speed = 0.1

while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= -1
    if ball.xcor() == 340 or ball.xcor() == -340:
        if ball.distance(paddle1) < 60 or ball.distance(paddle2) < 60:
            if ball.distance(paddle1) > 40 or ball.distance(paddle2) > 40:
                ball_speed -= 0.01
            ball.x_move *= -1
            if ball.heading() > 180:
                if ball.ycor() < paddle1.ycor() or ball.ycor() < paddle2.ycor():
                    ball.y_move *= -1
            elif ball.heading() < 180:
                if ball.ycor() > paddle1.ycor() or ball.ycor() > paddle2.ycor():
                    ball.y_move *= -1


        # pass


screen.exitonclick()

