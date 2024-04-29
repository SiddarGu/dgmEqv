
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
d = {'Category': ['Physics (Researchers)', 'Chemistry (Researchers)', 'Biology (Researchers)', 'Computer Science (Researchers)', 'Engineering (Researchers)'],
     'USA': [200, 180, 150, 130, 100],
     'China': [150, 200, 180, 100, 130],
     'Germany': [100, 120, 150, 200, 180],
     'Japan': [180, 150, 100, 130, 200],
     'South Korea': [150, 200, 180, 100, 130],
     'Russia': [100, 120, 150, 200, 180],
     'India': [180, 150, 100, 130, 200],
     'France': [150, 200, 180, 100, 130],
     'Canada': [100, 120, 150, 200, 180],
     'United Kingdom': [180, 150, 100, 130, 200]}

# Convert data to dataframe
df = pd.DataFrame(data=d)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data as an area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.iloc[:, 0],
             df.iloc[:, 1],
             df.iloc[:, 2],
             df.iloc[:, 3],
             df.iloc[:, 4],
             df.iloc[:, 5],
             labels=['Physics', 'Chemistry', 'Biology', 'Computer Science', 'Engineering'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set y axis ticks
# max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# max_total_value = np.ceil(max_total_value / 10) * 10
# ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set y axis label to include legend and unit
ax.set_ylabel('Number of Researchers \n(in thousands)', rotation=0, ha='right')
ax.yaxis.set_label_coords(-0.08, 0.5)

# Set grid lines
ax.grid(True, alpha=0.5)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 0.8))

# Set title and resize image
fig.suptitle('Distribution of Researchers in Science and Engineering by Country')
fig.tight_layout()

# Save image
fig.savefig('output/final/area_chart/png/20231228-140159_65.png', bbox_inches='tight')

# Clear current image state
plt.clf()