import turtle
import time

delay = 0,1

# set up the screen
wn = turtle
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "up"


# function
def move():
	if head.direction == "up":
		y = head.ycor()
		head.set(y + 20)


# Main game loop
while True:
	wn.update()

	move()
	
	time.sleep(delay)


wn.mainloop()
