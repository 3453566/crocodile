import turtle
import math
# 设置人，鳄鱼1，2，3位置信息
per = (0.00, math.sqrt(7500))
tim =0.2  # 人在0.2秒内奔跑为一单位
dmin = 5
lion1,lspeed1 = (-150.00, 0.00),15*tim
lion2,lspeed2 = (150.00, 0.00),20*tim
lion3,lspeed3 = (0.00, math.sqrt(7500)+150),20*tim
for i in range(1000):
    # 鳄鱼1前进了15
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(lion1)
    turtle.pendown()
    lion1_per = turtle.towards(per)
    turtle.setheading(lion1_per)
    turtle.fd(lspeed1)
    lion1 = turtle.position()

    # 鳄鱼2前进了20
    turtle.color("red")
    turtle.penup()
    turtle.goto(lion2)
    turtle.pendown()
    turtle.setheading(turtle.towards(per))
    turtle.fd(lspeed2)
    lion2 = turtle.position()

    # 鳄鱼3前进了20
    turtle.color("green")
    turtle.penup()
    turtle.goto(lion3)
    turtle.pendown()
    turtle.setheading(turtle.towards(per))
    turtle.fd(lspeed3)
    lion3 = turtle.position()


    # 人来比较谁会比较先吃到我
    turtle.color("black")
    turtle.penup()
    turtle.goto(per)
    turtle.pendown()
    d1 = turtle.distance(lion1)
    d2 = turtle.distance(lion2)
    d3 = turtle.distance(lion3)
    t1 = d1/lspeed1
    t2 = d2/lspeed2
    t3 = d3/lspeed3
    if t1 == min(t1,t2,t3):
        per_lion1 = turtle.towards(lion1)
        turtle.setheading(per_lion1+180)
        turtle.fd(lspeed1)
    elif t2 == min(t1,t2,t3):
        per_lion2 = turtle.towards(lion2)
        turtle.setheading(per_lion2+180)
        turtle.fd(lspeed2)
    else :
        per_lion3 = turtle.towards(lion3)
        turtle.setheading(180+per_lion3)
        turtle.fd(lspeed3)
    per = turtle.position()
    # 当人在下一个tim秒内跑过的距离小于任意一只鳄鱼在下一个tim秒内跑过的距离时跳出循环，输出奔跑的总时间

    if min(t1,t2,t3)<=tim :
        break



