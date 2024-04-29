
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000, 1500], [1200, 1600], [1300, 1700], [1400, 1800]])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(quarters, data[:, 0], label='Online Retailers', bottom=data[:, 1], color='#0066CC')
ax.bar(quarters, data[:, 1], label='Brick-and-Mortar Shops', color='#FF9900')

for i, (p1, p2) in enumerate(zip(data[:, 0], data[:, 1])):
    ax.annotate('{}\n{}'.format(p1, p2), xy=(i, p1 + p2), xytext=(0, 3),
                textcoords='offset points', ha='center', va='bottom')

plt.title('Comparison of Online and Brick-and-Mortar Retailers in 2021')
plt.xticks(quarters)
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/459.png')
plt.clf()