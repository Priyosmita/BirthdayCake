import turtle
t= turtle.Turtle()
t.shape('turtle')
t.screen.bgcolor("#A8DF8E")
t.speed(1)
t.pensize(4)
t.color("#FBD85D")
t.penup()
t.backward(200)
t.right(90)
t.forward(25)
t.pendown()
#first layer
t.fillcolor("#D988B9")
t.begin_fill()  
for i in range(1):   
    t.forward(75)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(400)
t.end_fill()  
t.penup()
t.right(180)
t.forward(50)
t.left(90)
t.forward(3)
t.pendown()
#second layer
t.fillcolor("#FF4B91")
t.begin_fill()  
for i in range(1):
    t.forward(70)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(300)
t.end_fill() 
t.penup()
t.right(180)
t.forward(50)
t.left(90)
t.forward(73)
t.pendown()
#third layer
t.fillcolor("#FF8080")
t.begin_fill()  
for i in range(1):
    t.forward(70)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(200)
t.end_fill() 
t.penup()
t.right(180)
t.forward(90)
t.left(90)
t.forward(73)
t.pendown()
#candle
t.color("#A78295")
t.fillcolor("#A78295")
t.begin_fill()  
for i in range(1):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(10)
t.end_fill() 
t.penup()
t.right(90)
t.forward(73)
t.pendown()
#fire
t.color("#FFA41B")
t.fillcolor("#FFA41B")
t.begin_fill()
t.left(30)  
for i in range(1):
    t.circle(-60,60)
    t.right(100)
    t.circle(-50,75)
    t.right(60)
    t.forward(7)
t.end_fill() 
t.penup()
#message
t.left(85)
t.forward(350)
t.right(90)
t.forward(220)
t.right(180)
t.pendown()
t.pensize(100)
t.hideturtle()
t.color("#DF2E38")
t.hideturtle()
t.write("Happy Birthday^3^",font=("Segoe Print", 16, "normal"))
turtle.done()