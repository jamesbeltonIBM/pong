import turtle
#creats the screen of wich the program is run
wn= turtle.Screen()
#names the screen
wn.title("pong")
#changes the backround
wn.bgcolor("black")
#makes the window
wn.setup(width=800, height=600)
#stops the window from up dating
wn.tracer(0)

#creats the score
score_one = 0
score_two = 0

#paddle A
#it creats the pen called paddle_a
paddle_a= turtle.Turtle()
#the pwn speed is at the max
paddle_a.speed(0)
#makes the paddle a square
paddle_a.shape("square")
#makes it's colour white
paddle_a.color("white")
#makes it into a rectangle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#stops drawing
paddle_a.penup()
#moves the paddle to -350,0
paddle_a.goto(-350,0)

#paddle B
#repets the prosses but it is now called paddle b
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
#send the paddle to the other side of the screen
paddle_b.goto(350,0)

#ball
#does simmiler as the other two but makes it a squair
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
#moves it to the middle of the screen
ball.goto(0,0)
#the ball's movement
#this is the x-axi
ball.dx = 0.2
#this is y-axi
ball.dy = 0.2

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#sends the writing to the back
pen.hideturtle()
pen.goto(0,260)
#writes the score wich has been moved to the top of the screen
pen.write("player 1: 0   Player 2:  0", align="center",font=("Courier", 24, "normal"))

#function to move the paddle up
def paddle_a_up():
    #serches for the y cordinat of paddle_a
    y= paddle_a.ycor()
    #adds 20 to the y cordinat
    y+= 20
    #moves the paddle to it's new y cordinats
    paddle_a.sety(y)
def paddle_a_down():
    #serches for the y cordinat of paddle_a
    y= paddle_a.ycor()
    #subtrats 20 to the y cordinat
    y-= 20
    #moves the paddle to it's new y cordinats
    paddle_a.sety(y)
def paddle_b_up():
    #serches for the y cordinat of paddle_b
    y= paddle_b.ycor()
    #adds 20 to the y cordinat
    y+= 20
    #moves the paddle to it's new y cordinats
    paddle_b.sety(y)
def paddle_b_down():
    #serches for the y cordinat of paddle_b
    y= paddle_b.ycor()
    #subtrats 20 to the y cordinat
    y-= 20
    #moves the paddle to it's new y cordinats
    paddle_b.sety(y)
#keyboard binding/ serches for a serten button press on the keyboard
wn.listen()
#when it find the key press of 'w' it will call the function 'paddle_a_up'
wn.onkeypress(paddle_a_up, "w")
#when you press 's' it will call the function 'paddle_a_down'
wn.onkeypress(paddle_a_down, "s")
#when you press the up arrow it will call the function 'paddle_b_up'
wn.onkeypress(paddle_b_up, "Up")
#when you press the down arrow it will call the function '
wn.onkeypress(paddle_b_down, "Down")

#main loop
while True:
    #so the program can stay open and checks wether these conditions have been met
    wn.update()

    #moveing the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #cheks wether the ball is hitting the edge of the play aria
    if ball.ycor() > 290:
        ball.sety(290)
        #reverces the ball's y direction
        ball.dy *= -1
    

    if ball.ycor() < -290:
        ball.sety(-290)
        #reverces the ball's y direction
        ball.dy *= -1

    if ball.xcor() > 390:
        #resets the ball's possition
        ball.goto(0,0)
        #changes the balles x direction
        ball.dx *= -1
        #adds a score to player one
        score_one += 1
        #displays the new score
        pen.clear()
        pen.write("player 1: {}   Player 2:  {}".format(score_one, score_two), align="center",font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        #resets the ball's possition
        ball.goto(0,0)
        #changes the balles x direction
        ball.dx *= -1
        #adds one point two player two
        score_two += 1
        #displays the new score
        pen.clear()
        pen.write("player 1: {}   Player 2:  {}".format(score_one, score_two), align="center",font=("Courier", 24, "normal"))
        
    # paddle and ball collisions
    #checks to see wether the ball is hitting the baddle and if it is be hind it.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() -40):
        #this will make the x 340
        ball.setx(340)
        #it will push the ball in the opposit direction
        ball.dx *= -1
    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() -40):
        #this will make the x 340
        ball.setx(-340)
        #it will push the ball in the opposit direction
        ball.dx *= -1
    #this is the winning codition
    if score_one == 10:
        #hides the hud
        pen.clear()
        paddle_a.color("black")
        paddle_b.color("black")
        ball.color("black")
        #creats the winner sighn with the simmiler prosses as the score board
        winer = turtle.Turtle()
        winer.color("white")
        winer.penup()
        winer.goto(0,0)
        winer.write("PLAYER ONE WINS!", align="center",font=("Courier", 50, "normal"))
    #sane as the last if
    if score_two == 10:
        pen.clear()
        paddle_a.color("black")
        paddle_b.color("black")
        ball.color("black")
        winer = turtle.Turtle()
        winer.color("white")
        winer.penup()
        winer.goto(0,0)
        winer.write("PLAYER two WINS!", align="center",font=("Courier", 50, "normal"))