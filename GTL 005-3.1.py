# File: tdemo_lorenz_3views.py
# Lorenz attractor with three synchronized projections
# Shows xOy, xOz, yOz planes and live info
from turtle import *
import time

# ========== 可调参数 ==========
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
dt = 0.01
steps = 15000         # 总迭代步数
draw_delay = 0.05     # 每次刷新后的暂停时间（秒），调大可以让绘制更慢

# ========== 各投影的数值范围 ==========
X_RANGE = (-25, 25)
Y_RANGE = (-30, 30)
Z_RANGE = (0, 50)

# ========== 画布布局（世界坐标 0~200） ==========
def map_xOy(x, y):
    wx = 15 + (x - X_RANGE[0]) / (X_RANGE[1] - X_RANGE[0]) * 70
    wy = 15 + (y - Y_RANGE[0]) / (Y_RANGE[1] - Y_RANGE[0]) * 70
    return wx, wy

def map_xOz(x, z):
    wx = 15 + (x - X_RANGE[0]) / (X_RANGE[1] - X_RANGE[0]) * 70
    wy = 115 + (z - Z_RANGE[0]) / (Z_RANGE[1] - Z_RANGE[0]) * 70
    return wx, wy

def map_yOz(y, z):
    wx = 115 + (y - Y_RANGE[0]) / (Y_RANGE[1] - Y_RANGE[0]) * 70
    wy = 115 + (z - Z_RANGE[0]) / (Z_RANGE[1] - Z_RANGE[0]) * 70
    return wx, wy

def draw_axes():
    """画出三个投影窗口的边框与坐标轴标注"""
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("gray")
    t.pensize(1)

    # ------ xOy ------
    t.penup(); t.goto(15, 15); t.pendown()
    t.goto(85, 15); t.goto(85, 85); t.goto(15, 85)
    t.goto(15, 15)
    t.penup(); t.goto(50, 5); t.write("xOy 投影", align="center", font=("Arial", 9, "bold"))
    t.penup(); t.goto(15, 15); t.pendown(); t.goto(85, 15); t.penup()
    t.goto(15, 15); t.pendown(); t.goto(15, 85); t.penup()
    t.goto(85, 15); t.write("x", font=("Arial", 8))
    t.goto(15, 85); t.write("y", font=("Arial", 8))

    # ------ xOz ------
    t.penup(); t.goto(15, 115); t.pendown()
    t.goto(85, 115); t.goto(85, 185); t.goto(15, 185)
    t.goto(15, 115)
    t.penup(); t.goto(50, 105); t.write("xOz 投影", align="center", font=("Arial", 9, "bold"))
    t.penup(); t.goto(15, 115); t.pendown(); t.goto(85, 115); t.penup()
    t.goto(15, 115); t.pendown(); t.goto(15, 185); t.penup()
    t.goto(85, 115); t.write("x", font=("Arial", 8))
    t.goto(15, 185); t.write("z", font=("Arial", 8))

    # ------ yOz ------
    t.penup(); t.goto(115, 115); t.pendown()
    t.goto(185, 115); t.goto(185, 185); t.goto(115, 185)
    t.goto(115, 115)
    t.penup(); t.goto(150, 105); t.write("yOz 投影", align="center", font=("Arial", 9, "bold"))
    t.penup(); t.goto(115, 115); t.pendown(); t.goto(185, 115); t.penup()
    t.goto(115, 115); t.pendown(); t.goto(115, 185); t.penup()
    t.goto(185, 115); t.write("y", font=("Arial", 8))
    t.goto(115, 185); t.write("z", font=("Arial", 8))

