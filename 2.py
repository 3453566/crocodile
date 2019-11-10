import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['figure.figsize'] = (6, 6)

F1 = open("data.txt",'r');
list = F1.readlines();
list_source = []
for i in range(len(list)):
    column_list = list[i].strip().split(" ")    # 每一行split后是一个列表
    list_source.append(column_list)               # 加入list_source
list = np.array(list_source)


fig, ax = plt.subplots()   #生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割，例：fig.add_subplot(2,2,2).表示将画布分割为两行两列


#ax在第2个子图中绘制，其中行优先，
x0data,y0data,x1data,y1data,x2data,y2data,x3data,y3data= [], [] ,[],[],[], [] ,[],[]     #初始化数组

ln0, = ax.plot([],[], color='r',linewidth=0.8, animated=False)  #第三个参数表示画曲线的颜色和线型，具体参见：https://blog.csdn.net/tengqingyong/article/details/78829596
ln1, = ax.plot([],[], color='k',linewidth=1,animated=False)
ln2, = ax.plot([],[], color='g',linewidth=1,animated=False)
ln3, = ax.plot([],[], color='b',linewidth=1,animated=False)
def init():
    ax.set_xlim(-88, 88)#设置x轴的范围pi代表3.14...圆周率，
    ax.set_ylim(-51, 101)#设置y轴的范围
    return ln0,#返回曲线

def update(n):
    
    x0data.append(float(list[n][0]))         #将每次传过来的n追加到xdata中
    y0data.append(float(list[n][1]))
    x1data.append(float(list[n][2]))         #将每次传过来的n追加到xdata中
    y1data.append(float(list[n][3]))
    x2data.append(float(list[n][4]))         #将每次传过来的n追加到xdata中
    y2data.append(float(list[n][5]))
    x3data.append(float(list[n][6]))         #将每次传过来的n追加到xdata中
    y3data.append(float(list[n][7]))
    ln0.set_data(x0data, y0data)    #重新设置曲线的值
    ln1.set_data(x1data, y1data)
    ln2.set_data(x2data, y2data)
    ln3.set_data(x3data, y3data)
    #print(xdata, ydata)
    return ln0,ln1,ln2,ln3,


ani = FuncAnimation(fig, update, frames=range(len(list)),#这里的frames在调用update函数是会将frames作为实参传递给“n”
                    init_func=init, blit=True)
ani.save('1.gif', dpi=1000)
plt.show()


