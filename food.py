from turtle import Turtle
from random import randint


class Food(Turtle):
"""
   food object for snake game
   generates random coordinates for placement
   when snake collides we run self.refresh
"""

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("blue")
		self.speed("fastest")
		random_x = randint(-280, 280)
		random_y = randint(-280, 280)
		self.goto(random_x, random_y)

	def refresh(self):
		random_x = randint(-280, 280)
		random_y = randint(-280, 280)
		self.goto(random_x, random_y)




