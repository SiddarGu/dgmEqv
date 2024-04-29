
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[450, 300, 850],
                 [510, 350, 950],
                 [400, 400, 900],
                 [430, 310, 820]])
region = np.array(['North America', 'Europe', 'Asia', 'Africa'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

width = 0.2
x = np.arange(4)
ax.bar(x, data[:, 0], label='Air Travel', width=width)
ax.bar(x + width, data[:, 1], label='Rail Travel', width=width)
ax.bar(x + 2 * width, data[:, 2], label='Road Travel', width=width)

ax.set_title('Mode of transportation used in four regions in 2021')
ax.set_xticks(x + width)
ax.set_xticklabels(region, rotation=45, ha='right', wrap=True)

ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/24.png')
plt.clf()