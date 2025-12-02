import turtle
import winsound
from winsound import SND_ASYNC

score_a=0
score_b=0
#display screen
win=turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor("pink")
win.title("Pong")
win.tracer(0)

#left_paddle
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380,0)
#right paddle
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.5
ball.dy=-0.5

#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("player A:  0  player B: 0" ,align= "center",font=("Ariel",24,"normal"))

def sound():
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)
def right_paddle_down():
     right_paddle.sety(right_paddle.ycor() - 20)
win.listen()
win.onkeypress(left_paddle_up,'m')
win.onkeypress(left_paddle_down,'k')
win.onkeypress(right_paddle_up,'d')
win.onkeypress(right_paddle_down,'s')
while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        score_a+=1
        pen.clear()
        pen.write("player A: {} player B: {}".format(score_a,score_b),align= "center",font=("Ariel",24,"normal"))
        ball.goto(0,0)
        ball.dx *= -1
        sound()
    if ball.xcor() < -390:
        ball.setx(-390)
        score_b+= 1
        pen.clear()
        pen.write("player A: {} player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        sound()
#collision with paddles
    if ball.xcor() > 370 and right_paddle.ycor() -50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.setx(360)
        ball.dx *= -1

    if ball.xcor() < -370 and left_paddle.ycor() -50 < ball.ycor()< left_paddle.ycor() +50:
        ball.setx(-360)
        ball.dx *= -1




