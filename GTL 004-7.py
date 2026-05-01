import turtle

screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("black")
screen.title("Cantor Set · Stained Glass")
screen.tracer(0)

pencolor=["#fabcab","#fcd5ce","#f8edeb","#f9dcc4","#f4acb7"]
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(4)


def cantor(t, x, y, length, depth):
    if depth == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(length)
    else:
        cantor(t, x, y, length / 3, depth - 1)
        cantor(t, x + 2 * length / 3, y, length / 3, depth - 1)

# 绘制多层康托尔集
start_y = 100
for i in range(5):
    pen.pencolor(pencolor[i % len(pencolor)])
    cantor(pen, -300, start_y - i * 40, 600, i)

screen.update()
screen.mainloop()