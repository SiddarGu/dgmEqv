
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y1 = np.array([5,7,9,11,12,14,17,19])
y2 = np.array([10,12,15,18,20,22,25,27])
y3 = np.array([3,4,5,6,7,8,9,10])

fig = plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot(x,y1,label='Domestic Tourists', color='r')
ax.plot(x,y2,label='International Tourists', color='b')
ax.plot(x,y3,label='Revenue', color='g')
ax.set_xticks(x)
ax.set_xticklabels(['January','February','March','April','May','June','July','August'], rotation=45)
ax.set_title('Number of Domestic and International Tourists and Revenue in the USA, 2021', fontsize=20, fontweight='bold')
ax.set_xlabel('Month', fontsize=15)
ax.set_ylabel('Value', fontsize=15)
ax.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/522.png')
plt.clf()