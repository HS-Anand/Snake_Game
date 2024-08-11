from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Scoreboard


class Game:

    def __init__(self):
        self.p = 0
        self.scoreboard = Scoreboard()
        self.snake = Snake()
        self.food = Food()

        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()

    def end(self):
        self.scoreboard.game_over()
        self.food.hideturtle()
        for segment in self.snake.segments:
            segment.hideturtle()

        self.screen.update()

        self.screen.exitonclick()

    def pause(self):
        self.scoreboard.pause()
        self.screen.update()
        self.p = 1

    def play(self):
        self.p = 0
        self.scoreboard.update_scoreboard()
        self.screen.update()


    def game(self):
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.end, "e")
        self.screen.onkey(self.pause, "p")
        self.screen.onkey(self.play, "l")

        self.snake.create_snake()
        game = True

        while game:
            self.screen.update()
            time.sleep(0.08)
            if self.p == 0:
                self.snake.move()
            for segment in self.snake.segments:
                if segment == self.snake.head:
                    pass
                elif segment.distance(self.food) < 14:
                    self.food.refresh()
            if self.snake.head.distance(self.food) < 14:
                self.food.refresh()
                self.scoreboard.increase_score()
                self.snake.extend()

            if self.snake.head.xcor() > 285 or self.snake.head.xcor() < -290 or self.snake.head.ycor() > 290 or self.snake.head.ycor() < -285:
                self.scoreboard.reset()
                self.scoreboard.update_scoreboard()
                self.snake.reset()

            for segment in self.snake.segments:
                if segment == self.snake.head:
                    pass
                elif self.snake.head.distance(segment) < 8:
                    self.scoreboard.reset()
                    self.scoreboard.update_scoreboard()
                    self.snake.reset()

        self.screen.exitonclick()



