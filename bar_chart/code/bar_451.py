

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[3000, 4000, 5000], [2000, 5000, 6000], [4000, 4000, 7000], [3000, 6000, 8000]])
x_pos = np.arange(4) 

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x_pos, data[:,0], width=0.4, label='Manufacturing', color='g', bottom=0)
ax.bar(x_pos, data[:,1], width=0.4, label='Retail', color='b', bottom=data[:,0])
ax.bar(x_pos, data[:,2], width=0.4, label='Service', color='r', bottom=data[:,0]+data[:,1])

ax.set_title('Manufacturing, Retail, and Service Industries in Four Countries in 2021', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], fontsize=14, rotation='vertical')
ax.set_ylabel('Value in million', fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(1,1), fontsize=14)

plt.tight_layout()
plt.savefig('bar chart/png/527.png')

plt.clf()