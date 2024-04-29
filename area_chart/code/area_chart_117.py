
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Category': ['Athletics (Events)', 'Gaming (Events)', 'Live Music (Events)', 'Film (Events)', 'Comedy (Events)'],
        '2020': [150, 180, 200, 170, 120],
        '2021': [180, 200, 220, 190, 150],
        '2022': [200, 220, 240, 200, 180],
        '2023': [220, 240, 260, 210, 210],
        '2024': [240, 260, 280, 230, 240],
        '2025': [260, 280, 300, 250, 270]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data with the type of area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.iloc[:, 1:].columns)

# Set the x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.yticks(rotation=0, ha='right', rotation_mode='anchor', wrap=True)
else:
    ax.set_xlim(0, len(df.index) - 1)
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    plt.yticks(rotation=0, ha='right', rotation_mode='anchor')

# Set the colors and transparency
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for idx, item in enumerate(ax.collections):
    item.set_color(colors[idx])
ax.collections[0].set_alpha(0.6)
ax.collections[1].set_alpha(0.6)
ax.collections[2].set_alpha(0.6)
ax.collections[3].set_alpha(0.6)
ax.collections[4].set_alpha(0.6)

# Set the background grid lines
ax.grid(axis='y', alpha=0.5)

# Set the legend's position and labels
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), title='Year')

# Set the title of the figure
plt.title('Event Trends in the Sports and Entertainment Industry')

# Automatically resize the image before savefig()
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-140159_28.png', bbox_inches='tight')

# Clear the current image state
plt.clf()