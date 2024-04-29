
# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Sector': ['Residential', 'Commercial', 'Industrial'],
        'Energy Consumption (kWh)': [5000, 8000, 12000],
        'CO2 Emissions (kg)': [3000, 6000, 8000],
        'Water Usage (L)': [4000, 5000, 6000],
        'Waste Produced (kg)': [1000, 1500, 2000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot data as stackplot
ax.stackplot(df['Sector'], df['Energy Consumption (kWh)'], df['CO2 Emissions (kg)'], df['Water Usage (L)'], df['Waste Produced (kg)'], labels=['Energy Consumption (kWh)', 'CO2 Emissions (kg)', 'Water Usage (L)', 'Waste Produced (kg)'])

# Set suitable colors and transparency
colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']
for i in range(len(ax.collections)):
    ax.collections[i].set_color(colors[i])
    ax.collections[i].set_alpha(0.7)

# Add background grid lines
ax.grid(axis='y', linestyle='--')

# Set legend's position and title
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title('Environmental Impact by Sector')

# Automatically resize the image
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_18.png', bbox_inches='tight')