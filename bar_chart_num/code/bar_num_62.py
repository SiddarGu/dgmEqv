
import matplotlib.pyplot as plt
import numpy as np

data = [[15, 20, 7000], 
        [20, 25, 4000], 
        [25, 30, 3000], 
        [30, 35, 2000]]

x = np.arange(len(data))

fig, ax = plt.subplots(figsize=(10,8))
ax.bar(x, [n[0] for n in data], label='Green Energy Usage(%)')
ax.bar(x, [n[1] for n in data], bottom=[n[0] for n in data], label='Renewable Energy Usage(%)')
ax.bar(x, [n[2] for n in data], bottom=[n[0] + n[1] for n in data], label='CO2 Emission(tonnes)')

ax.set_title('Environmental Sustainability Indicators of Four Countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.legend(bbox_to_anchor=(1, 1))

for i in range(len(data)):
    ax.annotate('%s' % data[i][0], xy=(i - 0.15, data[i][0]/2), size=12)
    ax.annotate('%s' % data[i][1], xy=(i - 0.15, (data[i][0] + data[i][1])/2), size=12)
    ax.annotate('%s' % data[i][2], xy=(i - 0.15, (data[i][0] + data[i][1] + data[i][2])/2), size=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/8.png')
plt.clf()