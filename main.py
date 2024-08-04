from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Scoreboard


scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

snake.create_snake()

game = True
while game:
    screen.update()
    time.sleep(0.08)
    snake.move()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif segment.distance(food) < 14:
            food.refresh()
    if snake.head.distance(food) < 14:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -285:
        game = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 8:
            game = False
            scoreboard.game_over()



screen.exitonclick()
