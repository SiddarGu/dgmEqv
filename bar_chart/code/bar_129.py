
import matplotlib.pyplot as plt
import numpy as np

# Set up data
region = ["North America","South America","Europe","Asia"]
vegetables = [8000,10000,9000,11000]
fruits = [6000,7000,8000,9000]
grains = [20000,18000,17000,16000]

# Set figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Plot data
ax.bar(region, vegetables, width=0.2, label="Vegetables")
ax.bar(region, fruits, bottom=vegetables, width=0.2, label="Fruits")
ax.bar(region, grains, bottom=np.array(vegetables)+np.array(fruits), width=0.2, label="Grains")

# Set labels
ax.set_title('Food Production Output in Tonnes from Four Regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Output (Tonnes)')
ax.set_xticklabels(region, rotation=45, ha="right")
plt.legend(loc="upper left")

# Plot grid
ax.grid(axis='y', linestyle='-.')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/163.png', bbox_inches='tight')

# Clear figure
plt.clf()