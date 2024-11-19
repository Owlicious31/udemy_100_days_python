from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgpic("snake_background.png")
screen.title("SNAKE")
scoreboard = Scoreboard()
screen.tracer(0)


snake = Snake()
food = Food()

# Snake movements
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


# Game starts here
game_on = True

while game_on:
    scoreboard.display()

    # Updating the screen each time all segments move
    screen.update()

    # Delaying the rate at which snake segments can move
    time.sleep(0.1)

    snake.move()

    # Detecting collisions with food
    if snake.snake_head.distance(food) < 15:
        food.go_random_location()
        scoreboard.increment_score()
        snake.extend_snake()

    # Detecting collisions with wall
    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285:
        scoreboard.game_over()
        game_on = False

    elif snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
        scoreboard.game_over()
        game_on = False

    # Detecting collisions with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
