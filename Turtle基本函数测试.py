# turtle.setheading(角度)：设置当前画笔朝向，即人或鳄鱼的朝向
# D = turtle.distance(positionLion1)：获取两个坐标之间的距离
# positionHuman = turtle.position()：得到当前位置的坐标（用来获得人或鳄鱼在每次运动之后的坐标）
# turtle.towards()：得到两个坐标之间的相位角（鳄鱼需要不停的调整角度来使鳄鱼的脸一直朝着人的方向，用这个方法来获得鳄鱼所需调整的角度）
# Turtle.goto(positionHuman) 去这个坐标所在位置
# lion_per = turtle.towards(per)获得2坐标相位角
# turtle.fd(15)前进15个单位

import turtle
# 设置人，鳄鱼1，2，3位置信息
per = (-86, -86.00)
lion1 = (-150.00, 0.00)
lion2 = (150.00, 0.00)
lion3 = (0.00, 260.00)

turtle.color("yellow")
turtle.goto(lion1)

turtle.pendown()
print(123)