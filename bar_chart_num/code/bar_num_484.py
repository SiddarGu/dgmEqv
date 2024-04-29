
import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 800, 500, 300],
        ['South America', 700, 450, 250],
        ['Europe', 600, 400, 200],
        ['Asia', 500, 350, 150]]

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Set Y-axis
Y = np.arange(len(data))

# Set variable names
variables = [v[0] for v in data]

# Set data
Crops = [v[1] for v in data]
Meats = [v[2] for v in data]
Dairy = [v[3] for v in data]

# Set bar width
width = 0.2

# Plot bar chart
ax.barh(Y-width, Crops, width, label='Crops', color='#f5dbd0')
ax.barh(Y, Meats, width, label='Meats', color='#6c7c46')
ax.barh(Y+width, Dairy, width, label='Dairy', color='#d1b7d8')

# Set figure title
ax.set_title('Food Production in four regions in 2021')

# Set Y-axis
ax.set_yticks(Y)
ax.set_yticklabels(variables)

# Turn on the grid
ax.grid(axis='x')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

# Display value for each bar
for v1, v2, v3 in zip(Y-width, Y, Y+width):
    ax.text(0, v1, str(Crops[int(v1)]), ha='center', va='center')
    ax.text(0, v2, str(Meats[int(v2)]), ha='center', va='center')
    ax.text(0, v3, str(Dairy[int(v3)]), ha='center', va='center')

# Auto adjust subplot parameters to give specified padding
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/299.png', dpi=300) 

# Clear state
plt.clf()