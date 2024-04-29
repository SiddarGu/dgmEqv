
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

City = ['Los Angeles','New York','Chicago','Houston']
Average_Home_Price = [1000000,1200000,900000,800000]
Houses_Sold = [50,60,45,40]

width = 0.35
p1 = ax.bar(City, Average_Home_Price, width, label='Average Home Price')
p2 = ax.bar(City, Houses_Sold, width, bottom=Average_Home_Price, label='Houses Sold')

ax.set_title('Average Home Prices and Houses Sold in four major cities in 2021')
ax.set_ylabel('Average Home Price($) & Houses Sold')
ax.set_xlabel('City')
ax.legend()
ax.grid(True, axis='y')

for i, v in enumerate(zip(Average_Home_Price, Houses_Sold)):
    ax.text(i - 0.2, (v[0] + v[1])/2 + 100000, str(v[1]), color='black', fontsize=12, ha='center', wrap=True)
    ax.text(i - 0.2, v[0]/2 - 100000, str(v[0]), color='black', fontsize=12, ha='center', wrap=True)

plt.xticks(np.arange(len(City)), City, rotation=45)
plt.tight_layout()
plt.savefig('Bar Chart/png/492.png')
plt.clf()