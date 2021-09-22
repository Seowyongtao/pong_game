from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.onkeypress(key="Up", fun=paddle_right.up)
screen.onkeypress(key="Down", fun=paddle_right.down)
screen.onkeypress(key="a", fun=paddle_left.up)
screen.onkeypress(key="s", fun=paddle_left.down)

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # Paddle right misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.update_l_score()

    # Paddle left misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.update_r_score()

screen.exitonclick()
