"""
方形递归分形 · 彩色玻璃花窗
背景黑色，金色描边，每个正方形填充不同颜色
"""
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Square Fractal · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)
pen.pencolor("#00CCFF")

# 填充颜色
square_colors = [ "#28c6c6" ,  "#28b1b1" , "#289c9c" , "#288787" ]

def square_fractal(t, size, depth):
    if depth == 0:
        return
    # 绘制并填充正方形
    t.fillcolor(square_colors[depth % len(square_colors)])
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    
    # 移动到下一个位置
    t.forward(size / 2)
    t.left(45)
    square_fractal(t, size * 0.707, depth - 1)
    t.right(45)
    t.backward(size / 2)

pen.penup()
pen.goto(-100, -100)
pen.setheading(0)
pen.pendown()
square_fractal(pen, 200, 5)

screen.update()
screen.mainloop()