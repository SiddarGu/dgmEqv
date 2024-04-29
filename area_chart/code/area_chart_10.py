


# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data in dictionary format
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Electricity (kWh)': [5000, 5200, 4500, 5100, 4800],
        'Natural Gas (kWh)': [4000, 4100, 4900, 3500, 4200],
        'Water (Liters)': [6000, 5500, 3300, 3200, 3400],
        'Waste (Tons)': [300, 220, 280, 250, 270]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and set y limits and ticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df)))

# Set x and y labels
ax.set_xlabel('Month')
ax.set_ylabel('Utility Usage')

# Set grid lines
ax.grid(color='lightgrey', linestyle='dashed')

# Plot area chart
ax.stackplot(df['Month'], df['Electricity (kWh)'], df['Natural Gas (kWh)'], df['Water (Liters)'], df['Waste (Tons)'], labels=['Electricity', 'Natural Gas', 'Water', 'Waste'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Utility Usage by Month')

# Automatically resize image
fig.tight_layout()

# Save figure and clear current image state
fig.savefig('output/final/area_chart/png/20231226-103019_18.png', bbox_inches='tight')
plt.clf()