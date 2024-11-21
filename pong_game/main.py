from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
scoreboard = Scoreboard()


# Opening animation
draw_tool = Turtle()
draw_tool.hideturtle()
draw_tool.color("white")
draw_tool.penup()
draw_tool.goto(0,320)
draw_tool.setheading(270)
draw_tool.pendown()
for _ in range(40):
    draw_tool.forward(10)
    draw_tool.penup()
    draw_tool.forward(10)
    draw_tool.pendown()

screen.tracer(0)


# Game objects
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

# Using key presses to move paddles
screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# Game starts here
game_on = True
sleep_duration = 0.070
while game_on:
    scoreboard.display_scores()
    ball.start_moving()
    screen.update()

    time.sleep(sleep_duration)

    # Detecting collisions with upper and lower walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detecting collisions and misses on the right side
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        sleep_duration *= 0.9
    elif ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increment_left_score()
        sleep_duration = 0.070


    # Detecting collisions and misses on the left side
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_duration *= 0.9
    elif ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increment_right_score()
        sleep_duration = 0.070

    # Checking if left paddle is out of bounds
    if left_paddle.ycor() > 240 :
        left_paddle.goto(left_paddle.xcor(),left_paddle.ycor() - 10)
    elif left_paddle.ycor() < -240:
        left_paddle.goto(left_paddle.xcor(), left_paddle.ycor() + 10)

    # Checking if right paddle is out of bounds
    if right_paddle.ycor() > 240:
        right_paddle.goto(right_paddle.xcor(),right_paddle.ycor() - 10)
    elif right_paddle.ycor() <-240:
        right_paddle.goto(right_paddle.xcor(), right_paddle.ycor() + 10)


screen.exitonclick()