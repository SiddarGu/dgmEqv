
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[500,3000,500,1000],[550,3200,550,1100],[600,3500,600,1200],[650,3700,650,1300]])
x = np.array([4,5,6,7])

plt.figure(figsize=(10,6))
plt.title("Social Media Users in the first half of 2020")
plt.xticks([4,5,6,7],['April 2020','May 2020','June 2020','July 2020'])
ax = plt.gca()
ax.grid(linestyle='--',alpha=0.5)

ax.set_xlabel('Month')
ax.set_ylabel('Users (million)')

ax.plot(x,data[:,0],label='Instagram Users',color='red',marker='o',linestyle='--')
ax.plot(x,data[:,1],label='Facebook Users',color='blue',marker='^',linestyle='-.')
ax.plot(x,data[:,2],label='Twitter Users',color='green',marker='s',linestyle=':')
ax.plot(x,data[:,3],label='Youtube Users',color='black',marker='*',linestyle='-')

for x0,y0 in zip(x,data[:,0]):
    ax.annotate(y0,(x0,y0),rotation=45,verticalalignment='bottom',horizontalalignment='right',wrap=True)
for x1,y1 in zip(x,data[:,1]):
    ax.annotate(y1,(x1,y1),rotation=45,verticalalignment='bottom',horizontalalignment='left',wrap=True)
for x2,y2 in zip(x,data[:,2]):
    ax.annotate(y2,(x2,y2),rotation=45,verticalalignment='top',horizontalalignment='right',wrap=True)
for x3,y3 in zip(x,data[:,3]):
    ax.annotate(y3,(x3,y3),rotation=45,verticalalignment='top',horizontalalignment='left',wrap=True)

ax.legend()
plt.tight_layout()
plt.savefig('line chart/png/265.png')
plt.clf()