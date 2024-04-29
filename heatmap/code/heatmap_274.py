
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Convert data into dictionary
data = {'Country': ['United States', 'China', 'Germany', 'Japan', 'India'],
        'CO2 Emissions (metric tons)': [5.2, 10.5, 3.5, 4.5, 8.2],
        'Renewable Energy Production (GWh)': [450, 600, 300, 350, 550],
        'Waste Management (%)': [70, 80, 90, 75, 65],
        'Water Usage (Liters per capita)': [5000, 6000, 4000, 4500, 6500],
        'Air Quality Index': [35, 50, 40, 45, 60]}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap using pandas dataframe
im = ax.imshow(df.iloc[:, 1:].values, cmap='Blues')

# Set x and y ticks and labels
ax.set_xticks(np.arange(df.shape[1]-1))
ax.set_yticks(np.arange(df.shape[0]))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'])

# Loop over data dimensions and create text annotations
for i in range(df.shape[0]):
    for j in range(df.shape[1]-1):
        text = ax.text(j, i, df.iloc[i, j+1],
                       ha="center", va="center", color="w")

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)

# Set title
ax.set_title("Environmental Sustainability Across Countries")

# Automatically resize image and save figure
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-162116_9.png', bbox_inches='tight')