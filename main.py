from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setting up screen object for game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# creating scoreboard object for score display
scoreboard = Scoreboard()

# creating food and snake objects for game from food.py and snake.py
food = Food()
snake = Snake()

# creates 3 squares for the body of the snake for game start
snake.create_snake()

# snake controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# main gameplay loop
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#detect food collision
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.record_score()

	#detect wall collision
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
		scoreboard.reset()
		snake.reset()
	#if head hits tail we lose
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 5:
			scoreboard.reset()
			snake.reset()


# click to exit at any time
screen.exitonclick()
