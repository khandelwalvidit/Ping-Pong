import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

right_pd = Paddle((350, 0))
left_pd = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(left_pd.up, "w")
screen.onkeypress(left_pd.down, "s")
screen.onkeypress(right_pd.up, "Up")
screen.onkeypress(right_pd.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    scoreboard.score()

    # collusion with wall

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # collision with paddle

    if ball.distance(right_pd) < 60 and ball.xcor() > 320 or ball.distance(left_pd) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_score_increase()
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_score_increase()
        ball.bounce_x()

screen.exitonclick()
