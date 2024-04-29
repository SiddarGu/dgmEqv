
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

regions = ['North America', 'South America', 'Europe', 'Asia']
price = [450000, 380000, 550000, 500000]
rent = [2500, 1800, 3000, 2300]

ax.bar(regions, price, width=0.4, bottom=rent, label='Price')
ax.bar(regions, rent, width=0.4, label='Rent')

ax.set_title('Average Home Price and Rent in Four Regions in 2021')
ax.set_xticks(regions)

for i in range(len(regions)):
    ax.annotate(f"{price[i]}", xy=(i-0.2, price[i]+rent[i]/2))
    ax.annotate(f"{rent[i]}", xy=(i+0.2, rent[i]/2))
    
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

plt.tight_layout()
plt.savefig('Bar Chart/png/186.png')
plt.cla()