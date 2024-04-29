
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'France'],
        'Electricity Consumption (kWh per capita)': [12000, 9000, 6000, 5000, 4000, 3000],
        'Renewable Energy (%)': [25, 15, 20, 30, 10, 25],
        'Energy Efficiency (%)': [50, 45, 55, 60, 40, 55],
        'Energy Imports (%)': [15, 20, 10, 5, 25, 10],
        'Electricity Production (TWh)': [1000, 800, 500, 400, 300, 200]}

# Create dataframe
df = pd.DataFrame(data)

# Set x and y labels
x_labels = ['Electricity Consumption (kWh per capita)', 'Renewable Energy (%)', 'Energy Efficiency (%)', 'Energy Imports (%)', 'Electricity Production (TWh)']
y_labels = ['United States', 'China', 'Japan', 'Germany', 'India', 'France']

# Set figure size
plt.figure(figsize=(12, 8))

# Plot heatmap
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='coolwarm', cbar=True)

# Set x and y ticks
ax.set_xticklabels(x_labels, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(y_labels, rotation=0, ha='right', rotation_mode='anchor')

# Set title
plt.title('Energy and Utilities in Different Countries')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-155147_37.png', bbox_inches='tight')

# Clear current image state
plt.clf()