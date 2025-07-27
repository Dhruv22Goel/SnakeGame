from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#00FFFF")  # Neon cyan
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")

    def refresh(self, snake_segments=None):
        is_on_snake = True
        while is_on_snake:
            x = randint(-280, 280) // 20 * 20
            y = randint(-280, 280) // 20 * 20
            new_pos = (x, y)
            if snake_segments:
                is_on_snake = any(segment.distance(new_pos) < 20 for segment in snake_segments)
            else:
                is_on_snake = False
        self.goto(new_pos)
