import turtle

x1, y1 = eval(input("Enter the coordinates for 1st point: "))
x2, y2 = eval(input("Enter the coordinates for 2nd point: "))
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
x, y = ((x1+x2)/2), ((y1+y2)/2)

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2,y2)
turtle.write("Point 2")

turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(distance)
turtle.done()


