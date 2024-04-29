
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig= plt.figure(figsize=(10, 6))
ax= fig.add_subplot()

# Get data
data = [['USA', 500, 450],
        ['UK', 400, 430],
        ['Germany', 350, 400],
        ['France', 300, 370]]
countries,manufactured_goods,exports = zip(*data)

# Set bar width
width = 0.35

# Plot bars
ax.bar(countries, manufactured_goods, width, label='Manufactured Goods')
ax.bar(np.arange(len(countries))+width, exports, width, label='Exports')

# Add xticks on the middle of the group bars
ax.set_xticks(np.arange(len(countries)) + width / 2)
ax.set_xticklabels(countries, fontsize=10, rotation=0, wrap=True)

# Set title
plt.title('Total manufactured goods and exports in four countries in 2021', fontsize=15)

# Create legend
ax.legend(loc='best')

# Set grid
ax.grid(axis='y')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/249.png')

# Clear current image state
plt.clf()