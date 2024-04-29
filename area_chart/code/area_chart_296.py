
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dictionary with data
data = {'Year': [2017, 2018, 2019, 2020, 2021], 'Production Volume (Units)': [500, 600, 700, 800, 900], 'Revenue ($)': [100000, 120000, 140000, 160000, 180000], 'Expenses ($)': [70000, 80000, 90000, 100000, 110000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig = plt.figure(figsize=(10, 6))

# Set the axes
ax = fig.add_subplot(111)

# Plot the area chart
ax.stackplot(df['Year'], df['Production Volume (Units)'], df['Revenue ($)'], df['Expenses ($)'], labels=['Production Volume (Units)', 'Revenue ($)', 'Expenses ($)'], colors=['lightblue', 'lightgreen', 'lightcoral'], alpha=0.5)

# Set the x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index), 1))
    ax.set_xticklabels(df['Year'])
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    ax.set_ylim(0, np.ceil(max_total_value / 100) * 100) # Round up to nearest 100
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Adjust the legend's position
ax.legend(loc='upper left')

# Add title and labels
plt.title('Manufacturing and Production Trends')
plt.xlabel('Year')
plt.ylabel('Amount')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-161902_3.png', bbox_inches='tight')

# Clear the current image state
plt.clf()