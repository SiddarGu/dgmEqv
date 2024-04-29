
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary with the given data
data = {'Country': ['Thailand', 'France', 'United States', 'Spain', 'China'],
        'Tourists (Millions)': [30, 25, 20, 15, 10],
        'Revenue (Billions)': [40, 35, 30, 25, 20],
        'Average Stay (Days)': [5, 6, 7, 8, 4],
        'Hotel Occupancy (%)': [75, 80, 85, 70, 90]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data using stackplot
ax.stackplot(df['Country'], df['Tourists (Millions)'], df['Revenue (Billions)'], df['Average Stay (Days)'], df['Hotel Occupancy (%)'],
             labels=['Tourists (Millions)', 'Revenue (Billions)', 'Average Stay (Days)', 'Hotel Occupancy (%)'], colors=['#f9a825', '#e53935', '#7e57c2', '#00acc1'], alpha=0.7)

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Country'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y', color='#9e9e9e', linestyle='--', alpha=0.2)

# Set legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and labels
ax.set_title('Tourism and Hospitality Statistics by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Value')

# Automatically resize image and save it
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-155112_53.png', bbox_inches='tight')

# Clear current image state
plt.close('all')