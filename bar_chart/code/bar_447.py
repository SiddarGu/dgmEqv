
import matplotlib.pyplot as plt
import numpy as np

region=['North','South','East','West']
theaters=[5,6,7,8]
museums=[8,9,10,11]
galleries=[4,5,6,7]

fig, ax = plt.subplots(figsize=(10,5))
x = np.arange(len(region))
ax.bar(x - 0.2, theaters, width=0.2, label='Theaters')
ax.bar(x, museums, width=0.2, label='Museums')
ax.bar(x + 0.2, galleries, width=0.2, label='Galleries')
ax.set_xticks(x)
ax.set_xticklabels(region,rotation=45, wrap=True)
ax.legend(loc='upper right')
ax.set_title('Number of theaters, museums, and galleries by region in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/370.png')
plt.clf()