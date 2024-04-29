


# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary of data
data = {'Type': ['Civil Cases', 'Criminal Cases', 'Contract Disputes', 'Intellectual Property Cases', 'Family Cases'],
        '2019': [150, 200, 180, 100, 120],
        '2020': [140, 220, 160, 110, 130],
        '2021': [170, 240, 200, 120, 150],
        '2022': [160, 230, 190, 130, 140],
        '2023': [180, 250, 210, 140, 160]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data as stacked area chart
ax.stackplot(df['Type'], df['2019'], df['2020'], df['2021'], df['2022'], df['2023'], labels=['2019', '2020', '2021', '2022', '2023'])

# Set x and y axis labels
ax.set_xlabel('Type')
ax.set_ylabel('Number of Cases')

# Set title
ax.set_title('Case Distribution by Type from 2019 to 2023')

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(linestyle='dotted')

# Rotate x-axis labels and set rotation_mode and ha parameters
plt.setp(ax.get_xticklabels(), rotation=45, rotation_mode='anchor', ha='right')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_64.png', bbox_inches='tight')

# Clear current image state
plt.clf()