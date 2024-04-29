
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Truck (Miles)': [20000, 22000, 24000, 26000, 28000],
        'Rail (Miles)': [15000, 16000, 17000, 18000, 19000],
        'Air (Miles)': [10000, 11000, 12000, 13000, 14000],
        'Sea (Miles)': [5000, 5500, 6000, 6500, 7000],
        'Pipeline (Miles)': [3000, 3500, 4000, 4500, 5000]}

# Create dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Calculate max total value and set y limit and ticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Truck', 'Rail', 'Air', 'Sea', 'Pipeline'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.7)

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Miles')

# Set title
ax.set_title('Transportation Mileage Trends from 2015 to 2019')

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Set legend
ax.legend(loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_63.png', bbox_inches='tight')

# Clear current image state
plt.clf()