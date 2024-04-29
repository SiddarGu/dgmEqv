
import matplotlib.pyplot as plt
import numpy as np

data = [[2001,120,200],[2002,130,220],[2003,140,250],[2004,160,270],[2005,180,300]]

x = np.array([x[0] for x in data])
y1 = np.array([x[1] for x in data])
y2 = np.array([x[2] for x in data])

plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.plot(x,y1,label='Fast Food Consumption(in billion)')
ax.plot(x,y2,label='Traditional Food Consumption(in billion)')
plt.title('Global Fast Food vs Traditional Food Consumption Over Time', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Consumption(in billion)', fontsize=14)
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.set_xticklabels(x,rotation=45, fontsize=12, ha="right", va="top") 
ax.legend(frameon=True, fontsize=12)
ax.grid(linestyle='--', linewidth=0.7)
for i,j in zip(x,y1):
    ax.annotate('{}'.format(j),xy=(i,j), xytext=(0,-9),textcoords="offset points", ha='center', va='top', fontsize=12)
for i,j in zip(x,y2):
    ax.annotate('{}'.format(j),xy=(i,j), xytext=(0,8),textcoords="offset points", ha='center', va='bottom', fontsize=12)
plt.tight_layout()
plt.savefig('line chart/png/444.png')
plt.clf()