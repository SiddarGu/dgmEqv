
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()

regions = ['East Coast', 'West Coast', 'Midwest', 'South']
prices = [400, 500, 350, 450]
units = [1000, 1200, 900, 1100]

width = 0.35
ax.bar(regions, prices, width, label='Price/sqft')
ax.bar(regions, units, width, bottom=prices, label='Units Sold')

ax.set_title('Average real estate prices and units sold across four regions in 2021')
ax.set_ylabel('Price/sqft & Units Sold')

ax.legend(loc='upper left')
ax.set_xticklabels(regions, rotation=45, ha='right', wrap=True)

plt.tight_layout()
plt.savefig('bar chart/png/506.png')
plt.clf()