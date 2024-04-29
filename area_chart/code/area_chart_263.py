
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Category': ['Music', 'Visual Arts', 'Theater', 'Dance', 'Literature', 'Film'],
        'Artists': [100, 150, 100, 75, 50, 25],
        'Performers': [150, 100, 200, 150, 75, 50],
        'Museums': [50, 100, 50, 25, 25, 100],
        'Galleries': [75, 50, 100, 50, 25, 75],
        'Venues': [200, 200, 150, 100, 50, 100]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
plt.grid(color='gray', linestyle='dotted')

# Plot area chart
ax.stackplot(df['Category'], df['Artists'], df['Performers'], df['Museums'], df['Galleries'], df['Venues'], labels=['Artists', 'Performers', 'Museums', 'Galleries', 'Venues'], colors=['#FFA07A', '#ADD8E6', '#90EE90', '#F0E68C', '#87CEEB'])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Count')

# Set title
ax.set_title('Arts and Culture Industry Distribution')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_22.png', bbox_inches='tight')

# Clear current image state
plt.clf()