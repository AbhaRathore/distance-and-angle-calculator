import math
import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter coordinates of 3 vertices of a triangle: "))

#Calculating the edges of the triangle a,b,c
a = math.sqrt((x2-x3)**2 + (y2-y3)**2)
b = math.sqrt((x1-x3)**2 + (y1-y3)**2)
c = math.sqrt((x1-x2)**2 + (y1-y2)**2)

#Computing the respective angles
A = math.acos((a**2 - b**2 - c**2)/(-2 * b * c))
B = math.acos((b**2 - c**2 - a**2)/(-2 * a * c))
C = math.acos((c**2 - a**2 - b**2)/(-2 * a * b))

print("The three angles of the triangle ABC are:", round(A*100)/100.0, round(B*100)/100.0, round(C*100)/100.0)

turtle.showturtle()
turtle.pensize(3)
turtle.speed(2)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(x1, y1)
turtle.goto(x2, y2)
turtle.write(x2, y2)
turtle.goto(x3, y3)
turtle.write(x3, y3)
turtle.goto(x1, y1)
turtle.done()

