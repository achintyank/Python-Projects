# importing libraries
import turtle as trtl
import random as rand
import time


wn = trtl.Screen()


# left paddle
left_paddle = trtl.Turtle()
left_paddle.penup()
left_paddle.left(90)
left_paddle.goto(-170,0) # middle of the left side of the screen
left_paddle.shape("square")
left_paddle.shapesize(stretch_len=3.5)
left_paddle_score=0

# right paddle
right_paddle = trtl.Turtle()
right_paddle.penup()
right_paddle.left(90)
right_paddle.goto(170,0) # middle of the right side of the screen
right_paddle.shape("square")
right_paddle.shapesize(stretch_len=3.5)
right_paddle_score = 0

# ball
ball = trtl.Turtle()
ball.penup()
initial_y = rand.randint(-180,180)
ball.goto(0,initial_y)
ball.left(90)
ball.shape("circle")
speed_x = 3
speed_y = 3

# score display turtles
text_1 = trtl.Turtle()  # for the left paddle
text_1.penup()
text_1.hideturtle()
text_1.goto(-110,150)

text_2=trtl.Turtle() # for the right paddle
text_2.penup()
text_2.hideturtle()
text_2.goto(110,150)

# functions

def left_up():
  y = left_paddle.ycor()
  y +=15
  left_paddle.sety(y)
def left_down():
  y = left_paddle.ycor()
  y -=15
  left_paddle.sety(y)

def right_up():
  y = right_paddle.ycor()
  y +=15
  right_paddle.sety(y)
def right_down():
  y = right_paddle.ycor()
  y-=15
  right_paddle.sety(y)

# key binding
wn.listen()
wn.onkeypress(left_up,"w")
wn.onkeypress(left_down,"s")
wn.onkeypress(right_up,"Up")
wn.onkeypress(right_down,"Down")

# main game loop
while True:
  wn.update()
 
 
  # make the ball constantly move
  ball.setx(ball.xcor()+speed_x)
  ball.sety(ball.ycor()+speed_y)
 
  # make the ball bounce off of the top and bottom of the window
  if ball.ycor() > 200:
    ball.sety(170)
    speed_y = speed_y*-1
     
  if ball.ycor() < -200:
    ball.sety(-170)
    speed_y=speed_y*-1
 
 
 
  # if the ball has the same x coordinate as the paddle and it's y coordinate is within the top of the
  # paddle and the bottom of it, it is considered a collision and will change the speed_x variable
  # to it's negative value
 
    # ball  collision with right paddle
  if ball.xcor() > 170 and ball.ycor() > right_paddle.ycor()-30 and ball.ycor() < right_paddle.ycor()+30:
    ball.setx(170)
    speed_x = speed_x*-1
  elif ball.xcor() > 175:
    # make the ball stop moving
    speed_x = 0
    speed_y = 0
    # give a point to the winner and update the score
    text_1.clear()
    left_paddle_score +=1
    text_1.write(left_paddle_score,font=("Arial",50,"normal"))
    # wait 5 seconds
    time.sleep(5)
    # give initial_y a new random value
    initial_y = rand.randint(-180,180)
    # make the ball return to it's starting point
    ball.goto(0,initial_y)
    # make the ball move again
    speed_x = 3
    speed_y = 3
   
  # ball collision with left paddle
  if ball.xcor() < -170 and ball.ycor() > left_paddle.ycor()-30 and ball.ycor() < left_paddle.ycor()+30:
    ball.setx(-170)
    speed_x = speed_x*-1
  elif ball.xcor() < -175:
    # make the ball stop moving
    speed_x = 0
    speed_y = 0
    # give a point to the winner and update the score
    text_2.clear()
    right_paddle_score +=1
    text_2.write(right_paddle_score,font=("Arial",50,"normal"))
    # wait 5 seconds
    time.sleep(5)
    # give initial_y a new random value
    initial_y = rand.randint(-180,180)
    # make the ball return to it's starting point
    ball.goto(0,initial_y)
    # make the ball move again
    speed_x = 3
    speed_y = 3
