#设有三条鳄鱼ABC分别站在等边三角形的三个角上，一个人站在三角形的正中间。每条鳄鱼和人的距离为100米，人的奔跑速度是10m/s鳄鱼A的奔跑速度是15m/s鳄鱼B和C的奔跑速度是20m/s,问:这个人最多还能活几秒?
import math
import time
t = 0
tim = 0.001
#以人为原点建立平面直角坐标系
x0 = 0
y0 = 0
s0 = 10*tim #人在0.01秒内的奔跑距离
#鳄鱼A在人的正上方
x1 = 0
y1 = 100
s1 = 15*tim
#鳄鱼B在人的左下方
x2 = -math.sqrt(7500) #大概是86.6
y2 = -50
s2 = 20*tim
#鳄鱼C在人的右下方
x3 = math.sqrt(7500) 
y3 = -50
s3 = 20*tim
txt = ''

f = open('data.txt','w')
f.write("")
f.close
t1 = 0
t2 = 0
t3 = 0
while True :
   #计算三只鳄鱼此刻若延直线分别需要多久能追上人
    t1 = math.sqrt(math.pow(x1-x0,2)+math.pow(y1-y0,2)) /15
    t2 = math.sqrt(math.pow(x2-x0,2)+math.pow(y2-y0,2)) /20
    t3 = math.sqrt(math.pow(x3-x0,2)+math.pow(y3-y0,2)) /20
    #当人在下一个0.001秒内跑过的距离小于任意一只鳄鱼在下一个0.01秒内跑过的距离时跳出循环，输出奔跑的总时间
    if t1<tim :
        print(t,"t1")
        break
    if t2<tim :
        print(t,"t2")
        break
    if t3<tim :
        print(t,"t3")
        break
    #判断此刻哪只鳄鱼以直线追上人所需时间最短，并使人往远离此鳄鱼的方向跑
    if t1==min(t1,t2,t3):
        x0 = x0+ math.cos(math.atan((y1-y0)/(x1-x0)))*s0
        y0 = y0+ math.sin(math.atan((y1-y0)/(x1-x0)))*s0
       # print(x0,y0)
    else :
        if t2==min(t1,t2,t3):
            x0 = x0+ math.cos(math.atan((y2-y0)/(x2-x0)))*s0
            y0 = y0+ math.sin(math.atan((y2-y0)/(x2-x0)))*s0
          #  print(x0,y0)
        else:
            if t3==min(t1,t2,t3):
                x0 = x0+ math.cos(math.atan((y3-y0)/(x3-x0)))*s0
                #鳄鱼c的横坐标与人相遇时变号
                if x0>x3:
                    y0 = y0+ math.sin(math.atan((y3-y0)/(x3-x0)))*s0
                else :
                    y0 = y0+ math.sin(math.atan((y3-y0)/(x0-x3)))*s0
    #使鳄鱼始终朝着人的方向跑
    x1 = x1 + math.cos(math.atan((y1-y0)/(x1-x0)))*s1
    y1 = y1 + math.sin(math.atan((y1-y0)/(x1-x0)))*s1
    x2 = x2 + math.cos(math.atan((y2-y0)/(x2-x0)))*s2
    y2 = y2 + math.sin(math.atan((y2-y0)/(x2-x0)))*s2
    if x0>x3:
        x3 = x3 + math.cos(math.atan((y0-y3)/(x0-x3)))*s3
        y3 = y3 - math.sin(math.atan((y3-y0)/(x0-x3)))*s3
    else :
        x3 = x3 - math.cos(math.atan((y0-y3)/(x0-x3)))*s3
        y3 = y3 - math.sin(math.atan((y0-y3)/(x0-x3)))*s3
    t = t + tim
    #print(x0,y0,x1,y1,x2,y2,x3,y3)
    
    txt = str(x0)+" "+str(y0)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+" "+str(x3)+" "+str(y3)+'\n'
    #print(txt)
    f = open('data.txt','a')
    f.write(txt)
    f.close
    print(txt)
    
    
    #print(t)
