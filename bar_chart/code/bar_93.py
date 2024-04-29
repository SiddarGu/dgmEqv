
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000, 4000, 6000], [900, 3000, 5000], [800, 3500, 4500], [700, 4000, 5500]])

fig = plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(np.arange(3), data[0], width=0.25, label='USA')
ax.bar(np.arange(3)+0.25, data[1], width=0.25, label='UK')
ax.bar(np.arange(3)+0.5, data[2], width=0.25, label='Germany')
ax.bar(np.arange(3)+0.75, data[3], width=0.25, label='France')
ax.set_xticks(np.arange(3)+0.375)
ax.set_xticklabels(['Vegetables\n(tons)', 'Fruits\n(tons)', 'Grains\n(tons)'], rotation=0, wrap=True)
ax.set_ylabel('Ton')
ax.set_title('Food production in four countries in 2021')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/88.png')
plt.clf()