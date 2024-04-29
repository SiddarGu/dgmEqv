
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Category': ['Chemicals', 'Plastics', 'Metals', 'Textiles', 'Electronics', 'Machinery', 'Food & Beverage', 'Pharmaceuticals', 'Paper & Packaging', 'Automotive'],
        'Production Output': [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],
        'Raw Materials Used': [800, 750, 700, 600, 550, 500, 450, 400, 350, 300],
        'Equipment': [600, 550, 500, 450, 400, 350, 300, 250, 200, 150]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and tick labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()) + 100)

# Set y ticks with random choice of length
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Units')

# Set title
ax.set_title('Manufacturing and Production Output and Resources')

# Plot stacked area chart
ax.stackplot(df['Category'], df['Production Output'], df['Raw Materials Used'], df['Equipment'], labels=['Production Output', 'Raw Materials Used', 'Equipment'], colors=['#4287f5', '#42f5c7', '#f54242'], alpha=0.8)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set legend position and labels
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), labels=['Production Output', 'Raw Materials Used', 'Equipment'])

# Set background grid lines
ax.grid(color='#d9d9d9', linestyle='dashed', linewidth=1)

# Automatically resize image before saving
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/area_chart/png/20231228-155112_38.png', bbox_inches='tight')

# Clear current image state
plt.clf()