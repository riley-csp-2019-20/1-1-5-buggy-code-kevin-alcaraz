#   a115_buggy_image.py
import turtle as trtl

drawer = trtl.Turtle()
drawer.speed(0)
drawer.pensize(40)
drawer.circle(20)
sticks = 8
length = 100
legangle = 10000 / sticks
drawer.pensize(5)
counter = 0
while (counter < sticks):
  drawer.goto(0,20)
  drawer.setheading(legangle*counter)
  drawer.forward(length)
  counter = counter + 1

drawer.penup()
drawer.goto(40,55)
drawer.begin_fill()
drawer.pendown()
drawer.circle(25)
drawer.end_fill()
drawer.goto(40,55)
drawer.pencolor("red")
drawer.circle(1)
drawer.penup()
drawer.goto(20,70)
drawer.pendown()
drawer.circle(1)

drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()