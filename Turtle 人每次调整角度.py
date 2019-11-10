import turtle

positionHuman = (0.00, 86.00)
positionLion1 = (-150.00, 0.00)
positionLion2 = (150.00, 0.00)
positionLion3 = (0.00, 260.00)
escapeDregree = 240

turtle.pensize(3)
for x in range(100):
    turtle.color("black")
    turtle.penup()
    turtle.goto(positionHuman)
    turtle.dot(2, "yellow")
    turtle.pendown()
    turtle.setheading(escapeDregree)

    lenthLion1 = turtle.distance(positionLion1)
    lenthLion2 = turtle.distance(positionLion2)
    if (x >= 2):
        if (lenthLion1 > lenthLion2):
            escapeDregree = escapeDregree - 20
            turtle.fd(10)
            print("1", escapeDregree)
        else:
            escapeDregree = escapeDregree + 20
            turtle.fd(10)
            print("2", escapeDregree)
    else:
        turtle.fd(10)
        print("3", escapeDregree)

    positionHuman = turtle.position()

    turtle.color("green")
    turtle.penup()
    turtle.goto(positionLion1)
    turtle.dot(2, "green")
    turtle.pendown()
    positionLion1ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion1ToHuman)
    turtle.fd(15)
    positionLion1 = turtle.position()

    turtle.color("red")
    turtle.penup()
    turtle.goto(positionLion2)
    turtle.dot(2, "red")
    turtle.pendown()
    positionLion2ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion2ToHuman)
    turtle.fd(20)
    positionLion2 = turtle.position()

    turtle.color("yellow")
    turtle.penup()
    turtle.goto(positionLion3)
    turtle.dot(2, "yellow")
    turtle.pendown()
    positionLion3ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion3ToHuman)
    turtle.fd(20)
    positionLion3 = turtle.position()