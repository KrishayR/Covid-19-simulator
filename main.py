import random
import turtle
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor('red')
wn.title('COVID-19 SIMULATOR')
wn.tracer(0)


balls = []


def greenbg():
    wn.bgcolor('#28e081')
def redbg():
    wn.bgcolor('red')
def blackbg():
    wn.bgcolor('black')
def whitebg():
    wn.bgcolor('white')
for i in range(30):
    balls.append(turtle.Turtle())

for ball in balls:
    ball_colors = ['#28e081','#275fd9','#de2f26','#c9c2c1','#f035e0','#ffe921','red','orange','yellow','green','white','blue','purple','pink']
    ball.shape('circle')
    ball.color('#28e081')
    ball.penup()
    ball.speed(0)
    x = random.randint(-290,290)
    y = random.randint(100,400)
    ball.goto(x ,y)
    ball.dy = 0
    ball.dx = random.randint(-3,3)
    ball.da = random.randint(0,6)

gravity = 0.01


while True:
    wn.onkey(greenbg, "Up")
    wn.onkey(redbg,'Down')
    wn.onkey(blackbg,'Right')
    wn.onkey(whitebg,'Left')
    wn.listen()
    wn.update()
    
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity

        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor()+ ball.dx)
        if ball.xcor() > 325:
            ball.dx *= -1
            
            ball.color('#28e081')
        if ball.xcor() < -325:
            ball.dx *= -1
            ball.color('#28e081')
        if ball.ycor() < -325:
            ball.sety(-325)
            ball.dy *= -1
            ball.color('#28e081')
    for i in range(0,len(balls)):
        for j in range(i+1,len(balls)):
            if balls[i].distance(balls[j]) < 20:
                balls[i].color('red')
                balls[j].color('red')
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy
                
                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy
                
                balls[j].dx = temp_dx
                balls[j].dy = temp_dy



wn.mainloop()
