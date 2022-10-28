from sys import set_coroutine_origin_tracking_depth
from tkinter import CENTER
import turtle


window_screen =turtle.Screen()
window_screen.title("simple pong (*_*) ")
window_screen.bgcolor("black")
window_screen.setup(height=600 , width=800)
window_screen.tracer(0)


#paddle A
pa=turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.shapesize(stretch_wid=6,stretch_len=1)
pa.color("blue")
pa.penup()
pa.goto(-350,0)

#paddle b
pb=turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.shapesize(stretch_wid=6,stretch_len=1)
pb.color("blue")
pb.penup()
pb.goto(350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=-2

score_a= 0
score_b= 0 
    
#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,120)
pen.write("player A : {} player B : {}".format(score_a,score_b), align="center", font=("courier",15,"normal"))
 



def paddlea_up():
    y=pa.ycor()
    y+=20
    pa.sety(y)

def paddlea_down():
    y=pb.ycor()
    y-=20
    pa.sety(y) 

def paddleb_up():
    y=pb.ycor()
    y+=20
    pb.sety(y)

def paddleb_down():
    y=pb.ycor()
    y-=20
    pb.sety(y)

window_screen.listen()
window_screen.onkeypress(paddlea_up,"w")
window_screen.onkeypress(paddlea_down,"s")
window_screen.onkeypress(paddleb_up,"Up")
window_screen.onkeypress(paddleb_down,"Down")





#main loop
while True:
    window_screen.update()

    #ball movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy*=-1
        score_a+=1
        pen.clear()
        pen.write("player A : {} player B : {}".format(score_a,score_b) , align="center", font=("courier",15,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dy*=-1
        score_b+=1
        pen.clear()
        pen.write("player A : {} player B : {}".format(score_a,score_b), align="center", font=("courier",15,"normal"))

    # collision of ball and paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < pb.ycor()+45 and ball.ycor() > pb.ycor()-45:
        ball.setx(340)
        ball.dx*=-1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < pa.ycor()+45 and ball.ycor()> pa.ycor()-45:
        ball.setx(-340)
        ball.dx*=-1

    
    
     


    


    






 
