# File: tdemo_cobweb.py
# A demonstration of cobweb plot for the logistic map

from turtle import *

N = 50          # 迭代次数
r = 3.9         # 参数 r
x0 = 0.2        # 初始值

def f(x):
    """逻辑斯蒂映射"""
    return r * x * (1 - x)

def jumpto(x, y):
    penup()
    goto(x, y)

def line(x1, y1, x2, y2):
    """画一条线段"""
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():
    """坐标系：抛物线 y = f(x) 和直线 y = x，范围 [0,1]"""
    # 坐标轴
    line(0, 0, 1, 0)
    line(0, 0, 0, 1)
    # 画抛物线 f(x)
    pencolor("gray")
    jumpto(0, f(0))
    pendown()
    for i in range(101):
        x = i / 100
        goto(x, f(x))
    # 画直线 y = x
    pencolor("gray")
    jumpto(0, 0)
    pendown()
    goto(1, 1)

def cobweb(start, color):
    """从 start 开始画蛛网迭代"""
    pencolor(color)
    x = start
    y = 0
    jumpto(x, y)
    pendown()
    dot(5)
    for _ in range(N):
        # 垂直移动到 y = f(x)
        y = f(x)
        goto(x, y)
        dot(5)
        # 水平移动到 y = x
        x = y
        goto(x, y)
        dot(5)

def main():
    reset()
    setworldcoordinates(-0.1, -0.1, 1.1, 1.1)
    speed(6)
    hideturtle()
    coosys()
    cobweb(x0, "blue")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()