import matplotlib.pyplot as plt
import numpy as np

""" plt.figure(figsize=(7,7))

x = np.linspace(-1,5,50)
zeros = [-0.1 for i in range(len(x))]
y1 = 3-x
y2 = 4-2*x

plt.plot(x,y1,'g',linewidth=4)
plt.plot(x,y2,'b',linewidth=4)
plt.plot(0,3,marker="o", markersize=15, markeredgecolor="black",markerfacecolor="red")

font = {'color':  'black',
        'size': 12
        }

box = {'facecolor': 'none',
       'edgecolor': 'red',
       'boxstyle': 'round'
      }

plt.text(0.35, 3.5, '(0,3) Máximo', fontdict=font, bbox=box)

plt.fill_between(x,zeros,y1,color="green",where=(x>=-0.1)&(y1>=-0.1),alpha=0.2)
plt.fill_between(x,zeros,y2,color="blue",where=(x>=-0.1)&(y2>=-0.1),alpha=0.1)
plt.grid()

plt.legend(["$x_{1} + x_{2} \leq  3$","$x_{1} + 2x_{2}\leq  4$"])
plt.xlabel("$x_{1}$",fontsize=20)
plt.ylabel("$x_{2}$",fontsize=20)
plt.title("Región factible",fontsize=20)

plt.xlim([-0.2,4.5])
plt.ylim([-0.2,4.5])

plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])
 """
""" plt.figure(figsize=(7,7))

x = np.linspace(-1,5,50)
zeros = [-0.1 for i in range(len(x))]
y1 = 3-x
y2 = 4-2*x
y2p = 5-2*x

plt.plot(x,y1,'g',linewidth=4)
plt.plot(x,y2p,'b',linewidth=4)
plt.plot(x,y2,'k--',linewidth=2)
plt.plot(0,3,marker="o", markersize=15, markeredgecolor="black",markerfacecolor="red")

font = {'color':  'black',
        'size': 12
        }

box = {'facecolor': 'none',
       'edgecolor': 'red',
       'boxstyle': 'round'
      }

plt.text(0, 2, '(0,3) Máximo', fontdict=font, bbox=box)

plt.fill_between(x,zeros,y1,color="green",where=(x>=-0.1)&(y1>=-0.1),alpha=0.2)
plt.fill_between(x,zeros,y2p,color="blue",where=(x>=-0.1)&(y2p>=-0.1),alpha=0.1)
plt.grid()

plt.legend(["$x_{1} + x_{2} \leq  3$","$x_{1} + 2x_{2}\leq  5$"])
plt.xlabel("$x_{1}$",fontsize=20)
plt.ylabel("$x_{2}$",fontsize=20)
plt.title("Región factible",fontsize=20)

plt.xlim([-0.2,4.5])
plt.ylim([-0.2,4.5])

plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])

plt.show() """

plt.figure(figsize=(7,7))

x = np.linspace(-1,5,50)
zeros = [-0.1 for i in range(len(x))]
y1 = 3-x
y1p = 4-x
y2 = 4-2*x

plt.plot(x,y1p,'g',linewidth=4)
plt.plot(x,y2,'b',linewidth=4)
plt.plot(x,y1,'k--',linewidth=2)
plt.plot(0,4,marker="o", markersize=15, markeredgecolor="black",markerfacecolor="red")

font = {'color':  'black',
        'size': 12
        }

box = {'facecolor': 'none',
'edgecolor': 'red',
'boxstyle': 'round'
}

plt.text(0.35, 3.9, '(0,4) NUEVO Máximo', fontdict=font, bbox=box)

plt.fill_between(x,zeros,y1p,color="green",where=(x>=-0.1)&(y1p>=-0.1),alpha=0.2)
plt.fill_between(x,zeros,y2,color="blue",where=(x>=-0.1)&(y2>=-0.1),alpha=0.1)
plt.grid()

plt.legend(["$x_{1} + x_{2} \leq  4$","$x_{1} + 2x_{2}\leq  4$"])
plt.xlabel("$x_{1}$",fontsize=20)
plt.ylabel("$x_{2}$",fontsize=20)
plt.title("Región factible",fontsize=20)

plt.xlim([-0.2,4.5])
plt.ylim([-0.2,4.5])

plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])

## ?
## !    asa
## TODO

plt.show()