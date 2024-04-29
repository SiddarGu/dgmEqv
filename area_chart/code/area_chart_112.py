
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa'],
        'Trucks (Units)': [5000, 4000, 6000, 3000, 2000],
        'Ships (Units)': [3000, 2500, 4000, 2000, 1000],
        'Planes (Units)': [1000, 1500, 2000, 500, 200],
        'Trains (Units)': [2000, 1000, 3000, 1000, 500],
        'Barges (Units)': [1500, 2000, 2500, 1000, 500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1:], labels=df.columns[1:], colors=['#6C9CD2', '#4A76A8', '#557799', '#D1B6E1', '#4D6F8C'], alpha=0.8)

# Set background grid lines
ax.grid(axis='y', color='#DDDDDD')

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_xticks([])
    ax.set_yticks([])

# Set y label with units from legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, [label + ' (Units)' for label in labels], loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image
fig.tight_layout()

# Add title
fig.suptitle('Distribution of Transportation Units by Region', fontsize=16)

# Save figure
fig.savefig('output/final/area_chart/png/20231228-140159_20.png', bbox_inches='tight')

# Clear current image state
plt.clf()