import turtle

def draw_square(some_turtel):
	for i in range(1,5):
		some_turtel.forward(100)
		some_turtel.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	#Create the turtle Brad - Draw a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(20)
	count = 0
	while (count < 36):
		draw_square(brad)
		brad.right(10)
		count += 1
	window.exitonclick()

draw_art()