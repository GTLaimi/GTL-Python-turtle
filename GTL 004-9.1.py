import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Dragon Curve · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1.5)

# 颜色列表
dragon_colors = ["#ff1744", "#ff9100", "#ffea00", "#00e676", "#00b0ff", "#d500f9"]

def l_system(iterations):
    axiom = "FX"
    rules = {"X": "X+YF+", "Y": "-FX-Y"}
    result = axiom
    for _ in range(iterations):
        result = "".join(rules.get(c, c) for c in result)
    return result

def draw_dragon(t, instructions, step, angle=90):
    color_idx = 0
    for cmd in instructions:
        if cmd == "F":
            t.pencolor(dragon_colors[color_idx % len(dragon_colors)])
            color_idx += 1
            t.forward(step*2)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

# 放大步长，调整起始点使图形居中
pen.penup()
pen.goto(160, 60)  # 经验偏移值
pen.setheading(0)
pen.pendown()

instructions = l_system(12)
draw_dragon(pen, instructions, step=4)  # 步长从 3 增加到 4

screen.update()
screen.mainloop()