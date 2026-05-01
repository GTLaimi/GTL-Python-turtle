import turtle as t
t.speed(100)
t.pencolor('#FFFFFF')
t.fillcolor('#FABCAB')
t.begin_fill()
for a in range(91):
    t.circle(4*a)
    t.left(2*a)
t.end_fill()
t.mainloop()