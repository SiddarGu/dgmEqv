

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
ax = plt.subplot()

products = ('Clothes', 'Electronics', 'Shoes', 'Accessories')
online_sales = (200, 150, 100, 80)
physical_store_sales = (300, 240, 170, 120)

x = range(len(products))

ax.bar(x, online_sales, width=0.3, label="Online Sales (million)", edgecolor='black',color='#0099cc')
ax.bar([i+0.3 for i in x], physical_store_sales, width=0.3, label="Physical Store Sales (million)", edgecolor='black', color='#ff9900')

ax.set_xticks([i+0.3/2 for i in x])
ax.set_xticklabels(products,rotation=20)
ax.set_title("Sales comparison between online and physical stores in 2021")
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/11.png')
plt.cla()