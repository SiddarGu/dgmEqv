
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 7))
ax = plt.subplot(111)

Region = np.array(['North America', 'Europe', 'Asia', 'South America'])
Retail_Stores = np.array([200, 150, 180, 220])
Online_Stores = np.array([400, 350, 380, 420])

x_pos = np.arange(len(Region))
width = 0.4

rects1 = ax.bar(x_pos, Retail_Stores, width, color='orange')
rects2 = ax.bar(x_pos + width, Online_Stores, width, color='blue')

ax.set_xticks(x_pos + width / 2)
ax.set_xticklabels(Region, rotation=45, ha="right", wrap=True)
ax.set_title('Number of retail stores and online stores in four regions in 2021')
ax.set_ylabel('Number of Stores')
ax.legend((rects1[0], rects2[0]), ('Retail Stores', 'Online Stores'))

plt.tight_layout()
plt.savefig('bar chart/png/32.png')
plt.clf()