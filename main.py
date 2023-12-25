from turtle import Screen
from time import sleep
from food import Food
from score import Score
from snake import Snake

WIDTH, HEIGHT = 500, 500

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor('green')

snake = Snake()
food = Food()
score=Score()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')
screen.onkey(snake.down,'s')

def game():
    game_going = True
    food.apper_food()
    while game_going:
        screen.update()
        sleep(0.1)
        snake.move()
        
        if abs(snake.squares_list[0].xcor()-food.xcor())<15 and abs(snake.squares_list[0].ycor()-food.ycor())<15:
            food.apper_food()
            snake.add_segment()
            score.increase_score()
            

        if abs(snake.squares_list[0].xcor())>WIDTH / 2 or abs(snake.squares_list[0].ycor())>HEIGHT / 2:
            game_going=False
            score.game_over()

        for segment in snake.squares_list[1:]:
            if snake.squares_list[0].distance(segment) < 10:
                game_going = False
                score.game_over()

            


game()
screen.exitonclick()