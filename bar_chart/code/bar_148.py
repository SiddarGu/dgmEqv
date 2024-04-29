
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,6))
ax = plt.subplot()
x = np.arange(4)
ax.bar(x, [150, 140, 130, 120], width = 0.25, label = 'Hotels', color = 'b')
ax.bar(x + 0.25, [200, 180, 170, 160], width = 0.25, label = 'Restaurants', color = 'g')
ax.bar(x + 0.5, [250, 300, 280, 270], width = 0.25, label = 'Tourists', color = 'r')

ax.set_xticks(x + 0.25/2)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], rotation=45, wrap=True)
ax.legend(loc='upper right')
ax.set_title('Number of hotels, restaurants, and tourists in four countries in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/480.png')
plt.clf()