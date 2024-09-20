import turtle

turtle.speed(10)
turtle.fillcolor('dim gray')
turtle.penup()
turtle.left(90) 
turtle.goto(0,100) 
turtle.pendown() 
turtle.begin_fill()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.penup() 
turtle.goto(75,50) 
turtle.pendown() 
turtle.circle(20)
turtle.end_fill()
turtle.penup() 









print(turtle.pos())








