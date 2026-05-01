"""
分形树 · 彩色玻璃花窗
背景黑色，金色描边，树叶部分填充绿色/金色渐变
"""
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Fractal Tree · Stained Glass")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)
pen.pencolor("#FFD700")

# 填充颜色（绿色系）
leaf_colors = [ "#19AA1D"]

def tree(t, branch_len, depth, max_depth):
    if depth == 0:
        return
    
    # 树干部分不填充，仅末梢叶子填充
    t.pensize(max(1, depth // 2))
    t.forward(branch_len)
    
    # 右分支
    t.right(25)
    tree(t, branch_len * 0.7, depth - 1, max_depth)
    
    # 左分支
    t.left(50)
    tree(t, branch_len * 0.7, depth - 1, max_depth)
    
    # 返回
    t.right(25)
    t.backward(branch_len)
    
    # 在末梢添加填充叶片（近似）
    if depth == 1:
        t.fillcolor(leaf_colors[depth % len(leaf_colors)])
        t.begin_fill()
        for _ in range(5):
            t.forward(60)
            t.right(144)
        t.end_fill()

# 绘制树
pen.penup()
pen.goto(0, -280)
pen.setheading(90)
pen.pendown()
tree(pen, 100, 7, 7)

screen.update()
screen.mainloop()