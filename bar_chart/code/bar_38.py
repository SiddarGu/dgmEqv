
import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 100000, 20000, 1000], 
        ['South America', 80000, 18000, 900], 
        ['Europe', 110000, 22000, 1100], 
        ['Asia', 140000, 26000, 1200]]

region, roads, railways, airports = np.array(data).T

x = np.arange(4)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

ax.bar(x - 0.2, roads, width=0.2, label='Roads (km)', color='#FFA500')
ax.bar(x, railways, width=0.2, label='Railways (km)', color='#87CEFA')
ax.bar(x + 0.2, airports, width=0.2, label='Airports', color='#90EE90')

ax.set_title('Transportation infrastructure in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region, rotation=0, ha='center', wrap=True)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/312.png')
plt.clf()