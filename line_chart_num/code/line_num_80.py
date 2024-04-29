
import matplotlib.pyplot as plt
import numpy as np

year = [2010,2011,2012,2013,2014,2015,2016,2017]
house_price = [200000,210000,220000,230000,240000,250000,260000,270000]
rent_price = [1500,1600,1700,1800,1900,2000,2100,2200]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.plot(year, house_price, label='House Price', color='tab:blue', linewidth=3)
ax.plot(year, rent_price, label='Rent Price', color='tab:orange', linestyle='dashed', linewidth=3)
ax.legend(loc='upper left')

ax.set_title('Average Housing Prices and Rents in the US from 2010 to 2017', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Price (USD)', fontsize=12)

plt.xticks(np.arange(min(year), max(year)+1, 1.0))

for a,b,c in zip(year, house_price, rent_price): 
    ax.annotate(f'{c}', xy=(a,b), size=12, ha='center', va='bottom')

plt.tight_layout()
plt.savefig('line chart/png/506.png')
plt.clf()