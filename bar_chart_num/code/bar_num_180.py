
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

labels = ['Truck','Rail','Ship','Air']
cost = [40,30,50,20]
time = [8,12,15,2]
x = np.arange(len(labels)) 
width = 0.35

ax.bar(x - width/2, cost, width, label='Cost(million)', color='lightgray')
ax.bar(x + width/2, time, width, label='Time(hours)', color='gray')

ax.set_xlabel('Mode')
ax.set_ylabel('Cost/Time')
ax.set_title('Cost and Time of transportation by different modes in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='best')

for i,j in zip(x,cost):
    ax.annotate(str(j),xy=(i-width/2,j+2))
for i,j in zip(x,time):
    ax.annotate(str(j),xy=(i+width/2,j+2))

plt.tight_layout()
plt.savefig('Bar Chart/png/573.png')
plt.clf()