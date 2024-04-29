
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'2021': ['Q1', 'Q2', 'Q3', 'Q4'], 'Total Revenue (Millions)': [500, 550, 600, 650], 'Gross Profit (Millions)': [300, 320, 350, 370], 'Operating Income (Millions)': [150, 160, 180, 190], 'Net Income (Millions)': [100, 110, 120, 130]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax = plt.gca()
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)

max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100

yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set background grid lines
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5, alpha=0.5)

# Plot the data with area chart
plt.stackplot(df['2021'], df['Total Revenue (Millions)'], df['Gross Profit (Millions)'], df['Operating Income (Millions)'], df['Net Income (Millions)'], labels=['Total Revenue (Millions)', 'Gross Profit (Millions)', 'Operating Income (Millions)', 'Net Income (Millions)'], colors=['#4e79a7', '#f28e2c', '#e15759', '#76b7b2'], alpha=0.8)

# Set legend and adjust its position
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image
plt.tight_layout()

# Add title and labels
plt.title('Financial Performance by Quarter in 2021')
plt.xlabel('Quarter')
plt.ylabel('Amount (Millions)')

# Save the chart
plt.savefig('output/final/area_chart/png/20231228-131755_35.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()