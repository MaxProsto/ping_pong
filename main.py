import turtle as t
import os
player1Score = 0
player2Score = 0

window = t.Screen()
window.bgcolor('yellow')
window.setup(width=800, height=600)
window.tracer(0)
leftraketka = t.Turtle()
leftraketka.speed(0)
leftraketka.shape('square')
leftraketka.color('black')
leftraketka.shapesize(stretch_wid=5, stretch_len=1)
leftraketka.penup()
leftraketka.goto(-350,0)
rightraketka = t.Turtle()
rightraketka.speed(0)
rightraketka.shape('square')
rightraketka.color('black')
rightraketka.shapesize(stretch_wid=5, stretch_len=1)
rightraketka.penup()
rightraketka.goto(350,0)
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(5,5)
ball_dx = 1.5
ball_dy = 1.5
pen = t.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                      Player B: 0 ", align="center", font=('Arial', 24, 'normal'))

def leftraketkaup():
    y = leftraketka.ycor()
    y = y + 90
    leftraketka.sety(y)
def leftraketkadown():
    y = leftraketka.ycor()
    y = y - 90
    leftraketka.sety(y)
def rightraketkaup():
    y = rightraketka.ycor()
    y = y + 90
    rightraketka.sety(y)
def rightraketkadown():
    y = rightraketka.ycor()
    y = y - 90
    rightraketka.sety(y)
    
window.listen()
window.onkeypress(leftraketkaup, 'w')
window.onkeypress(leftraketkadown, 's')
window.onkeypress(rightraketkaup, 'Up')
window.onkeypress(rightraketkadown, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy = ball_dy * -1

    if ball.xcor() > 390:  
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: 
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightraketka.ycor() + 40 and ball.ycor() > rightraketka.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay raketka.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftraketka.ycor() + 40 and ball.ycor() > leftraketka.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay raketka.wav&")