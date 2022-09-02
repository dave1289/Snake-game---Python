from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		with open("high_scores.txt", "r+") as high_score:
			contents = high_score.read()
			self.high_score = int(contents)
		self.score = 0
		self.color("white")
		self.goto(0, 250)
		self.update_scoreboard()


	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


	def record_score(self):
		self.score += 1
		self.update_scoreboard()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
		self.score = 0
		self.update_scoreboard()
		self.high_score_record()

	def high_score_record(self):
		with open("high_scores.txt", "w") as high_score:
			high_score.write(f"{self.high_score}")




