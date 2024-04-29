
import matplotlib.pyplot as plt
import numpy as np

data = [[1000,50],[1200,65],[1400,80],[1600,90]]
labels = ['Rail','Road','Air','Sea']

fig = plt.figure()
ax = fig.add_subplot()
ax.bar(labels, [i[1] for i in data], label='Cost')
ax.bar(labels, [i[0] for i in data], bottom=[i[1] for i in data], label='Distance (km)')
plt.xticks(labels)
plt.legend()
plt.title('Cost and distance of transportation by different modes in 2021')

for x,y in enumerate(data):
    ax.annotate(str(y[1]), xy=(x,y[1]), xytext=(0,3), 
                textcoords="offset points", ha='center', va='bottom')
    ax.annotate(str(y[0]), xy=(x,y[1]), xytext=(0,-3), 
                textcoords="offset points", ha='center', va='top')

plt.tight_layout()
plt.savefig('Bar Chart/png/435.png', bbox_inches='tight')
plt.clf()