
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6)) 
ax.set_title('Average house prices and rent in four regions in 2021')

regions = ["North", "South", "East", "West"] 
house_price = [200000, 250000, 210000, 240000] 
rent = [1200, 1500, 1300, 1400]

x = np.arange(len(regions)) 
width = 0.35

rects1 = ax.bar(x - width/2, house_price, width, label='House Price') 
rects2 = ax.bar(x + width/2, rent, width, label='Rent') 

ax.set_ylabel('Price($)') 
ax.set_xticks(x) 
ax.set_xticklabels(regions)
ax.legend(loc='upper center')

fig.tight_layout()
plt.savefig('bar chart/png/101.png')
plt.show()
plt.clf()