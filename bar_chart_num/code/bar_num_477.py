
import matplotlib.pyplot as plt
import numpy as np

Country=['USA','UK','Germany','France']
Beverage_Sales=[200,230,180,210]
Food_Sales=[400,450,420,480]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.bar(Country, Beverage_Sales, bottom=Food_Sales, label='Beverage Sales')
ax.bar(Country, Food_Sales, label='Food Sales')

ax.set_title('Food and Beverage Sales in four countries in 2021')
ax.legend(loc='upper right')

for i, v in enumerate(Beverage_Sales):
    ax.text(i, v + 3, str(v), color='black', fontweight='bold')
for i, v in enumerate(Food_Sales):
    ax.text(i, v + 3, str(v), color='black', fontweight='bold')

plt.xticks(np.arange(len(Country)), Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/460.png')
plt.clf()