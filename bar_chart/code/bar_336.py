
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
ax = plt.subplot()

data = [['North', 30, 15], ['South', 35, 18], ['East', 25, 12], ['West', 27, 14]]

regions = [item[0] for item in data]
totals = [item[1] for item in data]
grocery = [item[2] for item in data]

x_pos = np.arange(len(regions))

ax.bar(x_pos, totals, label='Total Expenditure (billion)',width=0.5, align='center')
ax.bar(x_pos, grocery, label='Grocery Expenditure (billion)', bottom=totals, width=0.5, align='center')

ax.set_xticks(x_pos)
ax.set_xticklabels(regions, rotation=45, ha='right', wrap=True)
ax.set_title('Total and Grocery Expenditure in four regions in 2021')
ax.legend(loc='upper center')

plt.tight_layout()
plt.savefig('bar chart/png/533.png')
plt.clf()