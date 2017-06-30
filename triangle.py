import turtle

def draw_triangle(some_triangle,dist,angle,color):
	for i in range (1,4):
		some_triangle.forward(dist)
		some_triangle.left(angle)
	some_triangle.bgcolor = (color)

window = turtle.Screen()
window.bgcolor = ("white")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("green")
brad.speed(2)
draw_triangle(brad,200,120,"red")
brad.forward(100)
brad.left(60)
draw_triangle(brad,100,120,"green")
window.exitonclick()
