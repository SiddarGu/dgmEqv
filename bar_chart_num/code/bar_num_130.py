
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2, 1.5], [1.2, 1], [0.8, 0.6], [0.4, 0.3]])
platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn"] 

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35
ax.bar(platforms, data[:, 0], width, label='Users (million)', bottom=0)
ax.bar(platforms, data[:, 1], width, label='Active Users (million)', bottom=data[:, 0])

for i, value in enumerate(data.flatten()):
    ax.annotate('{}'.format(value), xy=(i/2, value+0.05), rotation=90)

ax.set_title('Number of users and active users for four major social media platforms in 2021')
ax.legend(loc='upper left')
plt.xticks(platforms)
plt.tight_layout()
plt.savefig('Bar Chart/png/85.png')
plt.clf()