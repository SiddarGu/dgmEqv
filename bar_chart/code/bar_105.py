
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot(111)

city = ['New York', 'Los Angeles', 'Chicago', 'Miami']
price = [400000, 450000, 350000, 470000]
sold = [100, 150, 200, 90]

ax.bar(city, price, width=0.4, label='Average Home Price', color='blue')
ax.bar(city, sold, width=0.4, bottom=price, label='Homes Sold', color='orange')

ax.set_title('Average Home Prices and Number of Homes Sold in Four Major US Cities in 2021')
ax.set_ylabel('Price/Number')
ax.set_xlabel('City')
ax.set_xticks(np.arange(4))
ax.set_xticklabels(city, rotation = 20, wrap = True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/333.png')
plt.cla()