
import matplotlib.pyplot as plt 
import numpy as np 

data = [[2010,100,80,120,150],
        [2011,120,90,110,160],
        [2012,80,110,130,120],
        [2013,150,120,140,80]]

x = np.array(data)[:,0]
y1 = np.array(data)[:,1]
y2 = np.array(data)[:,2]
y3 = np.array(data)[:,3]
y4 = np.array(data)[:,4]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,1,1)
ax.plot(x,y1,label='Donations A(million dollars)',marker='o',linestyle='--',color='r',markersize=10,linewidth=2)
ax.plot(x,y2,label='Donations B(million dollars)',marker='s',linestyle=':',color='b',markersize=10,linewidth=2)
ax.plot(x,y3,label='Donations C(million dollars)',marker='^',linestyle='-.',color='g',markersize=10,linewidth=2)
ax.plot(x,y4,label='Donations D(million dollars)',marker='d',linestyle='-',color='m',markersize=10,linewidth=2)
plt.xticks(x)
for a,b in zip(x,y1):
    ax.annotate('%.1f' % b,xy=(a,b),xytext=(a-0.2,b+1)) 
for a,b in zip(x,y2):
    ax.annotate('%.1f' % b,xy=(a,b),xytext=(a-0.2,b+1)) 
for a,b in zip(x,y3):
    ax.annotate('%.1f' % b,xy=(a,b),xytext=(a-0.2,b+1)) 
for a,b in zip(x,y4):
    ax.annotate('%.1f' % b,xy=(a,b),xytext=(a-0.2,b+1)) 
plt.title('Donations for four charity organizations from 2010 to 2013')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/271.png')
plt.clf()