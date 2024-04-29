
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data dictionary
data = {'Category': ['Residential', 'Commercial', 'Industrial'],
        'Electricity (kWh)': [5000, 8000, 10000],
        'Gas (kWh)': [3000, 5000, 8000],
        'Water (gal)': [4000, 6000, 7000],
        'Solar (kWh)': [2000, 3000, 4000],
        'Wind (kWh)': [1000, 2000, 3000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    # Set x axis ticks and ticklabels
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])

    # Set y axis ticks and ticklabels
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value <= 10:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    elif max_total_value <= 100:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    elif max_total_value <= 1000:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    else:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot data as area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
             labels=['Electricity', 'Gas', 'Water', 'Solar', 'Wind'], colors=['purple', 'green', 'blue', 'orange', 'red'],
             alpha=0.4)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5)

# Set legend outside of the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

# Set title and labels
ax.set_title('Energy Consumption by Sector')
ax.set_xlabel('Category')
ax.set_ylabel('Amount (kWh/gal)')

# Automatically resize image and save figure
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_16.png', bbox_inches='tight')

# Clear current image state
plt.clf()