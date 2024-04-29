
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data
data = {
    'Indicator': ['Carbon Emissions (tonnes)', 'Renewable Energy (%)', 'Water Consumption (litres)', 'Waste Production (tonnes)', 'Air Quality (AQI)', 'Green Space (sq km)'],
    'Country A': [100000, 20, 500, 100, 50, 1000],
    'Country B': [75000, 30, 800, 80, 60, 800],
    'Country C': [50000, 40, 1000, 60, 70, 600],
    'Country D': [25000, 50, 1200, 40, 80, 400],
    'Country E': [10000, 60, 1500, 20, 90, 200]
}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Set the index as 'Indicator'
df.set_index('Indicator', inplace=True)

# Transpose the dataframe to make the countries as columns
df = df.T

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap
heatmap = sns.heatmap(df, annot=True, cmap='Blues', cbar=False)

# Set the x and y ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, ha='right', rotation_mode='anchor', rotation=45)
ax.set_yticklabels(df.index, rotation_mode='anchor', rotation=0)

# Set the title
plt.title('Environmental Sustainability Metrics by Country')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_73.png', bbox_inches='tight')

# Clear the current image state
plt.clf()