
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Athletics (Hours)': [50, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Music (Hours)': [75, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'Theater (Hours)': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Gaming (Hours)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    'Movies (Hours)': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 10, 100, or 1000
if max_total_value < 10:
    max_total_value = 10
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

# Create ax object
ax = plt.subplot()

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
plt.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.5)

# Plot the data with stackplot
ax.stackplot(df['Month'], df.iloc[:, 1:].T, labels=df.columns[1:])

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Rotate x axis ticklabels
ax.set_xticklabels(df['Month'], rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title('Entertainment Habits by Month')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-103019_19.png', bbox_inches='tight')

# Clear the current image state
plt.clf()