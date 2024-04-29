
import matplotlib.pyplot as plt
import numpy as np

product = ['Shoes','Clothes','Bags','Accessories']
online = [42, 65, 35, 21]
retail = [50, 80, 45, 30]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()

x = np.arange(len(product))
ax.bar(x-0.2, online, width=0.4, color='#00FFFF', label='Online sales')
ax.bar(x+0.2, retail, width=0.4, color='#FF6347', label='Retail sales')

ax.set_xticks(x)
ax.set_xticklabels(product, rotation=45, wrap=True)
ax.set_title('Number of online and retail sales for four products in 2021')
ax.legend(loc='best')
plt.tight_layout()

plt.savefig('bar chart/png/203.png')
plt.clf()