
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Represent data using a dictionary
data = {'Category': ['Manufacturing', 'Agriculture', 'Transportation', 'Energy', 'Construction'],
        'Carbon Emissions (Metric Tons)': [5000, 4000, 6000, 8000, 3000],
        'Renewable Energy Usage (Metric Tons)': [2000, 3000, 1000, 5000, 1000],
        'Waste Reduction (Metric Tons)': [1000, 2000, 1500, 4000, 800],
        'Water Conservation (Metric Tons)': [3000, 4000, 2000, 5000, 1500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize parameter
fig = plt.figure(figsize=(10,8))

# Set max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max total value up to nearest multiple of 10, 100 or 1000
if max_total_value < 10:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set yticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Plot the data with the type of area chart
ax = plt.axes()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], 
             labels=['Carbon Emissions', 'Renewable Energy Usage', 'Waste Reduction', 'Water Conservation'],
             colors=['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728'],
             alpha=0.8)

# Set background grid lines
ax.grid(color='gray', linestyle='dashed', alpha=0.5)

# Set x and y axis ticks and ticklabels
if np.random.uniform() < 0.7:
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.yticks(rotation=0, ha='right', rotation_mode='anchor')
else:
    plt.xticks(rotation=45, wrap=True, ha='right', rotation_mode='anchor')
    plt.yticks(rotation=0, wrap=True, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(yticks)

# Set legend and legend position
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left', bbox_to_anchor=(1, 1))

# Set title
plt.title('Environmental Impact by Industry Category')

# Automatically resize image
plt.tight_layout()

# Save the chart as a png image
plt.savefig('output/final/area_chart/png/20231226-130527_16.png', bbox_inches='tight')

# Clear the current image state
plt.clf()