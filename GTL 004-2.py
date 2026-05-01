"""
谢尔宾斯基三角形 · 彩色玻璃花窗
背景黑色，金色描边，内部填充红/橙/金色系
"""
import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Sierpinski Triangle · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)
pen.pencolor("#FFD700")

# 填充颜色列表
fill_colors = ["#b71c1c",  "#f44336",  "#ff9800", "#ffc107"]

def sierpinski(t, ax, ay, bx, by, cx, cy, depth, color_idx):
    if depth == 0:
        t.penup()
        t.goto(ax, ay)
        t.pendown()
        t.fillcolor(fill_colors[color_idx % len(fill_colors)])
        t.begin_fill()
        t.goto(bx, by)
        t.goto(cx, cy)
        t.goto(ax, ay)
        t.end_fill()
    else:
        abx, aby = (ax + bx) / 2, (ay + by) / 2
        bcx, bcy = (bx + cx) / 2, (by + cy) / 2
        cax, cay = (cx + ax) / 2, (cy + ay) / 2
        sierpinski(t, ax, ay, abx, aby, cax, cay, depth - 1, color_idx + 1)
        sierpinski(t, abx, aby, bx, by, bcx, bcy, depth - 1, color_idx + 2)
        sierpinski(t, cax, cay, bcx, bcy, cx, cy, depth - 1, color_idx + 3)

# 定义大三角形顶点
size = 400
h = size * math.sqrt(3) / 2
ax, ay = -size/2, -h/2
bx, by = size/2, -h/2
cx, cy = 0, h/2

sierpinski(pen, ax, ay, bx, by, cx, cy, 4, 0)

# 外框装饰
pen.penup()
pen.goto(ax, ay)
pen.pendown()
pen.pencolor("#FFD700")
pen.pensize(3)
pen.goto(bx, by)
pen.goto(cx, cy)
pen.goto(ax, ay)

screen.update()
screen.mainloop()