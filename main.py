import turtle

wn = turtle.Screen()
wn.title("ping-pong game by akshaj")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)


score_a = 0
score_b = 0


paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("green")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("green")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("red")
Ball.penup()
Ball.dx = 0.2
Ball.dy = -0.2


pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 | Player B: 0", align="center", font=("courier", 24, "normal"))


def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


wn.listen()
wn.onkeypress(paddle_A_up, "w")


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


wn.listen()
wn.onkeypress(paddle_A_down, "s")


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


wn.listen()
wn.onkeypress(paddle_B_up, "Up")


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


wn.listen()
wn.onkeypress(paddle_B_down, "Down")


while True:
    wn.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if (Ball.xcor() >340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_B.ycor() + 40 and Ball.ycor() > paddle_B.ycor() - 50):
        Ball.setx(340)
        Ball.dx *= -1
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_A.ycor() + 40 and Ball.ycor() > paddle_A.ycor() - 50):
        Ball.setx(-340)
        Ball.dx *= -1
    if score_a == 20:
        print("player A won!! congrats!!!! :)")
        exit()
    if score_b == 20:
        print("player B won!! congrats!!!! :)")
        exit()
