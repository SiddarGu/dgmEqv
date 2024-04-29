

import matplotlib.pyplot as plt
import numpy as np

data = [['North America',10000,15000,5000],
        ['Europe',8000,14000,4000],
        ['Asia',9000,13000,6000],
        ['South America',7000,12000,5000]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

index = np.arange(len(data))
width = 0.2

ax.bar(index-width, [i[1] for i in data], width, color='blue', label='Doctors')
ax.bar(index, [i[2] for i in data], width, color='orange', label='Nurses')
ax.bar(index+width, [i[3] for i in data], width, color='green', label='Hospitals')
ax.set_xticks(index)
ax.set_xticklabels([i[0] for i in data], rotation=0)
ax.legend()
ax.set_title('Number of doctors, nurses, and hospitals in four regions in 2021')

for i in index:
    ax.annotate(str(data[i][1]), xy=(i-width, data[i][1]), ha='center', va='bottom', rotation=0)
    ax.annotate(str(data[i][2]), xy=(i, data[i][2]), ha='center', va='bottom', rotation=0)
    ax.annotate(str(data[i][3]), xy=(i+width, data[i][3]), ha='center', va='bottom', rotation=0)

plt.tight_layout()
plt.savefig('Bar Chart/png/537.png')
plt.clf()