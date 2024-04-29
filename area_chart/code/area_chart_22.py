
# Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Harvested Area (acres)': [1000, 900, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
        'Crop Yield (bushels)': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
        'Livestock Inventory (head)': [200, 220, 250, 260, 280, 300, 320, 350, 380, 400, 410, 430]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value for y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Plot the data with area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Month'])
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.grid(color='grey', linestyle='dashed', alpha=0.5)
ax.legend(loc='upper left')
ax.set_title('Agriculture and Food Production Trends')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_6.png', bbox_inches='tight')

# Clear current image state
plt.clf()