'''
Simple Pong game written in Python
'''


import turtle


win = turtle.Screen()
win.title('Pong by Richard Craddock')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Paddle blue
paddle_blue = turtle.Turtle()
paddle_blue.speed(0)
paddle_blue.shape('square')
paddle_blue.color('blue')
paddle_blue.shapesize(stretch_wid=5,stretch_len=1)
paddle_blue.penup()
paddle_blue.goto(-350,0)


# Paddle red
paddle_red = turtle.Turtle()
paddle_red.speed(0)
paddle_red.shape('square')
paddle_red.color('red')
paddle_red.shapesize(stretch_wid=5,stretch_len=1)
paddle_red.penup()
paddle_red.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = .26
ball.dy = .26

#score 
score_blue = 0

score_red = 0


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('grey')
pen.penup()
pen.hideturtle()
pen.goto(0,0)
pen.write(f"RED: 0  BLUE: 0 ", align = 'center', font=('Courier', 47, 'bold'))

#new game
new = turtle.Turtle()
new.speed(0)
new.color('white')
new.penup()
new.hideturtle()
new.goto(10,-200)


#functions

def paddle_blue_up():
    y = paddle_blue.ycor()
    y += 20
    paddle_blue.sety(y)
    
def paddle_blue_down():
    y = paddle_blue.ycor()
    y -= 20
    paddle_blue.sety(y)
    
def paddle_red_up():
    y = paddle_red.ycor()
    y += 20
    paddle_red.sety(y)
    
def paddle_red_down():
    y = paddle_red.ycor()
    y -= 20
    paddle_red.sety(y)

def play_again():
    win.update()
    

def not_again():
    turtle.Terminator()

#keyboard binds
win.listen()
win.onkeypress(paddle_blue_up, "w")
win.onkeypress(paddle_blue_down, "s")
win.onkeypress(paddle_red_up, "Up")
win.onkeypress(paddle_red_down, "Down")
win.onkeypress(play_again, "y")
win.onkeypress(not_again, "n")

    
#Main game loop
while True: 
    win.update()
    
    #move the bball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
        
    
    #bborder checkiing
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_blue += 1
        pen.clear()
        pen.write(f"RED:{score_red}  BLUE:{score_blue}", align = 'center', font=('Courier', 47, 'bold'))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_red += 1
        pen.clear()
        pen.write(f"RED:{score_red}  BLUE:{score_blue}", align = 'center', font=('Courier', 47, 'bold'))
    
    #paddle and ball collision
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle_red.ycor()+45 and ball.ycor()> paddle_red.ycor()-45):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < paddle_blue.ycor()+45 and ball.ycor()> paddle_blue.ycor()-45):
        ball.setx(-340)
        ball.dx *= -1
    
    if score_blue >= 10:
        pen.clear()
        pen.write('BLUE PLAYER IS THE WINNER', align = 'center', font = ('Courier',34, 'bold'))
        ball.goto(0,0)
        # new.write('WOULD YOU LIKE TO PLAY AGAIN: y OR n: ',align = 'center',font=('courier',25,'bold'))
        # game_on = False
        
        
        
        
    if score_red >=10:
        pen.clear()
        pen.write('RED PLAYER IS THE WINNER', align = 'center', font = ('Courier',34, 'bold'))
        ball.goto(0,0)
        # game_on=False
        
