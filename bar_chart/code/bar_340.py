
import matplotlib.pyplot as plt
import numpy as np

# Set parameters
plt.figure(figsize=(10, 7))

# Draw the graph
x = np.arange(4)
area_farmed = [100, 120, 90, 140]
yields = [400, 430, 380, 460]

plt.bar(x, area_farmed, label='Area farmed(sq.km)', color='b', width=0.4)
plt.bar(x+0.4, yields, label='Yield(tons)', color='g', width=0.4)

# Set labels, legend and title
plt.xticks(x, ['Southeast Asia', 'North America', 'South America', 'Europe'], rotation=45, ha='right', wrap=True)
plt.ylabel('Units')
plt.legend()
plt.title('Area farmed and yields of agricultural products in four regions in 2021')

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/530.png')

# Clear the figure
plt.clf()