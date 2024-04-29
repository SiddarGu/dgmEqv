
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set data
data = {'Residential Type': ['Single-family Homes (Sales)', 'Condominiums (Sales)', 'Townhouses (Sales)'],
        '1st Quarter': [500, 400, 300],
        '2nd Quarter': [550, 450, 350],
        '3rd Quarter': [600, 500, 400],
        '4th Quarter': [650, 550, 450]}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set colors and transparency
colors = ['#ffcc99', '#99ff99', '#99ccff']
alpha = 0.6

# Set background grid lines
ax.grid(color='#cccccc', linestyle='-', linewidth=0.5)

# Set x-axis and y-axis ticks and ticklabels
if np.random.choice(2):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice(2):
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice(2):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value/100)*100
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Plot the data as an area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], colors=colors, alpha=alpha)

# Set legend
ax.legend(loc='upper right')

# Set title
ax.set_title('Quarterly Residential Sales by Type')

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('output/final/area_chart/png/20231228-145339_44.png', bbox_inches='tight')

# Clear the current image state
plt.clf()