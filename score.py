from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score()
        

    def game_over(self):
        self.goto(0, 0)
        self.write("you are losseeer", False, align='center', font=('Arial', 30, 'bold'))

    def update_score(self):
        self.speed(0)
        self.clear()
        self.goto(0, 220)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 16, 'normal')) 
            

    def increase_score(self):
        self.score += 1
        self.update_score()

    