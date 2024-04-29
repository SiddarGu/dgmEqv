
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {'Product': ['Solar Panels', 'Wind Turbines', 'Electric Vehicles', 'Sustainable Packaging', 'Composting', 'Green Buildings', 'Recycling Programs', 'Renewable Energy Credits'], 'Energy Consumption (kWh)': [200, 150, 100, 80, 50, 180, 120, 250], 'Water Usage (gal)': [250, 180, 120, 100, 70, 200, 150, 300], 'Waste Production (lbs)': [100, 80, 60, 50, 40, 80, 70, 100]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Energy Consumption (kWh)', 'Water Usage (gal)', 'Waste Production (lbs)'], colors=['#F94D4D', '#4DB4F9', '#7DD45A'], alpha=0.7)

# Set x and y ticks and tick labels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(df.index)
    ax.set_xticklabels(df['Product'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks().astype(int))

# Set background grid lines
ax.grid(color='#E3E3E3', linestyle='--', linewidth=1, alpha=0.5)

# Set legend position and title
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Environmental Impact of Sustainable Practices')

# Set title
ax.set_title('Environmental Impact of Sustainable Practices')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-145339_67.png', bbox_inches='tight')

# Clear current image state
plt.clf()