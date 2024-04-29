
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Define data as a dictionary
data = {'Category': ['Transportation', 'Agriculture', 'Energy', 'Waste Management'],
        'Carbon Dioxide (Tonnes)': [250000, 500000, 1000000, 250000],
        'Methane (Tonnes)': [100000, 1000000, 250000, 50000],
        'Nitrous Oxide (Tonnes)': [50000, 750000, 100000, 25000],
        'Sulfur Dioxide (Tonnes)': [10000, 50000, 25000, 10000],
        'Water Usage (Liters)': [250000000, 500000000, 1000000000, 50000000],
        'Electricity Usage (kWh)': [50000000, 100000000, 200000000, 10000000]}

# Convert data to a dataframe
df = pd.DataFrame(data)

# Set the index to Category
df.set_index('Category', inplace=True)

# Set the size of the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap using seaborn
sns.heatmap(df, annot=True, cmap='Blues', cbar=False)

# Set the ticks and ticklabels for the x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set the title
plt.title('Greenhouse Gas Emissions and Resource Usage by Industry')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-124154_66.png', bbox_inches='tight')

# Clear the current image state
plt.clf()