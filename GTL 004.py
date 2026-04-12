"""
分形矩阵 · 九宫格布局
- 3×3 网格排列九种分形
- 白色背景，深蓝/墨绿色线条
- 每个格子带标题和细边框
- 统一尺度，理性对齐
"""
import turtle
import math

# 屏幕设置
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("white")
screen.title("分形矩阵 · 九宫格")
screen.tracer(0)

# 主画笔
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)

# 网格参数
COLS, ROWS = 3, 3
CELL_W, CELL_H = 280, 280
START_X, START_Y = -420, 420
TITLE_OFFSET = -110

# 颜色定义
COLOR_PRIMARY = "#1a237e"   # 深蓝
COLOR_SECONDARY = "#004d40" # 深绿
COLOR_ACCENT = "#4a148c"    # 深紫

# ==================== 分形函数库 ====================
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

def sierpinski_tri(t, ax, ay, bx, by, cx, cy, depth):
    if depth == 0:
        t.penup()
        t.goto(ax, ay)
        t.pendown()
        t.begin_fill()
        t.goto(bx, by)
        t.goto(cx, cy)
        t.goto(ax, ay)
        t.end_fill()
    else:
        abx, aby = (ax + bx) / 2, (ay + by) / 2
        bcx, bcy = (bx + cx) / 2, (by + cy) / 2
        cax, cay = (cx + ax) / 2, (cy + ay) / 2
        sierpinski_tri(t, ax, ay, abx, aby, cax, cay, depth - 1)
        sierpinski_tri(t, abx, aby, bx, by, bcx, bcy, depth - 1)
        sierpinski_tri(t, cax, cay, bcx, bcy, cx, cy, depth - 1)

