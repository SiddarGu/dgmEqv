
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 500, 1000, 5000],
        [2002, 550, 900, 4000],
        [2003, 600, 1100, 6000],
        [2004, 650, 1300, 7000]]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

x = np.array([row[0] for row in data])
ax.plot(x, [row[1] for row in data], label='Quantity of Beverage (million L)', marker='o')
ax.plot(x, [row[2] for row in data], label='Quantity of Juice (million L)', marker='o')
ax.plot(x, [row[3] for row in data], label='Quantity of Food (million KG)', marker='o')

ax.grid(ls='-.')
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.03))
ax.set_title('Quantities of food and beverages in the Food and Beverage Industry from 2001 to 2004', fontsize=15, wrap=True)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Quantity (million)', fontsize=12)
ax.set_xticks(x)

fig.tight_layout()
plt.savefig('line chart/png/152.png')
plt.clf()