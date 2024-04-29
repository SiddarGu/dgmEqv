
import matplotlib.pyplot as plt
import numpy as np

data = [['North', 1000, 200], 
        ['South', 1200, 230], 
        ['East', 1400, 270], 
        ['West', 1500, 320]]

x = np.arange(len(data))

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
ax.bar(x - 0.2, [i[1] for i in data], width=0.2, color='b', label='Hospital Bed Capacity')
ax.bar(x, [i[2] for i in data], width=0.2, color='g', label='Doctor Availability')
ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data], fontsize=9, rotation=20, ha='right')
ax.set_title('Healthcare resources in four regions in 2021', fontsize=14)
ax.legend(loc='best')
fig.tight_layout()
plt.savefig('bar chart/png/476.png')
plt.clf()