import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Lévy C Curve · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

# 颜色序列
line_colors = ["#ff1744", "#ff9100", "#ffea00", "#00e676", "#00b0ff", "#d500f9"]
color_idx = 0

def levy(t, length, depth):
    global color_idx
    if depth == 0:
        t.pencolor(line_colors[color_idx % len(line_colors)])
        color_idx += 1
        t.forward(length*25)
    else:
        t.left(45)
        levy(t, length * 0.707, depth - 1)
        t.right(90)
        levy(t, length * 0.707, depth - 1)
        t.left(45)

# 放大参数：初始长度 15，深度 12，起始位置调整使图形居中
pen.penup()
pen.goto(-220, -120)  # 起始点左下，使最终图形中心大致在 (0,0)
pen.setheading(0)
pen.pendown()

levy(pen, 15, 12)

screen.update()
screen.mainloop()