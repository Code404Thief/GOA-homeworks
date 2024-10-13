from turtle import *
#square
speed(100)
shape("turtle")
width(9)
color("gray")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
forward(70)
color("gray")
begin_fill()
left(90) 
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()
color("gray")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
color("cyan")
begin_fill()
penup()
goto(190, 190)
pendown()
left(30)
right(90)
forward(70)
left(90)
forward(50)
left(90)
forward(70)
left(90)
forward(50)
end_fill()



#window
color("cyan")
begin_fill()
penup()
goto(10, 190)
pendown()
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
end_fill()

#left rooms
color("gray")

penup()
goto(0, 200)
pendown()
left(180)
forward(200)
right(90)
begin_fill()

forward(200)
left(90)
forward(200)
left(90)
forward(600)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
# right tower
begin_fill()
right(180)
forward(30)
left(90)
forward(50)
right(45)
forward(100)
right(90)
forward(100)
right(45)
forward(50)
end_fill()
#left tower
penup()
goto(0, 200)
pendown()

forward(200)
right(90)
forward(30)
right(90)
begin_fill()
forward(30)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(30)
end_fill()

#door
left(90)
forward(150)
color("brown")
begin_fill()
right(90)
forward(200)
left(90)
forward(250)
left(90)
forward(200)
left(90)
forward(250)
end_fill()
left(180)
forward(125)
color("gray")
right(90)
forward(200)
exitonclick()
