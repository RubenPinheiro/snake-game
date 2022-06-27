from turtle import Turtle


ALIGN = "center"
FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def refresh(self):
        self.clear()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)


