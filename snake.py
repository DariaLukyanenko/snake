from turtle import Turtle
class Snake:
    def __init__(self):
        self.squares_list = []
        self.create_snake()

    def move(self):
        
        for num in range(len(self.squares_list)-1,0,-1):
            x_cor = self.squares_list[num-1].xcor()
            y_cor = self.squares_list[num-1].ycor()
            self.squares_list[num].speed(0)
            self.squares_list[num].goto(x_cor, y_cor)
        self.squares_list[0].fd(20)

    def create_snake(self):
        for i in range(3):
            snake=Turtle()
            snake.color('black')
            snake.shape("square")
            snake.penup()
            snake.goto(i*(-20),0)
            self.squares_list.append(snake)
            
    def up(self):
        if self.squares_list[0].heading() != 270:
            self.squares_list[0].seth(90)

    def left(self):
        if self.squares_list[0].heading() != 0:
            self.squares_list[0].seth(180)

    def right(self):
        if self.squares_list[0].heading() != 180:
            self.squares_list[0].seth(0)

    def down(self):
        if self.squares_list[0].heading() != 90:
            self.squares_list[0].seth(270)

    
    def add_segment(self):
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.goto(self.squares_list[-1].xcor(),self.squares_list[-1].ycor())
        new_segment.shape('square')
        new_segment.color("black")
        self.squares_list.append(new_segment)
