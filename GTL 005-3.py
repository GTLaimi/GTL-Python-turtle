# File: tdemo_lorenz.py
# A simplified Lorenz attractor using turtle graphics

from turtle import *

# Lorenz 系统参数
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

dt = 0.01          # 时间步长
steps = 5000       # 迭代步数

def lorenz(x, y, z):
    """Lorenz 系统导数"""
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def main():
    reset()
    # 设置坐标范围以适合 x-z 投影
    setworldcoordinates(-30, 0, 30, 60)
    speed(0)
    hideturtle()
    
    # 初始条件
    x, y, z = 0.1, 0.0, 0.0
    
    penup()
    goto(x, z)
    pendown()
    pencolor("blue")
    
    for _ in range(steps):
        dx, dy, dz = lorenz(x, y, z)
        x += dx * dt
        y += dy * dt
        z += dz * dt
        goto(x, z)      # 投影到 x-z 平面
    
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()