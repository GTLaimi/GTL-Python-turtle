import turtle
import math
import colorsys

# 屏幕设置
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('black')
screen.title("万花筒 · 星芒之花")
screen.tracer(0)

# 主画笔
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)

# 辅助画笔（用于画中心圆点）
dotter = turtle.Turtle()
dotter.speed(0)
dotter.hideturtle()

def draw_petal(radius, angle, hue_start, hue_shift):
    """绘制一片花瓣（贝塞尔风格，用圆弧模拟）"""
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(angle)
    pen.forward(radius * 0.3)
    pen.pendown()
    
    # 颜色随位置渐变
    for i in range(20):
        t = i / 20
        hue = (hue_start + hue_shift * t) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
        pen.color((r, g, b))
        pen.circle(radius, 6)  # 小段弧线
        pen.left(2)
    
    # 返回中心
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(angle + 180)
    pen.forward(radius * 0.3)
    pen.pendown()
    for i in range(20):
        t = i / 20
        hue = (hue_start + hue_shift * (1 - t)) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
        pen.color((r, g, b))
        pen.circle(radius, 6)
        pen.left(2)

def kaleidoscope(petals=12, layers=5, base_radius=30):
    """绘制多层旋转对称花瓣"""
    for layer in range(layers):
        radius = base_radius * (layer + 1) * 1.8
        hue_base = (layer * 0.08) % 1.0  # 每层色调偏移
        
        for p in range(petals):
            angle = (360 / petals) * p + layer * 15  # 层间错位
            hue_start = (hue_base + p * 0.02) % 1.0
            draw_petal(radius, angle, hue_start, 0.15)
    
    # 中心装饰
    dotter.penup()
    dotter.goto(0, 0)
    dotter.dot(base_radius * 1.2, '#FFD700')
    dotter.dot(base_radius * 0.7, '#FFA500')
    dotter.dot(base_radius * 0.3, 'white')

# 绘制主图案
kaleidoscope(petals=16, layers=4, base_radius=25)

# 外圈星芒
pen.penup()
pen.goto(0, 0)
pen.setheading(0)
for i in range(36):
    hue = (i * 0.03) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen.color((r, g, b))
    pen.pensize(2)
    pen.penup()
    pen.forward(230)
    pen.pendown()
    pen.forward(40)
    pen.penup()
    pen.backward(270)
    pen.right(10)

screen.update()
screen.mainloop()