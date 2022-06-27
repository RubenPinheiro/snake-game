import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
"""to get the snake body to appear instantly pt.1"""
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    """appear instantly pt.2"""
    screen.update()
    """take 0.1s to move to the next code command"""
    time.sleep(0.05)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.snake[1:-1]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()



screen.exitonclick()
