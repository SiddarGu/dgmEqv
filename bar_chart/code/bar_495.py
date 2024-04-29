
import matplotlib.pyplot as plt
import numpy as np

Region = ['North','South','East','West']
Average_House_Price = [500,600,550,650]
Average_Rent = [750,900,800,850]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

ax.bar(Region, Average_House_Price, label="Average House Price", width=0.3, bottom=0)
ax.bar(Region, Average_Rent, label="Average Rent", width=0.3, bottom=Average_House_Price)

plt.title('Average House Price and Rent in four regions in 2021', fontsize=20)

ax.set_xticks(np.arange(len(Region)))
ax.set_xticklabels(Region, fontsize=15, rotation=45, ha='right')
ax.set_xlabel('Regions', fontsize=15)
ax.set_ylabel('Money($)', fontsize=15)

plt.legend(fontsize=15, bbox_to_anchor=(1, 0.9), loc='upper left')
plt.tight_layout()
plt.savefig('bar_495.png')
plt.clf()