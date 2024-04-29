
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data processing
data = {'Country': ['United States', 'Spain', 'France', 'China', 'Italy', 'Thailand'], 
        'Hotel Bookings (thousands)': [1500, 1200, 1000, 1800, 900, 1600], 
        'Tourism Revenue (millions)': [3000, 2500, 2000, 3500, 1800, 3000], 
        'Tourist Arrivals (thousands)': [2000, 1900, 1500, 2500, 1300, 2200], 
        'Hotel Occupancy (%)': [75, 85, 65, 80, 70, 90], 
        'Average Daily Rate ($)': [150, 170, 200, 120, 190, 100], 
        'Revenue per Available Room ($)': [112.50, 144.50, 130, 96, 133, 90]
        }

df = pd.DataFrame(data)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12,8))

# Create heatmap using seaborn
sns.heatmap(df.drop(columns=['Country']), annot=True, cmap='Blues', fmt='.2f', cbar=True, ax=ax)

# Set x and y tick labels
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', fontsize=12)
ax.set_yticklabels(df['Country'], fontsize=12)

# Set tick positions
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
ax.set_yticks(np.arange(len(df['Country'])) + 0.5)

# Set tick labels in the center of rows and columns
ax.set_xticklabels(df.columns[1:], ha='center')
ax.set_yticklabels(df['Country'], va='center')

# Set title
ax.set_title("Tourism and Hospitality Performance by Country", fontsize=16)

# Automatically resize and save the figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_8.png', bbox_inches='tight')

# Clear current image state
plt.clf()