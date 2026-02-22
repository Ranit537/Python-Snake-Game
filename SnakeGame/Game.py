from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
count = 0

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        count+=1
        snake.extend()
    scoreboard.score(count)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            continue
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()

