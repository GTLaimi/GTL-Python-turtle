"""
科赫雪花 · 彩色玻璃花窗
背景黑色，金色描边，内部填充渐变蓝紫色
（修正居中）
"""
import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Koch Snowflake · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)
pen.pencolor("#FFD700")  # 金色描边

# 填充颜色列表（从深蓝到浅蓝）
fill_colors = ["#0d47a1", "#1976d2", "#42a5f5"]

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size3 = size / 3.0
        koch_curve(t, order - 1, size3)
        t.left(60)
        koch_curve(t, order - 1, size3)
        t.right(120)
        koch_curve(t, order - 1, size3)
        t.left(60)
        koch_curve(t, order - 1, size3)

def draw_snowflake():
    # 计算等边三角形边长和中心偏移，使其居中
    size = 300
    # 等边三角形高度
    h = size * math.sqrt(3) / 2
    # 起始点为底边左端点，为了整体居中，计算偏移
    start_x = -size / 2
    start_y = h / 3  # 微调使视觉中心对齐
    
    pen.penup()
    pen.goto(start_x, start_y)
    pen.setheading(0)
    pen.pendown()
    
    for i in range(3):
        pen.fillcolor(fill_colors[i % len(fill_colors)])
        pen.begin_fill()
        koch_curve(pen, 4, size)
        pen.right(120)
        pen.end_fill()

draw_snowflake()

screen.update()
screen.mainloop()
