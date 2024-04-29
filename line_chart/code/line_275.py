
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker 
import numpy as np 

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1,1,1)

x = np.arange(6)
month = ['January', 'February', 'March', 'April', 'May', 'June']
Beverages = [1000, 1200, 900, 1100, 1200, 1000]
Sweets = [2000, 1800, 1500, 2000, 1900, 1700]
Snacks = [800, 900, 1000, 800, 1000, 1100]
Bakery = [600, 650, 700, 750, 800, 900]

ax.plot(x, Beverages, label='Beverages', marker ='o', color = 'b')
ax.plot(x, Sweets, label = 'Sweets', marker = 'o', color = 'g')
ax.plot(x, Snacks, label = 'Snacks', marker = 'o', color = 'r')
ax.plot(x, Bakery, label = 'Bakery', marker = 'o', color = 'm')

ax.set_xticks(x)
ax.set_xticklabels(month, rotation=45, ha="right")

plt.title('Food and Beverage Industry Sales in the First Half of 2021')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(loc='best')
plt.grid(color='grey', linestyle='--', linewidth=1, alpha=0.3)
plt.tight_layout()
plt.savefig('line chart/png/75.png')
plt.clf()