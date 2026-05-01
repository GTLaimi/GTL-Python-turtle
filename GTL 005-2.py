# File: tdemo_bifurcation_final.py
# Fast, clean bifurcation diagram with accurate timing

from turtle import *
import time

# ===== 可调参数 =====
width = 400          # r 轴列数 (调小更快)
height = 150         # 每列点数
r_min = 2.5
r_max = 4.0
transient = 200      # 跳过暂态迭代

def f(r, x):
    return r * x * (1 - x)

def bifurcation():
    """极速绘制分叉图，不逐步刷新"""
    tracer(0, 0)         # 完全关闭自动刷新，不绘制任何东西
    hideturtle()
    
    # 用于 stamp 的海龟，点调得很细
    stamper = Turtle()
    stamper.hideturtle()
    stamper.penup()
    stamper.shape("circle")
    stamper.shapesize(0.05, 0.05)   # 极细的点，后期结构清晰
    stamper.color("black")
    
    start = time.time()
    dr = (r_max - r_min) / width
    r = r_min
    
    for i in range(width):
        x = 0.5
        for _ in range(transient):
            x = f(r, x)
        for _ in range(height):
            x = f(r, x)
            stamper.goto(r, x)
            stamper.stamp()
        r += dr
    
    # 所有点 stamp 完毕，现在一次性刷新屏幕
    update()
    total = time.time() - start
    
    # 在左上角显示总耗时
    status = Turtle()
    status.hideturtle()
    status.penup()
    status.goto(r_min + 0.05, 1.03)
    status.color("red")
    status.write(f"完成！实际耗时: {total:.2f} 秒",
                 font=("Arial", 12, "bold"))

def main():
    reset()
    setworldcoordinates(r_min, -0.05, r_max, 1.10)
    speed(0)
    hideturtle()
    
    # 坐标轴
    pencolor("gray")
    penup(); goto(r_min, 0); pendown()
    goto(r_max, 0)
    penup(); goto(r_min, 0); pendown()
    goto(r_min, 1)
    penup()
    
    bifurcation()
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()