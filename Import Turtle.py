import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("yellow")
wn.title("Turtle")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.hideturtle()
tess.color("blue")
tess.pensize(5)


tess.forward(100)             # Make tess draw equilateral triangle
tess.dot(50, 'red')

tess.right(100)
tess.backward(100)
tess.left(100)

tess.dot(50,'red')
tess.left(500)
tess.forward(100)             # Make tess draw equilateral triangle
tess.dot(50, 'red')


tess.left(90)
tess.forward (100)
tess.dot(50, 'red')
tess.left(680)
tess.left (90)
tess.forward (95)
tess.dot(50, 'red')





wn.mainloop()
