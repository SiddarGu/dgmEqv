
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2200, 1200], [1800, 1000], [1700, 800], [1600, 900]])
country = np.array(['USA', 'UK', 'Germany', 'France'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()  
ax.bar(country, data[:, 0], label='Cases', color='#FFA500')
ax.bar(country, data[:, 1], bottom=data[:, 0], label='Legal Personnel', color='#FFD700')
ax.set_title('Number of cases and legal personnel in four countries in 2021')
ax.set_xticklabels(country, rotation=45, ha="right", rotation_mode="anchor")
ax.legend(loc=2)
plt.tight_layout()
plt.savefig("bar chart/png/108.png")
plt.clf()