def tree(t, branch_len, depth, max_depth):
    if depth == 0:
        return
    t.pensize(max(1, depth // 2))
    t.forward(branch_len)
    t.right(25)
    tree(t, branch_len * 0.7, depth - 1, max_depth)
    t.left(50)
    tree(t, branch_len * 0.7, depth - 1, max_depth)
    t.right(25)
    t.backward(branch_len)

def draw_hex_fractal(t, x, y, radius, depth):
    if depth == 0:
        return
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    for _ in range(6):
        t.forward(radius)
        t.left(60)
    new_radius = radius * 0.5
    for angle in [0, 60, 120, 180, 240, 300]:
        rad = math.radians(angle)
        nx = x + radius * math.cos(rad)
        ny = y + radius * math.sin(rad)
        draw_hex_fractal(t, nx, ny, new_radius, depth - 1)

def square_fractal(t, size, depth):
    if depth == 0:
        return
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.forward(size / 2)
    t.left(45)
    square_fractal(t, size * 0.707, depth - 1)
    t.right(45)
    t.backward(size / 2)

def draw_circles(t, x, y, radius, depth):
    if depth == 0:
        return
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)
    new_radius = radius * 0.5
    draw_circles(t, x, y + radius * 0.5, new_radius, depth - 1)
    draw_circles(t, x - radius * 0.5, y - radius * 0.3, new_radius, depth - 1)
    draw_circles(t, x + radius * 0.5, y - radius * 0.3, new_radius, depth - 1)

def cantor_set(t, x, y, length, depth):
    if depth == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(length)
    else:
        cantor_set(t, x, y, length / 3, depth - 1)
        cantor_set(t, x + 2 * length / 3, y, length / 3, depth - 1)

def levy_c_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        t.left(45)
        levy_c_curve(t, length * 0.707, depth - 1)
        t.right(90)
        levy_c_curve(t, length * 0.707, depth - 1)
        t.left(45)

# ==================== 辅助函数：绘制格子 ====================
def draw_cell_frame(t, cx, cy, w, h, title):
    """绘制单元格边框和标题"""
    t.penup()
    t.goto(cx - w/2, cy - h/2)
    t.pendown()
    t.pencolor("#b0bec5")
    t.pensize(1)
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.penup()
    t.goto(cx, cy + h/2 + 10)
    t.pencolor("#1a237e")
    t.write(title, align="center", font=("Courier New", 10, "bold"))

# ==================== 分形绘制调度 ====================
# 定义九宫格内容 (行, 列, 函数, 参数, 标题, 颜色)
cells = [
    # 第一行
    (0, 0, "koch", {"order": 3, "size": 80}, "Koch Snowflake", COLOR_PRIMARY),
    (0, 1, "sierpinski", {"depth": 4}, "Sierpinski Triangle", COLOR_SECONDARY),
    (0, 2, "tree", {"depth": 6, "len": 50}, "Fractal Tree", COLOR_ACCENT),
    # 第二行
    (1, 0, "hex", {"depth": 3, "radius": 60}, "Hexagonal Fractal", COLOR_PRIMARY),
    (1, 1, "square", {"size": 80, "depth": 3}, "Square Fractal", COLOR_SECONDARY),
    (1, 2, "circles", {"radius": 70, "depth": 3}, "Apollonian Circles", COLOR_ACCENT),
    # 第三行
    (2, 0, "cantor", {"depth": 4, "length": 120}, "Cantor Set", COLOR_PRIMARY),
    (2, 1, "levy", {"depth": 10, "length": 8}, "Lévy C Curve", COLOR_SECONDARY),
    (2, 2, "dragon", {}, "Dragon Curve", COLOR_ACCENT),
]

# 绘制每个格子
for row, col, ftype, params, title, color in cells:
    cx = START_X + col * CELL_W + CELL_W/2
    cy = START_Y - row * CELL_H - CELL_H/2
    
    # 画边框和标题
    draw_cell_frame(pen, cx, cy, CELL_W, CELL_H, title)
    
    # 移动到格子中心并设置颜色
    pen.penup()
    pen.goto(cx, cy)
    pen.setheading(0)
    pen.pencolor(color)
    pen.fillcolor("#e8eaf6")
    pen.pensize(1.5)
    
    # 根据类型绘制
    if ftype == "koch":
        pen.penup()
        pen.goto(cx - params["size"]/2, cy - params["size"]*0.3)
        pen.setheading(0)
        pen.pendown()
        for _ in range(3):
            koch_curve(pen, params["order"], params["size"])
            pen.right(120)
    
    elif ftype == "sierpinski":
        h = 100 * math.sqrt(3) / 2
        ax, ay = cx - 50, cy - h/2
        bx, by = cx + 50, cy - h/2
        cx0, cy0 = cx, cy + h/2
        sierpinski_tri(pen, ax, ay, bx, by, cx0, cy0, params["depth"])
    
    elif ftype == "tree":
        pen.penup()
        pen.goto(cx, cy - 40)
        pen.setheading(90)
        pen.pendown()
        tree(pen, params["len"], params["depth"], params["depth"])
    
    elif ftype == "hex":
        draw_hex_fractal(pen, cx, cy, params["radius"], params["depth"])
    
    elif ftype == "square":
        pen.penup()
        pen.goto(cx - params["size"]/2, cy - params["size"]/2)
        pen.setheading(0)
        pen.pendown()
        square_fractal(pen, params["size"], params["depth"])
    
    elif ftype == "circles":
        draw_circles(pen, cx, cy, params["radius"], params["depth"])
    
    elif ftype == "cantor":
        pen.pensize(3)
        for i in range(params["depth"]):
            cantor_set(pen, cx - params["length"]/2, cy - i*15, params["length"], i)
        pen.pensize(1.5)
    
    elif ftype == "levy":
        pen.penup()
        pen.goto(cx - 40, cy - 40)
        pen.setheading(0)
        pen.pendown()
        levy_c_curve(pen, params["length"], params["depth"])
    
    elif ftype == "dragon":
        # 简化龙曲线（使用L-system）
        def dragon_lsystem(n):
            s = "FX"
            rules = {"X": "X+YF+", "Y": "-FX-Y"}
            for _ in range(n):
                s = "".join(rules.get(c, c) for c in s)
            return s
        inst = dragon_lsystem(10)
        pen.penup()
        pen.goto(cx - 30, cy - 30)
        pen.setheading(0)
        pen.pendown()
        for cmd in inst:
            if cmd == "F":
                pen.forward(3)
            elif cmd == "+":
                pen.right(90)
            elif cmd == "-":
                pen.left(90)

# 总标题
pen.penup()
pen.goto(0, 480)
pen.pencolor("#1a237e")
pen.write("Fractal Matrix · 3×3 Gallery", align="center", font=("Courier New", 20, "bold"))

screen.update()
screen.mainloop()