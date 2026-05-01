import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Apollonian Circles · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)
pen.pencolor("#FFD700")

# 填充颜色
circle_colors = ["#0d47a1", "#1565c0", "#1e88e5", "#7e57c2", "#ab47bc"]

def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def apollonian(t, x, y, radius, depth):
    if depth == 0:
        return
    color = circle_colors[depth % len(circle_colors)]
    draw_circle(t, x, y, radius, color)
    
    new_radius = radius * 0.5
    # 上方
    apollonian(t, x, y + radius * 0.5, new_radius, depth - 1)
    # 左下
    apollonian(t, x - radius * 0.5, y - radius * 0.3, new_radius, depth - 1)
    # 右下
    apollonian(t, x + radius * 0.5, y - radius * 0.3, new_radius, depth - 1)

# 中心点设为 (0, 0)，初始半径 200，可完全居中
apollonian(pen, 0, 0, 200, 4)

screen.update()
screen.mainloop()