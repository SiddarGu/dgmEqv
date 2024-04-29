
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data
data = {'Crop': ['Corn', 'Wheat', 'Rice', 'Soybean', 'Barley', 'Oats', 'Sorghum', 'Rye', 'Millet', 'Quinoa', 'Teff', 'Buckwheat', 'Amaranth'],
        'Production (lbs)': [500, 400, 300, 250, 200, 100, 150, 50, 80, 120, 70, 90, 60],
        'Consumption (lbs)': [400, 350, 200, 150, 100, 80, 100, 40, 60, 100, 50, 70, 40],
        'Export (lbs)': [300, 250, 250, 200, 150, 50, 60, 30, 40, 80, 40, 50, 30],
        'Import (lbs)': [200, 300, 150, 100, 80, 30, 40, 20, 20, 60, 30, 40, 20]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Set y limit and y ticks
ax.set_ylim(0, np.ceil(max_total_value/100)*100)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Production', 'Consumption', 'Export', 'Import'], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728'], alpha=0.7)

# Set x ticks and x tick labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0])

# Set x and y axis label
ax.set_xlabel('Crop')
ax.set_ylabel('Pounds')

# Set title
ax.set_title('Agriculture and Food Production by Crop')

# Set grid lines
ax.grid(linestyle='--', alpha=0.3)

# Set legend
ax.legend(loc='upper right')

# Automatically resize image
fig.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-131755_56.png', bbox_inches='tight')

# Clear current image state
plt.clf()