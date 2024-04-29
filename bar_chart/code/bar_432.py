
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

data = [['Los Angeles', 750, 450_000],
        ['New York', 650, 650_000],
        ['Chicago', 600, 400_000],
        ['Houston', 950, 350_000]]

cities, homes, prices = [row[0] for row in data], [row[1] for row in data], [row[2]/1000 for row in data]

x_pos = np.arange(len(cities))

bar1 = ax.bar(x_pos, homes, color='#004488', width=0.4, label='Homes Sold')
bar2 = ax.bar(x_pos, prices, color='#EE7733', width=0.4, label='Average Price', bottom=homes)

ax.set_xticks(x_pos)
ax.set_xticklabels(cities, rotation=45, ha='right', wrap=True)
ax.set_ylabel('Number of Homes and Average Price ($1000)')
ax.set_title('Number of homes sold and average price in four cities in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/535.png')
plt.clf()