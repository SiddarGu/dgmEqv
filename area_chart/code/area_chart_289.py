
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary of data
data_dict = {'Category': ['Paintings', 'Sculptures', 'Music', 'Literature', 'Dance', 'Film', 'Photography', 'Theater', 'Fashion', 'Design', 'Architecture', 'Culinary Arts', 'History', 'Culture', 'Heritage'], 
             'Exhibitions (Events)': [20, 25, 30, 35, 40, 20, 25, 30, 35, 40, 20, 25, 30, 35, 40], 
             'Concerts (Events)': [30, 20, 40, 25, 35, 30, 20, 40, 25, 35, 30, 20, 40, 25, 35],
             'Museum Visits (Events)': [25, 30, 20, 35, 40, 25, 30, 20, 35, 40, 25, 30, 20, 35, 40],
             'Theater Performances (Events)': [35, 40, 25, 20, 30, 35, 40, 25, 20, 30, 35, 40, 25, 20, 30],
             'Festivals (Events)': [40, 35, 30, 25, 20, 40, 35, 30, 25, 20, 40, 35, 30, 25, 20]}

# Convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(16, 9))

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

# Plot the data with area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# Set labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Events')
ax.set_title('Events in Arts and Culture by Category')

# Set ticks and ticklabels
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate and set y-axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend
ax.legend(loc='upper right')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_57.png', bbox_inches='tight')

# Clear current image state
plt.clf()