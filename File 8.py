
#Question 8

acc = 0 
import turtle
import random
turtle.showturtle()
turtle.home()


turtle.penup()

turtle.goto(-60,-50)


turtle.pendown()

turtle.goto(60,-50)
turtle.goto(60,50)
turtle.goto(-60,50)
turtle.goto(-60,-50)



turtle.hideturtle()



turtle.penup()

i=0
while i <10:

    
    x1 =  random.randint(-60,60)
    y1 = random.randint(-50,50)
    turtle.goto(x1,y1)
    turtle.dot(5)
    i+=1





    










