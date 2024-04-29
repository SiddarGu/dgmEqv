


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set data as a dictionary
data = {
    'Category': ['Domestic', 'International', 'Local', 'Regional', 'National', 'Global', 'Continental', 'Statewide', 'Cross-border'],
    'Shipping (Tons)': [5000, 7000, 4500, 6000, 8000, 10000, 12000, 5000, 9000],
    'Trucking (Tons)': [3000, 5000, 2000, 4000, 6000, 8000, 10000, 4000, 6000],
    'Air Freight (Tons)': [2000, 3000, 1500, 2500, 4000, 5000, 8000, 3000, 4000],
    'Rail (Tons)': [4000, 1000, 3000, 2000, 3000, 2000, 5000, 2000, 3000],
    'Warehousing (Tons)': [1000, 1500, 1000, 500, 2000, 3000, 4000, 1000, 1500]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and round up to nearest multiple of 1000
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000

# Set y limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Plot the data as an area chart
ax.stackplot(df['Category'], df['Shipping (Tons)'], df['Trucking (Tons)'], df['Air Freight (Tons)'], df['Rail (Tons)'], df['Warehousing (Tons)'], labels=['Shipping', 'Trucking', 'Air Freight', 'Rail', 'Warehousing'], colors=['#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#264653'], alpha=0.8)

# Set legend and its position
leg = ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

# Set x and y ticks and tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
plt.setp(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# Add title and labels
ax.set_title('Freight Volume Across Different Modes of Transportation')
ax.set_xlabel('Category')
ax.set_ylabel('Tons')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-140159_61.png', bbox_inches='tight')

# Clear current image state
plt.clf()