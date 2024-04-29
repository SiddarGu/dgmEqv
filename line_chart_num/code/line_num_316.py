
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[3000, 450, 4200], [3500, 500, 4500], [3300, 600, 4800], [4000, 550, 5100]])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

plt.figure(figsize=(16, 8))
ax = plt.subplot()
ax.set_title('Quarterly performance of an online retail store')
ax.plot(quarters, data[:, 0], color='b', linewidth=2, label='Revenue(million dollars)')
ax.plot(quarters, data[:, 1], color='g', linewidth=2, label='Profit(million dollars)')
ax.plot(quarters, data[:, 2], color='r', linewidth=2, label='Number of Transactions')
ax.set_xticks(quarters)
ax.legend(loc='upper left')

for i, label in enumerate(data[:, 0]):
    ax.annotate(label, (quarters[i], data[i, 0]), rotation=45, ha='right', va='center', size=12)
for i, label in enumerate(data[:, 1]):
    ax.annotate(label, (quarters[i], data[i, 1]), rotation=45, ha='right', va='center', size=12)
for i, label in enumerate(data[:, 2]):
    ax.annotate(label, (quarters[i], data[i, 2]), rotation=45, ha='right', va='center', size=12)

plt.tight_layout()
plt.savefig('line chart/png/92.png')
plt.clf()