def main():
    setup(width=800, height=800)
    setworldcoordinates(0, 0, 200, 200)
    speed(0)
    hideturtle()
    tracer(0, 0)

    draw_axes()
    update()

    # 三个投影轨迹海龟
    t_xy = Turtle()
    t_xy.hideturtle()
    t_xy.pencolor("blue")
    t_xy.pensize(1)
    t_xy.penup()

    t_xz = Turtle()
    t_xz.hideturtle()
    t_xz.pencolor("green")
    t_xz.pensize(1)
    t_xz.penup()

    t_yz = Turtle()
    t_yz.hideturtle()
    t_yz.pencolor("red")
    t_yz.pensize(1)
    t_yz.penup()

    # 信息显示海龟
    info = Turtle()
    info.hideturtle()
    info.penup()
    info.color("black")

    # 初始条件
    x, y, z = 0.1, 0.0, 0.0

    wx, wy = map_xOy(x, y)
    t_xy.goto(wx, wy)
    t_xy.pendown()

    wx, wy = map_xOz(x, z)
    t_xz.goto(wx, wy)
    t_xz.pendown()

    wx, wy = map_yOz(y, z)
    t_yz.goto(wx, wy)
    t_yz.pendown()

    start_time = time.time()
    refresh_every = 30   # 多少步刷新一次

    for i in range(1, steps + 1):
        # Lorenz 方程
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt

        # 三个投影添加新线段
        t_xy.goto(*map_xOy(x, y))
        t_xz.goto(*map_xOz(x, z))
        t_yz.goto(*map_yOz(y, z))

        # 定时更新信息
        if i % refresh_every == 0:
            elapsed = time.time() - start_time
            mins = int(elapsed // 60)
            secs = int(elapsed % 60)
            millis = int((elapsed - int(elapsed)) * 1000)
            time_str = f"{mins:02d}:{secs:02d}:{millis:03d}"

            info.clear()
            y_pos = 82
            dy = 6
            info.goto(117, y_pos)
            info.write("Lorenz 吸引子", font=("Arial", 10, "bold"))
            y_pos -= dy
            info.goto(117, y_pos)
            info.write(f"σ={sigma}  ρ={rho}  β={beta:.3f}", font=("Arial", 8))
            y_pos -= dy
            info.goto(117, y_pos)
            info.write(f"dt={dt}  总步数={steps}", font=("Arial", 8))
            y_pos -= dy*1.2
            info.goto(117, y_pos)
            info.write(f"运行 {time_str}", font=("Arial", 10, "bold"))
            y_pos -= dy
            info.goto(117, y_pos)
            info.write("当前位置:", font=("Arial", 8, "underline"))
            y_pos -= dy
            info.goto(120, y_pos)
            info.write(f"x = {x:.4f}", font=("Arial", 8, "italic"))
            y_pos -= dy*0.8
            info.goto(120, y_pos)
            info.write(f"y = {y:.4f}", font=("Arial", 8, "italic"))
            y_pos -= dy*0.8
            info.goto(120, y_pos)
            info.write(f"z = {z:.4f}", font=("Arial", 8, "italic"))
            y_pos -= dy*1.2
            info.goto(117, y_pos)
            info.write("方程:", font=("Arial", 8, "underline"))
            y_pos -= dy
            info.goto(120, y_pos)
            info.write("dx/dt = σ(y-x)", font=("Arial", 7))
            y_pos -= dy*0.8
            info.goto(120, y_pos)
            info.write("dy/dt = x(ρ-z)-y", font=("Arial", 7))
            y_pos -= dy*0.8
            info.goto(120, y_pos)
            info.write("dz/dt = xy - βz", font=("Arial", 7))

            update()
            time.sleep(draw_delay)   # 调慢绘制速度的关键

    # 最终统计
    elapsed = time.time() - start_time
    mins = int(elapsed // 60)
    secs = int(elapsed % 60)
    millis = int((elapsed - int(elapsed)) * 1000)
    time_str = f"{mins:02d}:{secs:02d}:{millis:03d}"
    info.goto(117, 5)
    info.write(f"完成! 总耗时: {time_str}", font=("Arial", 9, "bold"))
    update()
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()