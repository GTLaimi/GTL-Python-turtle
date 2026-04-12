import turtle
import random

# 初始化屏幕
screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor('#0a1f1e')  # 深墨绿背景
screen.title("分形树 · 春意盎然")
screen.tracer(0)  # 关闭动画，绘制完成后一次性更新

# 画笔设置
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)
pen.left(90)  # 向上
pen.penup()
pen.goto(0, -300)
pen.pendown()

# 颜色渐变函数：从深棕色到翠绿，再到嫩黄
def get_color(depth, max_depth):
    if depth < max_depth * 0.3:
        # 树干部分：棕色系
        r = 101 + int(80 * (depth / (max_depth * 0.3)))
        g = 67 + int(40 * (depth / (max_depth * 0.3)))
        b = 33
    elif depth < max_depth * 0.7:
        # 树枝部分：绿色渐变
        ratio = (depth - max_depth * 0.3) / (max_depth * 0.4)
        r = 34 + int(80 * (1 - ratio))
        g = 139 + int(60 * ratio)
        b = 34 + int(40 * ratio)
    else:
        # 末梢：嫩黄/浅绿
        ratio = (depth - max_depth * 0.7) / (max_depth * 0.3)
        r = 154 + int(100 * ratio)
        g = 205 + int(50 * (1 - ratio))
        b = 50 + int(100 * ratio)
    return f'#{r:02x}{g:02x}{b:02x}'

def tree(branch_len, depth, max_depth):
    if depth == 0:
        return
    
    # 颜色随深度变化
    pen.color(get_color(depth, max_depth))
    pen.pensize(max(1, depth // 2))
    
    # 主枝干
    pen.forward(branch_len)
    
    # 右分支
    pen.right(20 + random.randint(-5, 8))  # 随机摇曳
    tree(branch_len * (0.65 + random.random() * 0.1), depth - 1, max_depth)
    
    # 左分支
    pen.left(40 + random.randint(-8, 5))
    tree(branch_len * (0.6 + random.random() * 0.15), depth - 1, max_depth)
    
    # 归位
    pen.right(20 + random.randint(-5, 5))
    pen.backward(branch_len)

# 绘制参数
MAX_DEPTH = 12
pen.penup()
pen.goto(0, -280)
pen.pendown()
tree(120, MAX_DEPTH, MAX_DEPTH)

# 地面点缀几片落叶（小圆点）
pen.penup()
pen.goto(-30, -290)
for _ in range(12):
    x = random.randint(-200, 200)
    y = random.randint(-300, -270)
    pen.goto(x, y)
    pen.dot(random.randint(4, 8), '#8b5a2b')
    
screen.update()
screen.mainloop()