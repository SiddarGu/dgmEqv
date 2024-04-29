

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary with data
data = {
    'Category': ['Residential', 'Commercial', 'Industrial'],
    'Coal (Energy)': [15, 30, 50],
    'Natural Gas (Energy)': [50, 70, 80],
    'Nuclear (Energy)': [0, 5, 10],
    'Hydro (Energy)': [10, 15, 20],
    'Solar (Energy)': [30, 50, 70],
    'Wind (Energy)': [40, 60, 80]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Define figure size and create axes
fig, ax = plt.subplots(figsize=(10,6))

# Set x and y axis ticks
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Create area chart
ax.stackplot(df['Category'], df['Coal (Energy)'], df['Natural Gas (Energy)'], df['Nuclear (Energy)'], df['Hydro (Energy)'], df['Solar (Energy)'], df['Wind (Energy)'], labels=['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind'])

# Adjust legend position and add labels
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_ylabel('Energy (TWh)')
ax.set_xlabel('Sector')

# Set grid lines
ax.grid(color='lightgrey', linestyle='--')

# Set title
ax.set_title('Energy Usage by Sector')

# Rotate x ticks and set rotation mode
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-131755_58.png', bbox_inches='tight')

# Clear current image state
plt.clf()