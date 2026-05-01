import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Hexagonal Fractal · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)
pen.pencolor("#FFD700")

hex_colors = ["#0d47a1", "#1e88e5",  "#5e35b1", "#7e57c2"]

def draw_hexagon(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(radius)
        t.left(60)
    t.end_fill()

def hex_fractal(t, x, y, radius, depth):
    if depth == 0:
        return
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    
    color_idx = depth % len(hex_colors)
    draw_hexagon(t, radius, hex_colors[color_idx])
    
    new_radius = radius * 0.5
    for angle in [0, 60, 120, 180, 240, 300]:
        rad = math.radians(angle)
        nx = x + radius * math.cos(rad)
        ny = y + radius * math.sin(rad)
        hex_fractal(t, nx, ny, new_radius, depth - 1)

hex_fractal(pen, 0, 0, 150, 4)

screen.update()
screen.mainloop()