
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Represent data using dictionary
data_dict = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Trucks (Units)': [200, 180, 220, 210],
    'Ships (Units)': [100, 120, 90, 110],
    'Planes (Units)': [50, 45, 60, 40],
    'Trains (Units)': [150, 160, 170, 180]
}

# Use pandas to process data
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(linestyle='--', alpha=0.5)

# Set colors and transparency
colors = ['#FFB6C1', '#87CEEB', '#FFDAB9', '#90EE90']

# Plot the data with type of area chart
ax.stackplot(df['Month'], df['Trucks (Units)'], df['Ships (Units)'], df['Planes (Units)'], df['Trains (Units)'], labels=['Trucks', 'Ships', 'Planes', 'Trains'], colors=colors, alpha=0.7)

# Set legend's position
ax.legend(loc='upper left')

# Set title and axis labels
ax.set_title('Transportation and Logistics by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Units')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231226-103019_27.png', bbox_inches='tight')

# Clear current image state
plt.clf()