import turtle
turtle.bgcolor("lightblue")
turtle.pensize(1.5)
turtle.speed(0.5)
color = ["purple","black""red","yellow"]
for b in range(9):
  for x in color:
    turtle.color(x)
    turtle.circle(100)
    turtle.left(10)
turtle.mainloop()