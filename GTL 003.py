import turtle
import colorsys
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('#0b0c10')
screen.title("彩虹螺旋 · 无限延伸")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

# 绘制一个复杂的螺旋组合，颜色基于HSV循环
def rainbow_spiral():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    # 螺旋参数
    turns = 8          # 旋转圈数
    steps = 600        # 总步数
    start_radius = 5
    growth = 1.8       # 半径增长率
    
    for i in range(steps):
        # 计算进度
        progress = i / steps
        angle = progress * 360 * turns
        
        # 螺旋半径逐渐增大
        r = start_radius + growth * angle * 0.05
        
        # 计算位置（使用阿基米德螺旋公式）
        rad = math.radians(angle)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        
        # 颜色：HSL彩虹渐变，饱和度、亮度维持高值
        hue = (progress * 3) % 1.0  # 多次循环彩虹
        saturation = 0.9
        value = 1.0
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        pen.color(rgb)
        
        # 动态线宽：外圈稍细
        pen.pensize(max(1, 4 - progress * 2))
        
        # 移动到新点（首点用goto，后续用goto亦可，但会形成线段）
        if i == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
        
        # 每隔一段画一个小星星点缀
        if i % 20 == 0 and i > 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            for _ in range(5):
                pen.forward(8)
                pen.backward(8)
                pen.right(72)
            pen.penup()
            pen.goto(x, y)
            pen.pendown()

# 额外绘制一些同心圆环作为背景装饰
def draw_background_rings():
    pen.penup()
    pen.goto(0, 0)
    pen.pensize(1)
    for rad in range(50, 400, 30):
        hue = (rad / 400) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, 0.5, 0.3)
        pen.color(rgb)
        pen.penup()
        pen.goto(0, -rad)
        pen.pendown()
        pen.circle(rad)

# 绘制
draw_background_rings()
rainbow_spiral()

# 中心亮点
pen.penup()
pen.goto(0, 0)
pen.dot(20, 'white')
pen.dot(12, '#FFD700')

screen.update()
screen.mainloop()