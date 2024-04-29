
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[2017,30000,10,100],[2018,50000,15,110],[2019,70000,20,120],[2020,90000,25,130]])

plt.figure(figsize=(8, 6))
ax = plt.subplot()
ax.plot(data[:,0], data[:,1], color='#006400', linewidth=2, label='Number of Tourists')
ax.plot(data[:,0], data[:,2], color='#ffa500', linewidth=2, label='Tourism Revenue (billion dollars)')
ax.plot(data[:,0], data[:,3], color='#0000ff', linewidth=2, label='Average Spending per Head (dollars)')
ax.set_title('Tourism development in the United States from 2017 to 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.legend(loc='upper left', frameon=False, fontsize=10)
ax.grid(True, color='#808080', linestyle='--', linewidth=1)

for x, y1, y2, y3 in data:
    ax.annotate('{}'.format(y1), (x, y1), xytext=(-8, 4), textcoords='offset points')
    ax.annotate('{}'.format(y2), (x, y2), xytext=(-8, 4), textcoords='offset points')
    ax.annotate('{}'.format(y3), (x, y3), xytext=(-8, 4), textcoords='offset points')

ax.set_xticks(data[:,0])   
ax.set_xticklabels(data[:,0], rotation=0)
plt.tight_layout()
plt.savefig('line chart/png/313.png')
plt.clf()