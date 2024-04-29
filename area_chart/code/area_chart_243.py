
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary with data
data = {'Category': ['Archaeology', 'Psychology', 'Sociology', 'History', 'Anthropology'],
        '2016': [250, 300, 200, 150, 100],
        '2017': [270, 280, 220, 160, 120],
        '2018': [300, 250, 230, 180, 140],
        '2019': [280, 260, 240, 200, 160],
        '2020': [320, 240, 250, 220, 180]}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12,8))

# Plot the data with an area chart
ax = plt.subplot(1, 1, 1)
ax.stackplot(df['Category'], df['2016'], df['2017'], df['2018'], df['2019'], df['2020'], labels=['2016', '2017', '2018', '2019', '2020'], alpha=0.7)

# Set x and y tick labels
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y')

# Set legend
ax.legend(loc='upper left')

# Set title
plt.title('Number of Publications in Social Sciences and Humanities from 2016 to 2020')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_9.png', bbox_inches='tight')

# Clear current image state
plt.clf()