

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

month = ['January', 'February', 'March', 'April']
retail_sales = np.array([50,60,65,70])
e_commerce_sales = np.array([30,40,48,50])

p1 = ax.bar(month, retail_sales, width=0.8, label='Retail Sales')
p2 = ax.bar(month, e_commerce_sales, width=0.8, bottom=retail_sales, label='E-commerce Sales')

ax.set_title('Retail and E-commerce Sales from January to April 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Sales (million)')
ax.legend(loc='upper left')

plt.xticks(month) 

for p in p1+p2:
    h = p.get_height()
    ax.annotate("{:.0f}".format(h), xy=(p.get_x()+p.get_width()/2., h),
                 ha='center', va='center', xytext=(0, 10), 
                 textcoords='offset points', rotation=90, fontsize=11)

plt.tight_layout()
plt.savefig('Bar Chart/png/612.png')
plt.clf()