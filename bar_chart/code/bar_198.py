
import matplotlib.pyplot as plt
import numpy as np

Location = ['Los Angeles', 'New York', 'Chicago', 'Dallas']
price_data = [500, 450, 400, 350]
rent_data = [30, 35, 25, 20]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()

ax.bar(Location, price_data, width=0.4, label='Average House Price(K)', color='#0F6EFF')
ax.bar(Location, rent_data, width=0.4, label='Monthly Rent(K)', bottom=price_data, color='#E9F41C')

ax.set_title('Average House Prices and Monthly Rents in four US cities in 2021', fontsize=15, fontweight='bold')
ax.set_ylabel('Price and Rent (in thousands)', fontsize=15)
ax.set_xlabel('Location', fontsize=15)
ax.set_xticks(Location)
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, fontsize=15)

plt.tight_layout()
plt.savefig('bar chart/png/562.png')
plt.clf()