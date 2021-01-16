import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("pink")
wn.tracer(3)

pencere=turtle.Turtle()
pencere.penup()
pencere.setposition(-300,-300)
pencere.pendown()
pencere.pensize(3)
for side in range(4):
    pencere.fd(600)
    pencere.left(90)
pencere.hideturtle()

score=0
score_pen=turtle.Turtle()
score_pen.speed()
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-230,275)
scorestring="Score: %s" %score
score_pen.hideturtle()

can=3
can_pen=turtle.Turtle()
can_pen.speed()
can_pen.color("white")
can_pen.penup()
can_pen.setposition(255,275)
canstring="Can: %s" %can
can_pen.hideturtle()

kullanıcı=turtle.Turtle()
kullanıcı.color("red")
kullanıcı.shape("triangle")
kullanıcı.penup()
kullanıcı.speed(0)

maxGoals=10
goals=[]

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("green")
    goals[count].shape("circle")
    goals[count].pu()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
   
            
         
            

                
maxGoals2=7
goals2=[]

for count in range(maxGoals2):
    goals2.append(turtle.Turtle())
    goals2[count].color("red")
    goals2[count].shape("circle")
    goals2[count].pu()
    goals2[count].speed(0)
    goals2[count].setposition(random.randint(-300,300),random.randint(-300,300))
    

speed=(1)

def turnleft():
    kullanıcı.left(30)

def turnright():
    kullanıcı.right(30)

def increasespeed():
    global speed
    speed +=1

def isCollision(t1,t2):
     d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
     if d<20:
         return True
     else:
         return False
     
        
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")

while True:
    kullanıcı.forward(speed)
    
    if kullanıcı.xcor()>300 or kullanıcı.xcor()<-300:
        kullanıcı.right(100)
    if kullanıcı.ycor()>300 or kullanıcı.ycor()<-300:    
        kullanıcı.right(100)
        

    for count in range(maxGoals):
        goals[count].fd(3)

        if goals[count].xcor()>300 or goals[count].xcor()<-300:
            goals[count].right(100)

        if goals[count].ycor()>300 or goals[count].ycor()<-300:
            goals[count].right(100)

            
        if isCollision(kullanıcı,goals[count]):
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            score+=10
            score_pen.undo()
            scorestring="Score: %s" %score
            score_pen.write(scorestring ,False, align= "right",font=("Franklin Gothic Medium",16)) 

           
    for count in range(maxGoals2):
        goals2[count].fd(3)

        if goals2[count].xcor()>300 or goals2[count].xcor()<-300:
            goals2[count].right(100)

        if goals2[count].ycor()>300 or goals2[count].ycor()<-300:
            goals2[count].right(100)

            
        if isCollision(kullanıcı,goals2[count]):
            goals2[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals2[count].right(random.randint(0,360))
            score-=20
            score_pen.undo()
            scorestring="Score: %s" %score

            score_pen.color('deep pink')
            style = ('Franklin Gothic Medium', 30, 'italic')
            score_pen.write(str(scorestring), font=style, align='center')

            can-=1
            can_pen.undo()
            canstring="Can: %s" %can

            can_pen.color("white")
            style = ('Franklin Gothic Medium', 30, 'italic')
            can_pen.write(str(canstring), font=style, align='left')
            if(can==0):
                turtle.bye()
            



            
            
