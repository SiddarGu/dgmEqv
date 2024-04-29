
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dictionary with the given data
data = {
    'Country': ['United States', 'China', 'India', 'Russia', 'Brazil', 'Australia', 'Canada'],
    'Carbon Emissions (Million Metric Tons)': [5.2, 10.5, 3.8, 4.1, 2.4, 1.9, 2.2],
    'Renewable Energy (%)': [35, 20, 15, 25, 30, 40, 35],
    'Green Space (%)': [25, 18, 20, 22, 35, 40, 30],
    'Water Consumption (Liters per Capita)': [120, 135, 100, 150, 130, 140, 125],
    'Waste Production (Kilograms per Capita)': [350, 300, 250, 400, 375, 200, 325]
}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set the index to be the Country column
df.set_index('Country', inplace=True)

# Create a figure using a larger figsize
fig = plt.figure(figsize=(10, 8))

# Plot the heatmap using imshow()
ax = plt.imshow(df, cmap='coolwarm')

# Set the ticks and ticklabels for x and y axis
plt.xticks(np.arange(len(df.columns)), df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df.index)), df.index)

# Add a colorbar
plt.colorbar()

# Add a title
plt.title('Environmental Impact by Country')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_45.png', bbox_inches='tight')

# Clear the current image state
plt.clf()