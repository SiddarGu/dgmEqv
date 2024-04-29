

import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Retail_Sales = [10,5,7,6]
E_commerce_Sales = [2,1,3,2]

fig = plt.figure(figsize=(8,4))

x = np.arange(len(Country))
width = 0.35

ax = fig.add_subplot()
ax.bar(x-width/2, Retail_Sales, width, label='Retail Sales')
ax.bar(x+width/2, E_commerce_Sales, width, label='E-commerce Sales')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.grid(linestyle=':')
ax.set_title('Retail and e-commerce sales in four countries in 2021')
ax.legend()

for i in range(len(Retail_Sales)):
    ax.annotate(Retail_Sales[i], (x[i]-width/2,Retail_Sales[i]), xytext=(0,3), textcoords='offset points')
    ax.annotate(E_commerce_Sales[i], (x[i]+width/2,E_commerce_Sales[i]), xytext=(0,3), textcoords='offset points')

plt.tight_layout()
plt.savefig('Bar Chart/png/95.png',dpi=200)

plt.clf()