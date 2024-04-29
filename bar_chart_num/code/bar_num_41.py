
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Retail_Sales = [15,10,12,11]
E_commerce_Sales = [4.5,3.5,2.5,3.2]

x = np.arange(len(Country))
width = 0.35

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()
ax.bar(x - width/2, Retail_Sales, width, label='Retail Sales')
ax.bar(x + width/2, E_commerce_Sales, width, label='E-commerce Sales')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title('Comparison of Retail and E-commerce Sales in four countries in 2021')
ax.set_ylabel('Sales (billion)')
ax.legend()

for a,b in zip(x,Retail_Sales):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=10)
for a,b in zip(x,E_commerce_Sales):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/534.png')
plt.clf()