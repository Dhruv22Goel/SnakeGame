from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def start_game():
    global game_is_on
    game_is_on = True
    food.refresh(snake.segments)
    loop()

def restart_game():
    global game_is_on
    scoreboard.clear()
    scoreboard.__init__()
    snake.reset()
    food.refresh(snake.segments)
    game_is_on = True
    loop()

def loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh(snake.segments)
            scoreboard.increase_score()
            snake.extend()

        # Detect wall collision
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            scoreboard.game_over()
            game_is_on = False

        # Detect self-collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(start_game, "space")
screen.onkey(restart_game, "r")

scoreboard.goto(0, 0)
scoreboard.write("Press SPACE to Start", align="center", font=("Courier", 24, "bold"))

screen.mainloop()
