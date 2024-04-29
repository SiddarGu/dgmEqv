


# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as dictionary
data = {'Year': [2016, 2017, 2018, 2019, 2020], 'Clean Air (Annual Average)': [80, 85, 90, 95, 100], 'Clean Water (Annual Average)': [70, 75, 80, 85, 90], 'Renewable Energy (Annual Average)': [25, 30, 35, 40, 45], 'Waste Management (Annual Average)': [40, 45, 50, 55, 60], 'Green Spaces (Annual Average)': [50, 55, 60, 65, 70]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].transpose(), labels=df.iloc[:, 1:].columns, colors=['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'], alpha=0.6)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    max_value = np.ceil(max_total_value)
elif max_total_value < 100:
    max_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_value = np.ceil(max_total_value / 100) * 100
else:
    max_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_value)

# Set y ticks and ticklabels
yticks = np.linspace(0, max_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, wrap=True)

# Set background grid lines
ax.grid(axis='y', alpha=0.3)

# Set legend and position
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left')

# Set title
ax.set_title('Environmental Progress in the Last 5 Years')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_68.png', bbox_inches='tight')

# Clear current state
plt.clf()