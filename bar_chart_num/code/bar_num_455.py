
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
y = [2.6, 0.7, 1.2, 0.4]

fig, ax = plt.subplots(figsize=(10,6))
plt.bar(x, y, color='#0059b3', width=0.5)
ax.set_xticks(x)
ax.set_xticklabels(['Facebook','Twitter','Instagram','Snapchat'])
ax.set_title('Number of Monthly Users on Popular Social Media Platforms in 2021')
ax.set_ylabel('Monthly Users (million)')
for i, v in enumerate(y):
    ax.text(i, v/2, str(v), color='white', fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/474.png')
plt.clf()