
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

region = ['North America','Europe','Africa','Asia']
hydroelectric = [1000,1100,1200,1300]
solar = [2000,2200,2400,2600]
wind = [3000,3300,3600,3900]

# Create figure
fig = plt.figure(figsize=(10,5))

# Create axes
ax = fig.add_subplot(111)

# Create bar chart
x = np.arange(len(region))
ax.bar(x - 0.2, hydroelectric, width=0.2, label='Hydroelectric', color='#8dafbe')
ax.bar(x, solar, width=0.2, label='Solar', color='#ffc000')
ax.bar(x + 0.2, wind, width=0.2, label='Wind', color='#007f5f')

# Set the x-axis
ax.set_xticks(x)
ax.set_xticklabels(region)

# Set the y-axis
ax.yaxis.set_major_formatter(FuncFormatter('{:.0f}'.format))

# Set title
plt.title('Energy Production from Hydroelectric, Solar and Wind in four regions in 2021')

# Set legend
plt.legend(loc='best')

# Add label
for i in range(len(hydroelectric)):
    ax.annotate(hydroelectric[i]+solar[i]+wind[i], xy=(i, hydroelectric[i]+solar[i]+wind[i]), xytext=(0, 3), 
            textcoords="offset points", ha='center', va='bottom')

# Adjust the size of the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/572.png')

# Clear the figure
plt.clf()