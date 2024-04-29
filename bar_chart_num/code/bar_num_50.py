
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[500, 450, 400], [550, 500, 500], [500, 400, 450], [550, 450, 480]])
labels = ['Vegetables(tons)', 'Fruits(tons)', 'Grain(tons)']
regions = ['North', 'South', 'East', 'West']

plt.figure(figsize=(9, 7))
ax = plt.subplot()

x = np.arange(len(regions))
bottom = np.zeros(len(regions))

for i in range(data.shape[1]):
    ax.bar(x, data[:, i], bottom=bottom, label=labels[i])
    bottom += data[:, i]

plt.title('Food production in four regions in 2021', fontsize=14)
plt.xticks(x, regions, fontsize=12)
plt.xlabel('Regions', fontsize=12)
plt.ylabel('Production(tons)', fontsize=12)
ax.legend(fontsize=12)

for i, v in enumerate(data.flatten()):
    ax.text(i // 3, bottom[i // 3] - (data[i // 3, i % 3] / 2), str(v), fontsize=10,
            color='white', ha='center', va='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/479.png')
plt.clf()